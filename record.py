#-*- coding: utf-8 -*-

#import librosa.display
import librosa
import pyaudio
import wave

import glob
from collections import defaultdict

import os
import shutil
import numpy as np

from sys import byteorder
from array import array
from struct import pack

class VOICE_RECORD():
    def __init__(self, chunk=8196, format=pyaudio.paInt16, channels=1, rate=44100, seconds=2):
        self.CHUNK=chunk
        self.FORMAT=format
        self.CHANNELS=channels
        self.RATE=rate
        self.SECONDS=seconds
        
        self.THRESHOLD = 500
        self.THRESHOLD_dB = 30 #librosa.core.amplitude_to_db(np.array([self.THRESHOLD]))
        self.THRESHOLD = int(librosa.core.db_to_amplitude(self.THRESHOLD_dB))

        self.SAMPLE_NAME = "./speaker/voice/"
        self.SAMPLE_NUM = 7
        self.MAX_ACCOUNT = 999 - self.SAMPLE_NUM
        self.is_record = False

        self.TARGET_DB = 80

    def account_number(self):
        return len(glob.glob(self.SAMPLE_NAME + '[0-9][0-9][0-9]'))

    def _account_renumber(self):
        sample_folders = glob.glob(self.SAMPLE_NAME + '[0-9][0-9][0-9]')
        numbers = [int(folder[-3:]) for folder in sample_folders]
        numbers.sort()
        
        for i, sample_num in enumerate(numbers[:self.SAMPLE_NUM]):
            if i != sample_num:
                print ('account_reunber error: sub sample folder is delete')
                exit()

        for i, folder in enumerate(numbers[self.SAMPLE_NUM:]):
            os.rename(self.SAMPLE_NAME + str(format(folder,'03')), self.SAMPLE_NAME + str(format(self.SAMPLE_NUM + i,'03')))

        return len(numbers) - self.SAMPLE_NUM

    def is_silent(self, data):
        "Returns 'True' if below the 'silent' threshold"

        return np.amax(data) < 500 #self.THRESHOLD

    def record(self):
        p = pyaudio.PyAudio()

        stream = p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK)

        end_sec = int(self.RATE / self.CHUNK * self.SECONDS)
        end_silent_timer = 0
        recording = False

        print("* recording")
        self.is_record = True

        frames = np.empty([0], dtype = np.int16)
        while 1: 
            # little endian, signed short
            data = np.fromstring(stream.read(self.CHUNK), dtype = np.int16)
            if byteorder == 'big':
                data.byteswap(True)
            frames = np.append(frames, data)
            
            silent = self.is_silent(data)
            print ('silent ', silent, 'recording ', recording, 'end_silent_timer ', end_silent_timer)
            
            if not recording and not silent:
                recording = True
            elif recording:
                if not silent:
                    end_silent_timer = 0
                else:
                    end_silent_timer += 1
                
                if end_silent_timer > end_sec:
                    break

        self.is_record=False
        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        print ((frames.shape))
        #lbrosa 데이터 형태로 변환
        _frames = librosa.util.buf_to_float(frames, dtype=np.float32)

        print ((_frames.shape))
        #초반, 후반 무음 제거
        frames, index = librosa.effects.trim(_frames, top_db=self.THRESHOLD_dB)
        print (librosa.get_duration(_frames, sr=self.RATE), librosa.get_duration(frames, sr=self.RATE))
        
        """
        #충분한 mfcc데이터 개수가 모이지 않는다면 배속을 느리게 설정하여 시간을 늘인다
        mfcc = librosa.feature.mfcc(y=frames, sr=self.RATE, n_mfcc = 50).T
        if mfcc.shape[0] < 2500:
            frames = librosa.effects.time_stretch(frames, librosa.get_duration(frames, sr=self.RATE) / 15)
            _mfcc = librosa.feature.mfcc(y=frames, sr=self.RATE, n_mfcc = 50).T
            print _mfcc.shape
        print 'mfcc :', mfcc.shape
        """

        return frames

    def remove_silent(self, frames):
        trigger = False
        start = -1
        end = -1

        for i, f in enumerate(frames):
            if trigger and f < self.THRESHOLD:
                end = i
                break
            elif f > self.THRESHOLD:
                strat = i
                trigger = True

        if not trigger:
            return np.any([False])
        else:
            return frames[start:end], frames[end:]


    def delete(self, number):
        if number < self.SAMPLE_NUM:
            print ('SAMPLE FILE NOT DELETE')
            exit()
        #해당 번호 데이터 삭제
        shutil.rmtree(self.SAMPLE_NAME + str(format(number,'03')), ignore_errors=True)
        #폴더 번호 정리
        self._account_renumber()


    def save_wav(self, frames):
        print ('save_wav----------------------------------------------------')
        
        #무음 예외 처리
        if frames.shape == (self.CHUNK,):
            print ('save_wav ERROR : No record')
            print ('wav file non save')
            return False

        #폴더 번호가 정리 안되어 있을 경우를 대비하기 위해서 폴더 번호 정리
        max_account = self._account_renumber()
        #등록된 최대 사용자 수 초과시
        if max_account >= self.MAX_ACCOUNT:
            print ('save_wav ERROR : account_max, please use this after delete account')
            return False

        #새로운 사용자 폴더 생성 후 음성파일 저장
        create_num = str(format(self.SAMPLE_NUM + max_account,'03'))
        folder = self.SAMPLE_NAME + create_num

        if not os.path.isdir(folder):
            print (folder, 'is create')
            os.mkdir(folder)

        intervals = librosa.effects.split(frames, top_db=self.THRESHOLD_dB)

        for i , interval in enumerate(intervals):
            print (interval, interval[1] - interval[0])

            if interval[1] - interval[0] > self.RATE * 1.5:
                path = folder + '/' + str(format(i,'04')) + '.wav'
                librosa.output.write_wav(path, frames[interval[0]:interval[1]], self.RATE)


        #path = folder + '/' + create_num + '.wav'
        #librosa.output.write_wav(path, frames, self.RATE)

    def temp_save(self, path, frames):
        librosa.output.write_wav(path, frames, self.RATE)

    def temp_slice(self, path):
        frames, rate = librosa.load(path, sr= self.RATE)
        frames = librosa.util.normalize(frames, norm=np.inf, axis = None)
        frames, interval = librosa.effects.trim(frames, top_db=self.THRESHOLD_dB)

        print (self.THRESHOLD_dB, self.THRESHOLD)

        intervals = librosa.effects.split(frames, top_db=self.THRESHOLD_dB, ref=np.max, frame_length= 2048, hop_length=512)

        #print('interval')
        for i , interval in enumerate(intervals):
            print (interval, interval[1] - interval[0], len(frames))

            if interval[1] - interval[0] > self.RATE * 1 and path[-4:] == '.wav':
                _path = path[:-4] + '-' + str(format(i,'04')) + '.wav'
                _frame = frames[interval[0]:interval[1]]
                _frame,_ = librosa.effects.hpss(_frame)
                #_frame = librosa.util.normalize(_frame, norm=np.inf, axis = None)

                librosa.output.write_wav(_path, _frame, self.RATE)


if __name__ == '__main__' :
    a = VOICE_RECORD(seconds=2)
    #a.delete()
    frames = a.record()
    a.temp_save('./valid.wav', frames)
    frames, sr = librosa.load('./valid.wav', sr = 44100)
    #a.save_wav(frames)
    #frames = librosa.util.normalize(frames, norm=np.inf, axis = None)
    #frames_h, frames_p = librosa.effects.hpss(frames)
    #a.temp_save('./test_h.wav', frames_h)
    #a.temp_save('./test_p.wav', frames_p)

    #frames = librosa.util.normalize(frames, norm=np.inf, axis = None)
    #a.temp_save('./test.wav', frames)
    
    #frames = librosa.util.normalize(frames, norm=-np.inf, axis = None)
    #a.temp_save('./test1.wav', frames)
    #a.temp_slice('./valid.wav')
    
    if 0:
        from pydub import AudioSegment
        from pydub.playback import play

        song = AudioSegment.from_wav("./valid.wav")

        # boost volume by 6dB
        louder_song = song + 6

        # reduce volume by 3dB
        quieter_song = song - 3

        #Play song
        play(louder_song)

        #save louder song 
        louder_song.export("./test.wav", format='wav')
        

    if 0:
        folders = glob.glob(a.SAMPLE_NAME + '[0-9][0-9][0-9]')
        folders.sort()
        for i, folder in enumerate(folders):
            print("----------------------------------------------")
            wavs = glob.glob(folder + '/*.wav')
            for wav in wavs:
                a.temp_slice(wav)
                os.remove(wav)
            print ("Label {0} has files {1}".format(folder, ','.join(wavs)))
        
#-*- coding: utf-8 -*-
import librosa
import record

import glob
from collections import defaultdict

import os
import shutil
import numpy as np

class MFCC_EXTRACT():
    def __init__(self):
        self.SAMPLE_NAME = "./speaker/voice/"
        self.MFCC_NAME = "./speaker/mfcc/"
        self.MFCC_NUMBER = 20
        self.SAMPLE_NUM = 7
        self.MAX_ACCOUNT = 999 - self.SAMPLE_NUM

        self.MEL_NUMBER = self.MFCC_NUMBER# + 128
        self.SPEC_NUMBER = 10
        self.ETC_NUMBER = 12 #+ 6+ 384

        self.FEATURE_NUMBER = 20 + 12#self.MEL_NUMBER + self.SPEC_NUMBER + self.ETC_NUMBER

    def _account_renumber(self):
        mfcc_folders = glob.glob(self.MFCC_NAME + '[0-9][0-9][0-9]')
        numbers = [int(folder[-3:]) for folder in mfcc_folders]
        numbers.sort()
        
        for i, sample_num in enumerate(numbers[:self.SAMPLE_NUM]):
            if i != sample_num:
                print ('account_renumber error: sub sample folder is delete')
                exit()

        for i, folder in enumerate(numbers[self.SAMPLE_NUM:]):
            os.rename(self.MFCC_NAME + str(format(folder,'03')), self.MFCC_NAME + str(format(self.SAMPLE_NUM + i,'03')))

        return len(numbers) - self.SAMPLE_NUM

    def delete(self, number):
        if number < self.SAMPLE_NUM:
            print ('SAMPLE FILE NOT DELETE')
            exit()
        #해당 번호 데이터 삭제
        shutil.rmtree(self.MFCC_NAME + str(format(number,'03')), ignore_errors=True)
        #폴더 번호 정리
        self._account_renumber()

#----------------------------------------------------------------------------------------------------------------
    def frame_to_mfcc(self, frame, rate):
        mfcc = librosa.feature.mfcc(y=frame, sr=rate, n_mfcc = self.MFCC_NUMBER)
        #mfcc_delta = librosa.feature.delta(mfcc)
        #mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
        
        #mfcc = np.append(mfcc, mfcc_delta, axis=0)
        #mfcc = np.append(mfcc, mfcc_delta2, axis=0)

        #mfcc = np.append(mfcc, librosa.feature.melspectrogram(y=frame, sr=rate), axis=0)
        
        # MFCC_NUMBER + MEL_NUMBER
        return mfcc.T

    def one_folder_to_mfcc(self, folder_name, rate):
        wavs = glob.glob(folder_name + '/*.wav')
        x_data = np.empty([0, self.MEL_NUMBER])
        for wav in wavs:
            frame, rate = librosa.load(wav, sr=rate)
            mfcc = self.frame_to_mfcc(frame, rate)
            x_data = np.append(x_data, mfcc, axis=0)

        print ("MFCC Label {0} has files {1}".format(folder_name, ','.join(wavs)))
        return x_data
#----------------------------------------------------------------------------------------------------------------

    def frame_to_spec(self, frame, rate):
        spec = librosa.feature.spectral_centroid(y=frame, sr=rate)
        spec = np.append(spec, librosa.feature.spectral_bandwidth(y=frame, sr=rate), axis = 0)
        spec = np.append(spec, librosa.feature.spectral_contrast(y=frame, sr=rate), axis=0)
        spec = np.append(spec, librosa.feature.spectral_rolloff(y=frame, sr=rate), axis=0)

        # 1 + 1 + 7 + 1
        return spec.T

    def one_folder_to_spec(self, folder_name, rate):
        wavs = glob.glob(folder_name + '/*.wav')
        x_data = np.empty([0, self.SPEC_NUMBER])
        for wav in wavs:
            frame, rate = librosa.load(wav, sr=rate)
            spec = self.frame_to_spec(frame, rate)
            x_data = np.append(x_data, spec, axis=0)

        print ("SPEC Label {0} has files {1}".format(folder_name, ','.join(wavs)))
        return x_data
#----------------------------------------------------------------------------------------------------------------

    def frame_to_etc(self, frame, rate):
        etc = librosa.feature.chroma_stft(y=frame, sr=rate)
        ####etc = librosa.feature.zero_crossing_rate(y=frame)
        #etc = np.append(etc, librosa.feature.rmse(y=frame), axis=0)
        #etc = np.append(etc, librosa.feature.poly_features(y=frame, sr=rate), axis=0)
        #etc = np.append(etc, librosa.feature.tonnetz(y=frame, sr=rate), axis=0)
        #etc = np.append(etc, librosa.feature.chroma_stft(y=frame, sr=rate), axis=0)
        #etc = np.append(etc, librosa.feature.tempogram(y=frame, sr=rate), axis=0)
        
        # 1 + 1 + 2 + 6 + 12 + 384
        return etc.T

    def one_folder_to_etc(self, folder_name, rate):
        wavs = glob.glob(folder_name + '/*.wav')
        x_data = np.empty([0, self.ETC_NUMBER])
        for wav in wavs:
            frame, rate = librosa.load(wav, sr=rate)
            etc = self.frame_to_etc(frame, rate)
            x_data = np.append(x_data, etc, axis=0)

        print ("ETC Label {0} has files {1}".format(folder_name, ','.join(wavs)))
        return x_data
#----------------------------------------------------------------------------------------------------------------

    def all_save(self, rate):
        sample_folders = glob.glob(self.SAMPLE_NAME + '[0-9][0-9][0-9]')
        sample_folders.sort()
        for folder in sample_folders:
            print ("-----------------------------------------------")
            
            mfcc_folder_name = self.MFCC_NAME + folder[-3:]
            if not os.path.isdir(mfcc_folder_name):
                os.mkdir(mfcc_folder_name)
            
            if not os.path.exists(mfcc_folder_name + '/mfcc.npy'):
                x_data = self.one_folder_to_mfcc(folder, rate)
                np.save(mfcc_folder_name + '/mfcc', x_data)

            #if not os.path.exists(mfcc_folder_name + '/spec.npy'):
            #    x_data = self.one_folder_to_spec(folder, rate)
            #    np.save(mfcc_folder_name + '/spec', x_data)
            
            if not os.path.exists(mfcc_folder_name + '/etc.npy'):
                x_data = self.one_folder_to_etc(folder, rate)
                np.save(mfcc_folder_name + '/etc', x_data)
#----------------------------------------------------------------------------------------------------------------

    def load(self, path, total_num):
        x_data = np.load(path)
        x_data = x_data.astype(dtype=np.float32)        
        
        if total_num <= 0 or len(x_data) < total_num:
            _total_num = len(x_data)
        else:
            _total_num = total_num

        return x_data[:_total_num]

    def all_load(self):
        x_data = np.empty([0, self.FEATURE_NUMBER])
        y_data = np.empty([0])

        mfcc_folders = glob.glob(self.MFCC_NAME + '[0-9][0-9][0-9]')
        mfcc_folders.sort()

        for i, folder in enumerate(mfcc_folders):
            print ("-----------------------------------------------")
            x_tmp = self.load(folder+'/mfcc.npy', total_num)
            x_tmp = np.insert(x_tmp, [self.MEL_NUMBER], self.load(folder+'/etc.npy', total_num), axis=1)

            x_data = np.append(x_data, x_tmp, axis=0)
            y_data = np.append(y_data, np.full((len(x_tmp),),i, dtype=np.int32), axis=0)
            print ('x_data :', x_tmp.shape)

            print ("temp_load Label {0} ".format(folder))

        return (x_data, y_data)

    def temp_frame_to_feature(self, frames, rate):
        x_data = np.empty([0, self.FEATURE_NUMBER])

        frames = librosa.util.normalize(frames, norm=np.inf, axis = None)
        intervals = librosa.effects.split(frames, top_db=50, ref=np.max, frame_length= 2048, hop_length=512)
        interval_num = 0;
        for i , interval in enumerate(intervals):

            if interval[1] - interval[0] > rate * 1:
                interval_num += 1
                _frame = frames[interval[0]: interval[1]]
                _frame,_ = librosa.effects.hpss(_frame)
                #_frame = librosa.util.normalize(_frame, norm=np.inf, axis = None)
                feature = librosa.feature.mfcc(y=_frame, sr=rate, n_mfcc=self.MFCC_NUMBER, n_fft=1024, hop_length = 256)
                #_mfcc_delta = librosa.feature.delta(feature)
                #_mfcc_delta2 = librosa.feature.delta(feature, order=2)
                
                #feature = np.append(feature, _mfcc_delta, axis=0)
                #feature = np.append(feature, _mfcc_delta2, axis=0)
                #feature = np.append(feature, librosa.feature.melspectrogram(y=_frame, sr=rate, n_fft=1024, hop_length = 256), axis=0)
                                
                # MFCC_NUMBER * 3

                #feature = np.append(feature, librosa.feature.spectral_centroid(y=_frame, sr=rate, n_fft=1024, hop_length = 256), axis=0)
                #feature = np.append(feature, librosa.feature.spectral_bandwidth(y=_frame, sr=rate, n_fft=1024, hop_length = 256), axis=0)
                #feature = np.append(feature, librosa.feature.spectral_contrast(y=_frame, sr=rate, n_fft=1024, hop_length = 256), axis=0)
                #feature = np.append(feature, librosa.feature.spectral_rolloff(y=_frame, sr=rate, n_fft=1024, hop_length = 256), axis=0)
                # 1 + 1 + 7 + 1

                #feature = np.append(feature, librosa.feature.zero_crossing_rate(y=_frame), axis=0)
                #feature = np.append(feature, librosa.feature.rmse(y=_frame), axis=0)
                #feature = np.append(feature, librosa.feature.poly_features(y=_frame, sr=rate), axis=0)
                #feature = np.append(feature, librosa.feature.tonnetz(chroma=librosa.feature.chroma_cqt(y=_frame, sr=rate, hop_length = 256), sr=rate), axis=0)
                feature = np.append(feature, librosa.feature.chroma_stft(y=_frame, sr=rate, n_fft=1024, hop_length = 256), axis=0)
                #feature = np.append(feature, librosa.feature.tempogram(y=_frame, sr=rate), axis=0)
                # 1 + 1 + 2 + 6 + 12 + 384

                x_data = np.append(x_data, feature.T, axis=0)

                #librosa.output.write_wav(path[:-4]+str(i)+'.wav', frames[interval[0]: interval[1]], rate)
        #mfcc = librosa.feature.mfcc(y=frames, sr=rate, n_mfcc=self.MFCC_NUMBER).T
        #mfcc = self._normalization(mfcc)
        print ('valid feature :', x_data.shape, 'inteval_num :', interval_num)
        return x_data

    def temp_valid_to_feature(self, path, rate):
        frames, rate = librosa.load(path, sr=rate)
        x_data = self.temp_frame_to_feature(frames, rate)
        return x_data

    def temp_load(self, total_num, test_persent):
        x_data = np.empty([0, self.FEATURE_NUMBER])
        y_data = np.empty([0])

        x_test_data = np.empty([0, self.FEATURE_NUMBER])
        y_test_data = np.empty([0])

        mfcc_folders = glob.glob(self.MFCC_NAME + '[0-9][0-9][0-9]')
        mfcc_folders.sort()
        print (mfcc_folders)
        for i, folder in enumerate(mfcc_folders):
            print ("-----------------------------------------------")
            x_tmp = self.load(folder+'/mfcc.npy', total_num)
            #x_tmp = np.insert(x_tmp, [self.MEL_NUMBER], self.load(folder+'/spec.npy', total_num), axis=1)
            x_tmp = np.insert(x_tmp, [self.MEL_NUMBER], self.load(folder+'/etc.npy', total_num), axis=1)
            #x_tmp = np.insert(x_tmp, [self.MEL_NUMBER + self.SPEC_NUMBER], self.load(folder+'/etc.npy', total_num), axis=1)

            if total_num <= 0 or len(x_tmp) < total_num:
                _total_num = len(x_tmp)
            else:
                _total_num = total_num
            
            test_num = int(_total_num * test_persent / 100)

            x_tmp_test = x_tmp[_total_num-test_num:_total_num]
            x_tmp = x_tmp[:_total_num - test_num*2 ]

            x_data = np.append(x_data, x_tmp, axis=0)
            y_data = np.append(y_data, np.full((_total_num - test_num - test_num,),i, dtype=np.int32), axis=0)
            x_test_data = np.append(x_test_data, x_tmp_test, axis=0)
            y_test_data = np.append(y_test_data, np.full((test_num,),i, dtype=np.int32), axis=0)
            print ('x_data :', x_tmp.shape, ', x_test_data :', x_tmp_test.shape)

            print ("temp_load Label {0} ".format(folder))
        
        print ('total_len : ', len(x_data) + len(x_test_data), 
               'test_num : ', len(x_test_data),
               'remainder : ', len(x_data))

        return (x_data, y_data, x_test_data, y_test_data)


if __name__ == '__main__' :
    mfcc = MFCC_EXTRACT()
    #mfcc.wav_to_melspectogram('./valid.wav', 44100)
    mfcc.all_save(rate=44100)
    #mfcc.all_load(2500)
    #x_data, y_data = mfcc.all_load()
    #print (mfcc.wav_to_mfcc('./valid.wav',44100).shape)
    #print x_data.shape
    #print y_data.shape
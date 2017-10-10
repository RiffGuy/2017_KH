#-*-coding: utf-8 -*-
import record
import mfcc

def enroll_account(chunk, seconds):
    v = record.VOICE_RECORD(seconds=seconds, rate=44100)
    frames = v.record()
    v.save_wav(frames)

    m = mfcc.MFCC_EXTRACT()
    m.all_save(rate=44100)

def delete_account(number):
    v = record.VOICE_RECORD()
    v.delete(number)

    m = mfcc.MFCC_EXTRACT()
    m.delete(number)

if __name__ == '__main__':
    pass
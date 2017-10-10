#voice_extract.py

import librosa
import glob
from collections import defaultdict

class VoiceFeature(object):
	def __init__(self):
		self.features = defaultdict(list)

	def enroll(self, name, mfcc):
		self.features[name].extend(mfcc)

	def makeOutPut(self):
		print self.features
		f = open('output.txt', 'w')
		#f.write(self.features)
		f.close()

if __name__ == '__main__':
	vf = VoiceFeature()
	sample_name="./sample"
	for i in range(3):
		print "-----------------------------------------------"
		print i
		foldername=sample_name+str(i)
		wavs = glob.glob(foldername + '/*.wav')
		for wav in wavs:
			rosa_signal, rosa_fs = librosa.load(wav)
			mfcc = librosa.feature.mfcc(y=rosa_signal,sr=rosa_fs)
			vf.enroll(foldername,mfcc)
		print "Label {0} has files {1}".format(foldername, ','.join(wavs))
	vf.makeOutPut()

            

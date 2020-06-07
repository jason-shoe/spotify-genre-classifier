from os import path
from pydub import AudioSegment
import sys
from ffprobe import FFProbe
import soundfile as sf
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

audioDataframe = pd.DataFrame(columns = np.arange(200))
for x in range(1,10418):
    print(int(x/10418*10000)/100,x)
    try:
        destination = 'wav/' + str(x) + '.wav'
        y, sr = librosa.load(destination, dtype='float32')

        cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        sliceAmount = 100
        t = np.arange(len(cent[0][:sliceAmount]))

        sp = np.fft.fft(cent[0][:sliceAmount])
        freq = np.fft.fftfreq(t.shape[-1])
        vals = []
        for y in range(100):
            val  = y
            amp = math.pow(math.pow(sp.real[val],2)+math.pow(sp.imag[val],2),0.5)
            angle = math.tanh(sp.imag[val]/sp.real[val])
            vals.append(amp)
            vals.append(angle)
    except:
        print("no file")
        vals = [0] * 200
    audioDataframe.loc[x] = vals
    if(x%1000 == 0):
        audioDataframe.to_csv('../data/2audioSongList.csv')
audioDataframe.to_csv('../data/2audioSongList.csv')
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:16:01 2020

@author: andro
"""

import numpy as np
import wave as wv
#import librosa

def inv_conv_old(a):
    res = []
    for i in range(len(a)):
        res.append(np.dot(a[i:], np.roll(a,i)[i:]))
    print("converting array")
    return np.array(res)

def inv_conv(a):
    return np.convolve(a, np.flip(a, 0))[-len(a):]

def runmean(a, width):
    res = []
    amod = np.concatenate((np.full(width, np.mean(a[:width])), a, np.full(width, np.mean(a[-width:]))))
    for i in range(len(a)):
        res.append(np.mean(amod[i : i + 2 * width]))
    return np.array(res)
import matplotlib.pyplot as plt 

def getpeaks(a):
    return

def loadwav(filename):
    # Read file to get buffer                                                                                               
    ifile = wv.open(filename)
    samples = ifile.getnframes()
    audio = ifile.readframes(samples)

    # Convert buffer to float32 using NumPy                                                                                 
    audio_as_np_int16 = np.frombuffer(audio, dtype=np.int16)
    audio_as_np_float32 = audio_as_np_int16.astype(np.float32)

    # Normalise float32 array so that values are between -1.0 and +1.0                                                      
    max_int16 = 2**15
    audio_normalised = audio_as_np_float32 / max_int16
    return audio_normalised

def loadcsv(filename):
    lines = open(filename, "r").readlines()[2:]
    time = []
    sig = []
    for l in lines:
        parts = l.split(',')
        time.append(float(parts[0]))
        sig.append(float(parts[1]))
    return np.array(time), np.array(sig)

noisify = lambda a, dev: a + np.random.normal(0, dev, len(a))

waveshift = lambda a, shift: np.concatenate((np.zeros(shift), a[:-shift]))
#!/usr/bin/python

import librosa
import librosa.display

def plot_wav(y, sr, title):
    plt.figure()
    librosa.display.waveplot(y, sr)
    plt.title(title)
    #plt.show()
    name = str(title) + ".png"
    plt.savefig(name)

def plot_spec(spec, sr, title):
    # spec = melspec, logmelspec
    plt.figure()
    librosa.display.specshow(spec, sr=sr, x_axis='time', y_axis='mel')
    plt.title(title)
    #plt.show()
    name = str(title) + ".png"
    plt.savefig(name)

def plot_wavnspec(y, sr, spec, title):
    # plot a wavform
    plt.figure()
    plt.subplot(2, 1, 1)
    librosa.display.waveplot(y, sr)
    name1 = str(title) + "_wave"
    plt.title(name1)
    # plot mel spectrogram
    plt.subplot(2, 1, 2)
    librosa.display.specshow(spec, sr=sr, x_axis='time', y_axis='mel')
    name2 = str(title) + "_spec"
    plt.title(name2)
    plt.tight_layout()
    name = str(title) + "_cb.png"
    plt.savefig(name)

def main():
    data = './testdata/0.wav'
    y, sr = librosa.load(data) # Load a wav file
    # sr origin:44100, librosa:22050, sr=xxxx can be set to yours -> sample rate
    # extract log-mel spectrogram feature
    melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
    # (n_fft = window size, hop_length = adjacent distance between windows, n_mels = numbers of mel bands)
    # convert to log scale
    logmelspec = librosa.power_to_db(melspec)
    print ("shape of log-mel-spec: ", logmelspec.shape) #(frequency domain, time domain)
    # extract mfcc features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    print ("shape of mfccs: ", mfccs.shape)










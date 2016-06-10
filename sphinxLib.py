#uses pocketshpinx to get a voice response

import sys,os
import pyaudio
import wave
import os.path as path

MODELDIR = "pocketsphinx/model"
DATADIR = "pocketsphinx/test/data"

def decodeSpeech(hmmd,lmdir,dictp,wavfile):
    import pocketsphinx as ps
    import sphinxbase
    configr = ps.Decoder.default_config()
    configr.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
    configr.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
    configr.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
    speechRec = ps.Decoder(configr)
    wavFile = file(wavfile,'rb')
    wavFile.seek(44)
    speechRec.start_utt()
    while True:
        buf = wavFile.read(1024)
        if buf:
            speechRec.process_raw(buf, False, False)
        else:
            break
    speechRec.end_utt()
    #print ('Best hypothesis segments: ', [seg.word for seg in speechRec.seg()])
    result = " ".join([seg.word for seg in speechRec.seg()]).replace('<s> ','').replace('<sil> ',"")

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

def RecordAndDecode(Seconds = 10):
    fn = "o"+str(x)+".wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * Seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(fn, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    wavfile = fn
    recognised = decodeSpeech(hmdir,lmd,dictd,wavfile)
    return recognised

if __name__ == "__main__":
    for x in range(10):
        recognised = RecordAndDecode()
        print(recognised)
        cm = 'espeak.exe "'+recognised+'"'
        os.system(cm)

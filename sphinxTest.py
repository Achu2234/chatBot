from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import pyaudio

MODELDIR = "pocketsphinx/model"
DATADIR = "pocketsphinx/test/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
decoder = Decoder(config)

stream.start_stream()            #Start the pyaudio recording stream
#While the model-adaption thread is running and no button is clicked: record sound.
while self.running and not ma_is_clicked:
  buf = stream.read(1024)           #read first chunk from the mic-stream
  if buf:
    data_chunk = array('h', buf)
    percent = max(data_chunk)/1000.
    if percent > 1.0:
        percent = 1.0
    #We have to do the following, because we are not in the main thread and want to
    #modify the value of a progressbar
    gtk.gdk.threads_enter()         
    ma_level_progressbar.set_fraction(percent) #Set "level" of the progressbar, which indicates the input volume
    gtk.gdk.threads_leave()
    data_all.extend(data_chunk)
else:
    break
                        
#Stop the recording stream
stream.stop_stream()

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, 'something.raw'), 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])

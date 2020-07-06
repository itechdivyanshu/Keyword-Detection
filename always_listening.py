import sys, os, pyaudio
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

modeldir = "files/sphinx/models"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
#disable -logfn to get logs in console
config.set_string('-logfn', 'files/sphinx.log')
config.set_string('-keyphrase', 'jarvis')
#decoder = Decoder(config)

#decoder.set_kws('keyword', 'keyword.list')
#decoder.set_search('keyword')

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
stream.start_stream()

# Process audio chunk by chunk. On keyword detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
while True:
    buf = stream.read(1024)

    decoder.process_raw(buf, False, False)

    if decoder.hyp() != None:
        #print ([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        for seg in decoder.seg():
        	print(seg.word)
        	break
        print ("Detected keyword, restarting search")
        #
        # Here you run the code you want based on keyword
        #
        decoder.end_utt()
        decoder.start_utt()

import GUI
import duckduckgo
import sphinxLib
import eSpeaker
import splash
from lexicons import *

DEFAULT_LEXICON = "lexicon.txt"
lexicon_file = open(DEFAULT_LEXICON)
lexicon = lexicon_file.read()
    
splash1 = splash.splash()
splash1.mainloop()

root = GUI.GUI(eSpeaker.say,sphinxLib.RecordAndDecode,decode)
root.mainloop()

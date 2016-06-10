import GUI
import duckduckgo
import sphinxLib
import eSpeaker
from lexicons import *

DEFAULT_LEXICON = "lexicon.txt"
lexicon_file = open(DEFAULT_LEXICON)
lexicon = lexicon_file.read();
    

root = GUI.GUI(eSpeaker.say,sphinxLib.RecordAndDecode,decode);
root.mainloop();

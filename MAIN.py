import GUI
import duckduckgo
import sphinxLib
import eSpeaker


root = GUI.GUI(eSpeaker.say,sphinxLib.RecordAndDecode);
root.mainloop();

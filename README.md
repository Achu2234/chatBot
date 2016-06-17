# chatBot
an attempt to make a simple chat bot AI in python, using pocketsphinx for voice recognition, and tkinter for the GUI.
## To run:
Currently this project is in all kinds of pieces that have yet to be put together, but you should still be able to run some of the individual scripts. This may require you to install pocketsphinx via pip:
```
pip install pocketsphinx
```
or:
```
python -m pip install pocketsphinx
```
This requires [swig](http://www.swig.org) to install, as well as [this compiler](https://www.microsoft.com/en-us/download/details.aspx?id=44266) on windows. The compiler may crash due to a missing stdint.h file, which you can get from [here](https://code.google.com/archive/p/msinttypes/). once you have all of this installed correctly, you should be able to run the pocketsphinx examples. None of these have been tested on OSX or Linux, but they should work.
Everything else so far should run with the default python modules for either python 2.7 or 3.5.

To see the main application, run MAIN.py!

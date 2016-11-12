import subprocess
import platform
# DO NOTE: MAC OSX has not been tested yet

def say(message):
    print("saying")
    if platform.system().lower() == "windows":
        proc = subprocess.Popen(["eSpeak.exe",message], shell=True)
    elif platform.system().lower() == "darwin": #Mac OSX will return "darwin"
        proc = subprocess.Popen(["speak",message], shell=True)

if __name__ == "__main__": # if this python module is being run as a script
    if platform.system().lower() == "windows":
        proc = subprocess.Popen(["eSpeak.exe","hello, on Windows!"], shell=True)
    elif platform.system().lower() == "darwin": #Mac OSX will return "darwin"
        proc = subprocess.Popen(["speak","hello, on Mac OSX!"], shell=True)
    elif platform.system().lower() == "linux":
        print("I AM NOT CERTAIN WHAT TO RUN ON THESE SYSTEMS!")

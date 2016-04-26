import subprocess,platform
# DO NOTE: MAC OSX has not been tested yet

def say(message):
    if platform.system().lower() == "windows":
        proc = subprocess.Popen(["eSpeak.exe",message])
    elif platform.system().lower() == "darwin": #Mac OSX will return "darwin"
        proc = subprocess.Popen(["speak",message])

if __name__ == "__main__": # if this python module is being run as a script
    if platform.system().lower() == "windows":
        proc = subprocess.Popen(["eSpeak.exe","hello, on Windows!"])
    elif platform.system().lower() == "darwin": #Mac OSX will return "darwin"
        proc = subprocess.Popen(["speak","hello, on Mac OSX!"])
    elif platform.system().lower() == "linux":
        print("I AM NOT CERTAIN WHAT TO RUN ON THESE SYSTEMS!")

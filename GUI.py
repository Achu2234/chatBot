try:
    from Tkinter import *
except:
    from tkinter import *

class GUI(Tk):
    def __init__(self, say, speechInput, processRequest): #the GUI object should be created with the say and speechInput as functions

        Tk.__init__(self)

        self.title("AI test 1")

        self.minsize(width=300, height=300);

        self.inputFrame = Frame(self);

        self.messageFrame = Frame(self);
        
        self.messageScroll = Scrollbar(self.messageFrame)
        self.messageList = Listbox(self.messageFrame, yscrollcommand = self.messageScroll.set);
        self.messageList.pack(fill=BOTH, expand=1, side = LEFT)
        self.messageScroll.pack(fill=Y, side = RIGHT)
        self.messageScroll.config(command = self.messageList.yview);
        self.messageFrame.pack(fill=BOTH, expand=1)
        
        self.inputFrame.pack(fill=X)
        self.inputBox = Entry(self.inputFrame,);
        self.inputBox.pack(fill=X, expand=1, side = LEFT)
        self.inputButton = Button(self.inputFrame,width = 5, text = "send", command = self.testprint);
        self.speakButton = Button(self.inputFrame,width = 5, text = "speak");
        self.inputButton.pack(side = RIGHT)
        self.speakButton.pack(side = RIGHT)
        self.espeakprocess = None;
        self.say = say
        self.processRequest = processRequest;
    def testprint(self):
        message = self.inputBox.get();
        self.messageList.insert(END,"You Said: "+str(message))
        response = self.processRequest(message);
        self.print(str(response));
    def print(self,message):
        self.say(message);
        self.messageList.insert(END,"I Said: "+str(message))
        self.messageList.see(END)

def defaultProcess(message):
    return message

if __name__ == "__main__":
    import eSpeaker
    root = GUI(eSpeaker.say, None, defaultProcess);
    root.mainloop();

try:
    from Tkinter import *
except:
    from tkinter import *

class splash(Tk):
    def __init__(self):

        Tk.__init__(self)

        self.image = PhotoImage(file="CypherAI.gif");
        
        label = Label(image=self.image)
        label.image = self.image
        label.pack()

        self.overrideredirect(1);
        self.geometry("%dx%d%+d%+d" % (640, 400, self.winfo_screenwidth()/2-320, self.winfo_screenheight()/2-200));
        
        self.after(5000,self.destroy);


if __name__ == "__main__":
    main = splash();
    main.mainloop();
    main.destroy();

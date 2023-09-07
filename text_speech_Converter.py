#text to speech converter
from tkinter import *
from gTTS import gTTS
import os
from tkinter import filedialog
#window
root = Tk()
frame1 = Frame(root,
               bg="green",height="200")
frame1.pack(fill=X)

frame2 = Frame(root,
               bg="light blue",
               height="730")
frame2.pack(fill=X)
label = Label(frame1, text="TEXT TO SPEECH CONVERTER",
              font="bold,20",
              bg="green").pack()
#functions
def input():
    entry = Entry(frame2, width=45,
                  bd=5, font=14)
    entry.place(x=80, y=50)
    entry.insert(0, " ")

    def play():
        language = "en"
        obj = gTTS(text=entry.get(),
                     lang=language,
                    slow=False)
        obj.save("convert.wav")
        os.system("convert.wav")

    button = Button(frame2, text="SUBMIT",
                    width="15", pady=10,
                    font="bold, 15",
                    command=play, bg='yellow')

    button.place(x=270,
                 y=130)

def browseFiles():

    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    r = open(filename, "r")
    t = r.read()
    language = "en"
    myobj = gTTS(text=t, lang=language, slow=False)
    myobj.save("convert.wav")
    os.system("convert.wav")

#placing of buttons
button1 = Button(frame2, text = "INPUT", width=15, pady=10, font="bold,15", command=input, bg="yellow").place(x=270,y=130)

button2 = Button(frame2, text="FILE", width=15,pady=10, font="bold,15", command=browseFiles, bg="yellow").place(x=270,y=230)

button3 = Button(frame2, text="exit", width=15, pady=10, font="bold,15", command=exit, bg="yellow").place(x=270,y=330)

root.title("text to speech convertor")
root.geometry("750x650+450+300")
root.resizable(False, False)
#running the window
root.mainloop()

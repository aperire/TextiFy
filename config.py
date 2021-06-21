import os
from tkinter import *
from PIL import Image, ImageTk
from subprocess import Popen, PIPE, STDOUT

def install():
    p = Popen(['open', '-a', 'Terminal', '-n'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    q = p.communicate("say Installing Requirements. Follow the steps on the terminal")
    q1 = p.communicate('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    q2 = p.communicate("brew install tesseract")
    path = os.getcwd()
    q3 = p.communicate(f"sudo chmod -R 755 {path}/Textify.app")
    q4 = p.communicate("sudo spctl --master-disable")

def install_windows():
    root = Tk()
    root.title(f"Textify Installer @LP SOLUTIONS")
    root.geometry("300x140")
    
    font = "Helvetica"
    
    title = Label(root, text="Install Requirements for TextiFy")
    title.pack()

    img = Image.open("Textify_logo.png")
    img = img.resize((80, 80), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(img)
    label_img = Label(image=test)
    label_img.image = test
    label_img.pack()

    btn_ok = Button(root, width=10, text="Download", command=install)
    btn_ok.pack()
    
    root.mainloop()

install_windows()
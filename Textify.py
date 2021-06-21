from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
from tkinter.ttk import *
from PIL import Image, ImageTk
from datetime import datetime
import os
from functions import *

def textify_windows():
    # Import Image Command
    def import_img():
        files = filedialog.askopenfilenames(title="Select File", initialdir=os.getcwd())
        for file in files:
            listbox_file.insert(END, file)
        return files
    # Delete Selected File Command
    def del_file():
        for index in reversed(listbox_file.curselection()):
            listbox_file.delete(index)
    # Convert Selected Image to String
    def write_str():
        try:
            path = listbox_file.get(listbox_file.curselection())
            string = img_to_txt(path)
            script.insert(END, string)
        except:
            msgbox.showerror("Unsupported Type", "File Type Not Supported!")
            for index in reversed(listbox_file.curselection()):
                listbox_file.delete(index)
    # Fix Grammar and Display
    def grammar():
        text = script.get("1.0", END)
        script.delete("1.0", END)
        script.insert(END, fix_grammar(text))
    # Export as .txt file
    def txt_exp():
        file_name = save_as.get("1.0", END)
        string = script.get("1.0", END)
        write_txt(file_name, string)
        msgbox.showinfo("Notification", "Saved Succesfully!")

    # Initiate
    root = Tk()
    root.title(f"TextiFy @LP SOLUTIONS {datetime.now().year}/{datetime.now().month}/{datetime.now().day}")
    root.geometry("500x1000")

    # Font
    font = "Helvetica"

    # Title
    label_title = Label(root, text="\nWelcome to TextiFy!", font=(font, 30, "bold"))
    label_title.pack()

    # Brand Image
    img = Image.open("lpsol-title.png")
    img = img.resize((160, 20), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(img)
    label_img = Label(image=test)
    label_img.image = test
    label_img.place(x=270, y = 55)
    label_img.pack()
    
    # Import File
    label_import = Label(root, text="\nImport Image", font=(font, 20, "bold"))
    label_import.pack()
    frame_import = Frame(root)
    frame_import.pack(fill="x", padx=5, pady=5)
    btn_import = Button(frame_import, width=10, text="Select File", command=import_img)
    btn_import.pack()
    
    frame_list = Frame(root)
    frame_list.pack(fill="both", padx=5, pady=5)
    scrollbar = Scrollbar(frame_list)
    listbox_file = Listbox(frame_list, selectmode="extended", height=4, yscrollcommand=scrollbar.set)
    listbox_file.pack(fill="both")
    scrollbar.config(command=listbox_file.yview)

    btn_del = Button(frame_import, width=10, text="Withdraw", command=del_file)
    btn_del.pack()
    
    # Display Converted Text
    btn_process = Button(root, text="Process", command=write_str)
    btn_process.pack()
    
    label_display = Label(root, text="Converted Text", font=(font, 20, "bold"))
    label_display.pack()
    script = Text(root, width=70, height=15)
    script.pack()

    # Grammar Check
    btn_grammar = Button(root, text="Grammar Check", command=grammar)
    btn_grammar.pack()

    # Export
    set_title = Label(root, text="Save file as", font=(font, 15, "bold"))
    set_title.pack()
    save_as = Text(root, width=15, height=1)
    save_as.pack()
    btn_txt_export = Button(root, text="Export as .txt", width=10, command=txt_exp)
    btn_txt_export.pack()


    developer = Label(root, text="\n\n\nDeveloped By Eric Lee", font=(font,10))
    contact = Label(root, text="Contact aperire0402@gmail.com for more info\n\t   www.lpsolution.net", font=(font, 10))
    developer.pack()
    contact.pack()
    root.mainloop()


textify_windows()
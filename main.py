import tkinter as tk
import customtkinter as ctk
# pip install customtkinter
import utils as u
from tkinter import filedialog
from PIL import Image

global image

## Function for the interface

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Bitmap Image", "*.bmp")])
    if file_path:
        image = Image.open(file_path)
        alpha = u.find_alpha((wi,he),(image.width,image.height))
        photo = ctk.CTkImage(dark_image=image, size=(alpha*image.width, alpha*image.height))
        image_label.configure(image=photo)
        btnImage.configure(text = "Cambia immagine")
        control_calculate()
        entF.focus_set()


def clear_all():
    btnImage.configure(text = "Carica immagine")
    image_label.configure(image=None)
    entF.delete(0, "end")
    entD.delete(0, "end")
    #btnCom.configure(state="disabled")
    
def control_calculate(event=""):
    lbR.configure(text = "")
    if (btnCom.cget("state")=="disabled"):
        if u.is_pos_int(entF.get()) and u.is_pos_int(entD.get()):
            d = int(entD.get())
            F = int(entF.get())
            if (d >= 0) and (d < (2*F - 2)):                
                if not (image_label.cget("image") is None):
                    btnCom.configure(state="normal")    
            else:
                lbR.configure(text = "Il valore di d deve essere un intero compreso tra 0 e (2F - 2)", text_color = "red")

def calculate(event=""):
    val = entF.get()
    print(u.is_pos_int(val))

def passToD(event):
    entD.focus_set()
        

## Creating interface

### interface style
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

### main window
root = ctk.CTk()
root.geometry("1000x1000")
wi = 1000
he = 1000
root.title("Progetto di compressione delle immagini")
root.resizable(False, False)
### frame of the interface
frame = ctk.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
### Project title
title = ctk.CTkLabel(master=frame, text="Progetto di compressione delle immagini", font = ("Roboto", 24))
title.pack(padx = 10)
### button for importing image
image_loaded = False
btnImage = ctk.CTkButton(frame, text="Carica immagine", command=load_image)
btnImage.pack(pady = 50)
### images
frameIm = ctk.CTkFrame(master = frame)
frameIm.pack()
image_label = ctk.CTkLabel(frameIm, text="")
image_label.pack()
image2_label = ctk.CTkLabel(frameIm, text="")
image2_label.pack()
### F parameter
lbF = ctk.CTkLabel(master=frame, text="Parametro F")
lbF.pack(padx = 10)
### Entry
entF = ctk.CTkEntry(frame, placeholder_text="Parametro F")
entF.pack(padx = 10, pady = 3)

### d parameter
lbD = ctk.CTkLabel(master=frame, text="Parametro d")
lbD.pack(padx = 10)
### Entry
entD = ctk.CTkEntry(frame, placeholder_text="Parametro d")
entD.pack(padx = 10, pady = 3)

### Reset button
btnCl = ctk.CTkButton(frame, text="Ripristina tutto", command=clear_all, fg_color="#df2c14", hover_color = "#c61a09")
btnCl.pack(pady = 20)

### Calculate button
btnCom = ctk.CTkButton(frame, text="Calcola", command=calculate, state="disabled")
btnCom.pack(pady = 20)

### Result paragraph
lbR = ctk.CTkLabel(master=frame, text="")
lbR.pack(padx = 10)

## Events handling
entF.bind("<Return>", passToD)
entF.bind("<Tab>", passToD)
entF.bind("<Key>", control_calculate)
entD.bind("<Key>", control_calculate)
entD.bind("<Return>", calculate)

root.mainloop()
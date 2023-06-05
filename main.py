import tkinter as tk
import customtkinter as ctk
# pip install customtkinter
import utils as u
from tkinter import filedialog
from PIL import Image, ImageTk

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
        #if btnCom.cget("state")=="disabled":
        #    btnCom.configure(state="normal")


def clear_all():
    btnImage.configure(text = "Carica immagine")
    image_label.configure(image=None)
    entF.delete(0, "end")
    entD.delete(0, "end")
    #btnCom.configure(state="disabled")
    

def calculate():
    val = entF.get()
    print(u.is_pos_int(val))
        

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
title = ctk.CTkLabel(master=frame, text="Progetto di compressione delle immagini", font = ("Robot", 24))
title.pack(padx = 10)
### button for importing image
image_loaded = False
btnImage = ctk.CTkButton(frame, text="Carica immagine", command=load_image)
btnImage.pack(pady = 50)
### image
image_label = ctk.CTkLabel(frame, text="")
image_label.pack(pady = 15)
### F parameter
lbF = ctk.CTkLabel(master=frame, text="Parametro F")
lbF.pack(padx = 10)
### Entry
entF = ctk.CTkEntry(frame, placeholder_text="Parametro F")
entF.pack(padx = 10, pady = 3)
### d parameter
lbD = ctk.CTkLabel(master=frame, text="Parametro d")
lbD.pack(padx = 10,)
### Entry
entD = ctk.CTkEntry(frame, placeholder_text="Parametro d")
entD.pack(padx = 10, pady = 3)

### Calculate button

btnCom = ctk.CTkButton(frame, text="Calcola", command=calculate)
btnCom.pack(pady = 20)


### Reset button
btnCl = ctk.CTkButton(frame, text="Ripristina tutto", command=clear_all, fg_color="#df2c14", hover_color = "#c61a09")
btnCl.pack(pady = 20)

root.mainloop()
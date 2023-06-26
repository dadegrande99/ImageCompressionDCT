import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import utils as u
from image_processing import process_image


# Function for the interface
def load_image():
    # Caricamento di un'immagine
    global file_path, alpha, image
    file_path = filedialog.askopenfilename(
        filetypes=[("Bitmap Image", "*.bmp")])
    if file_path:
        image_label.destroy()
        image2_label.destroy()
        sv_img.destroy()
        image_zone()
        image = Image.open(file_path)
        alpha = u.find_alpha(
            (root.winfo_width(), root.winfo_height()), (image.width, image.height))
        photo = ctk.CTkImage(dark_image=image, size=(
            alpha*image.width, alpha*image.height))
        image_label.configure(image=photo)
        image_label.pack(side="left", pady=15, padx=15)
        btnImage.configure(text="Cambia immagine")
        # control_calculate()
        entF.focus_set()


def clear_all():
    # reset all interface
    btnImage.configure(text="Carica immagine")
    image_label.destroy()
    image2_label.destroy()
    sv_img.destroy()
    image_zone()
    entF.delete(0, "end")
    entD.delete(0, "end")
    lbR.configure(text="")
    frame.focus_set()


def control_calculate(event=""):
    # Controll if i can compress the image
    results = ""
    errors = 0

    # Controllo se è presente l'immagine
    if image_label.cget("image") is None:
        if errors > 0:
            results += "\n"
        errors += 1
        results += "Immagine assente"

    if not (u.is_pos_int(entF.get()) and u.is_pos_int(entD.get())):
        if not (u.is_pos_int(entF.get())):
            if errors > 0:
                results += "\n"
            errors += 1
            results += "Valore di F non valido o assente"
        if not (u.is_pos_int(entD.get())):
            if errors > 0:
                results += "\n"
            errors += 1
            results += "Valore di d non valido o assente"
    else:
        d = int(entD.get())
        F = int(entF.get())
        if F > 0 and F <= min(image.width, image.height):
            if d < 0 or d >= (2*F - 2):
                if errors > 0:
                    results += "\n"
                errors += 1
                results += "Il valore di d deve essere un intero compreso tra 0 e (2F - 2)"
        else:
            if errors > 0:
                results += "\n"
            errors += 1
            results += "Valore di F non valido"

    lbR.configure(text=results, text_color="red")
    return (errors == 0)


def calculate(event=""):
    # Compress the image
    global img2

    if control_calculate():
        lbR.configure(text="")
    else:
        return

    img2 = Image.fromarray(process_image(
        file_path, int(entF.get()), int(entD.get())))
    image_label.pack(anchor="nw", pady=15, padx=15)
    photo2 = ctk.CTkImage(dark_image=img2, size=(
        alpha*img2.width, alpha*img2.height))
    image2_label.configure(image=photo2)
    image2_label.pack(pady=15, padx=15)
    sv_img.pack(pady=15)


def save_image():
    # Save the compressed image
    fp = filedialog.asksaveasfilename(
        defaultextension=".jpeg", filetypes=[("JPEG Files", "*.jpeg")])
    if file_path:
        img2.save(fp)
        print("Immagine salvata con successo!")


def image_zone():
    # Creating image zone
    global image_label, image2_label, sv_img

    image_label = ctk.CTkLabel(frameIm, text="")
    image_label.pack(side="left", pady=15, padx=15)
    image2_label = ctk.CTkLabel(frameIm, text="")
    image2_label.pack(pady=15, padx=15)
    sv_img = ctk.CTkButton(frameIm, text="Salva immagine", command=save_image)


def passToD(event):
    entD.focus_set()


def passToF(event):
    entF.focus_set()


# Creating interface

# interface style
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# main window
root = ctk.CTk()
root.geometry("1000x1000")
root.minsize(1000, 1000)
root.maxsize(1000, 1000)

root.title("Progetto di compressione delle immagini")

# frame of the interface
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
# Project title
title = ctk.CTkLabel(
    master=frame, text="Progetto di compressione delle immagini", font=("Roboto", 24))
title.pack(pady=5, padx=10)

# button for importing image
image_loaded = False
btnImage = ctk.CTkButton(frame, text="Carica immagine", command=load_image)
btnImage.pack(pady=20)

# images
frameIm = ctk.CTkFrame(master=frame)
frameIm.pack(pady=10, padx=15)
image_zone()

# F parameter
lbF = ctk.CTkLabel(master=frame, text="Parametro F")
lbF.pack(padx=10)
# Entry
entF = ctk.CTkEntry(frame, placeholder_text="Parametro F")
entF.pack(padx=10, pady=3)

# d parameter
lbD = ctk.CTkLabel(master=frame, text="Parametro d")
lbD.pack(padx=10)
# Entry
entD = ctk.CTkEntry(frame, placeholder_text="Parametro d")
entD.pack(padx=10, pady=3)

# Reset button
btnCl = ctk.CTkButton(frame, text="Ripristina tutto",
                      command=clear_all, fg_color="#df2c14", hover_color="#c61a09")
btnCl.pack(pady=20)

# Calculate button
btnCom = ctk.CTkButton(frame, text="Calcola", command=calculate)
btnCom.pack(pady=20)

# Result paragraph
lbR = ctk.CTkLabel(master=frame, text="")
lbR.pack(padx=10)

# Events handling
entF.bind("<Return>", passToD)
entF.bind("<Tab>", passToD)
# entF.bind("<Key>", control_calculate)
entD.bind("<Tab>", passToF)
# entD.bind("<Key>", control_calculate)
entD.bind("<Return>", calculate)

root.mainloop()

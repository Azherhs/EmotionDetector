from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
from deepface import DeepFace
from tabulate import tabulate
from tkinter.messagebox import showinfo
from pprint import pformat

image_path = ""

def set_image():
    if path_field.get() == '':
        showinfo(title='Error message', message="Path is empty. Please, enter file's path")
    else:
        img = Image.open(path_field.get())
        img = img.resize((350, 400))
        img = ImageTk.PhotoImage(img)
        panel = Label(root, image=img)
        panel.image = img
        panel.grid(row=3, column=3)

def start_analyse():
    image_path = path_field.get()
    obj = DeepFace.analyze(img_path=image_path)
    emotion_dict = {}
    output = 'Emotion: '
    for key in obj:
        if key == 'dominant_emotion':
            output += obj[key]
        elif key == 'emotion':
            emotion_dict = obj[key]
    em_out = output + '\n'
    for i in emotion_dict:
        em_out += i + ': ' + str(emotion_dict[i]) + '\n'
    ttk.Label(root, text=em_out).grid(row=3, column=2)

root = Tk()
root.geometry("1100x600")
root.option_add('*Font', 'Arial 12')
root.title("EmotionDetector")
root.resizable(False, False)

b1 = ttk.Label(text='       ')
b1.grid(row=0, column=0)
b2 = ttk.Label(text='       ')
b2.grid(row=1, column=0)

open_file_btn = ttk.Button(root, text='Open image', command=set_image)
open_file_btn.grid(row=1, column=1)
start_analyse_btn = ttk.Button(root, text='Analyse image', command=start_analyse)
start_analyse_btn.grid(row=2, column=1)
path_field = ttk.Entry(width=50)
path_field.grid(row=1, column=2)
root.mainloop()

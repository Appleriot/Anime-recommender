import csv
import random
import tkinter as tk
import time

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = Tk()
window.geometry('600x600')
window.title("Anime recommecation")
window.config(padx=10, pady=10, bg='white')

f = Frame(window)

xscrollbar = Scrollbar(f, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=N+S+E+W)

yscrollbar = Scrollbar(f)
yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)

text = Text(f, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.grid(row=0, column=0)

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)

title_label = Label(window, text="You ever just look at anime and want more?")
title_label.config(font=("Lobster", 34, ),fg='black', cursor="target")
title_label.pack(padx=10, pady=10)

filename = 'anime.csv'
with open(filename, encoding="utf8") as f:
    reader = csv.reader(f)
    base = {'all':[]}

    for row in reader:
        name = row[1]
        score = row[3]
        tag = row[2]
        neck  = name, score, tag

        base['all'].append(neck)

filenae_manga = 'top.csv'
with open(filenae_manga, encoding="utf8") as f2:
    reader2 = csv.reader(f2)
    base2 = {'all': []}

    for row2 in reader2:
        name2 = row2[2]
        socre = row2[9]
        gerne = row2[-1]
        whole = name2, socre, gerne

        base2['all'].append(whole)

filename_webtoon = 'Webtoon.csv'
with open(filename_webtoon, encoding="utf8") as f3:
    reader3 = csv.reader(f3)
    base3 = {'all':[]}

    for row4 in reader3:
        name3 = row4[1]
        score2 = row4[3]
        link = row4[-1]
        bottom  = name3, score2, link

        base3['all'].append(bottom)

good_ansewer = []
bad_answers = []
allls = []

for ans in base['all']:
    good_ansewer.append(ans)
for answer in base2['all']:
    bad_answers.append(answer)
for alls in base3['all']:
    allls.append(alls)

anime = Label(window, text=f'You should check out {random.choice(good_ansewer)}. You might like it!', cursor="target", fg="red",  wraplength=1200)
anime.config(font=('Arial', 12))
anime.pack(padx=10, pady=10)

def manga():
    anime.destroy()
    mangas = Label(window, text=f'You should check out {random.choice(bad_answers)}. You might like it!',
        wraplength=1200, justify="center", fg="red").place(x=0, y=100)
    
def webtoon():
    anime.destroy()
    webtoons = Label(window, text=f'You should check out {random.choice(allls)}. You might like it!',
            wraplength=1200, justify="center", fg="red").place(x=0, y=100)

random_manga = Button(text="New Manga", command=manga)
random_manga.pack()

random_webtoon = Button(text='New Webtoon', command=webtoon)
random_webtoon.pack()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo, cursor="target")
    label.image = photo #avoid garbage collection

image = Image.open('te.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

window.mainloop()

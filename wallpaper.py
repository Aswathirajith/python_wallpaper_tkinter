from tkinter import *
from PIL import ImageTk,Image
import os

def next_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter= counter+1



counter=1
root = Tk()
root.title('wallpaper')
root.geometry('350x500')
root.config(background='black')

file=os.listdir('image')

img_array=[]
for file in file:
    img=Image.open(os.path.join('image',file))
    resized_img=img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root,image=img_array[0])
img_label.pack(pady=(10,20))

next_btn=Button(root,text='Next',bg='white',fg='black', width=25,height=2,command=next_img)
next_btn.pack(pady=(5,5))
root.mainloop()

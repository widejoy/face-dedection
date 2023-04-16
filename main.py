import face_recognition
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageDraw
image_1 = face_recognition.load_image_file(string)

win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
   global entry
   global string
   string= entry.get()
   

   
label=Label(win, text="enter location of the image", font=("Courier 22 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)


win.mainloop()
image_1_loc = face_recognition.face_locations(image_1)
image_1_pil = Image.fromarray(image_1)
for i in range(0,len(image_1_loc)):

 top = image_1_loc[i][0]
 right = image_1_loc[i][1]
 bottom = image_1_loc[i][2]
 left = image_1_loc[i][3]

 draw = ImageDraw.Draw(image_1_pil)
 draw.rectangle((left,top,right,bottom),outline=(250,7,0))
b = str(len(image_1_loc))
a = "The total no of Faces are "+ b +" and they are"
print(a)

root = Tk()
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text=a).grid(column=0, row=0)
root.mainloop()

image_1_pil.show()
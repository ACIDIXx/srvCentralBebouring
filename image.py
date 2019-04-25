#!/usr/bin/python 
from PIL import Image
from PIL import ImageTk
import Tkinter 

 
def update_image():
        global tkimg1
        tkimg1 = ImageTk.PhotoImage(Image.open('jjh\frame.jpg'))
        label.config( image = tkimg1)
        label.after(240, update_image)
        print "Updated"
 
 
 
w = Tkinter.Tk()
im = Image.open('jjh\frame.jpg')
tkimg1 = ImageTk.PhotoImage(im)
label =  Tkinter.Label(w, image=tkimg1)
print "Loaded"
label.pack()
w.after(240, update_image)
w.mainloop()
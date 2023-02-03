from tkinter import * 
import tkinter as tk
import example


root = Tk()
root.geometry("200x200")
#image2 =Image.open(r'C:\Users\sanje\Pictures\ben-sweet-2LowviVHZ-E-unsplash-1.jpeg')
image1 = tk.PhotoImage(file = r'C:\Users\sanje\Pictures\Figure_2.png')
#image1 = ImageTk.PhotoImage(image2)

def click_event():
    example.eye_gaze()
    
label1 = Label( root, image = image1)
label1.place(x = 0, y = 0)

mybutton = Button(root, text ='Start Video', padx = 50, fg="red", command= click_event)
mybutton.pack(pady=70)

root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

image = Image.open(r"C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")
image = image.resize((100, 100), Image.ANTIALIAS)

tk_image = ImageTk.PhotoImage(image)

image_label = tk.Label(window, image=tk_image)
image_label.pack()

window.mainloop()
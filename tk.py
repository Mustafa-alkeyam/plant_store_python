from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):


	

		
	
	 
	def __init__(self, *args, **kwargs): 
		
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		
		self.frames = {} 

		
		for F in (Home, Page1, Page2, Page3, Page4):

			frame = F(container, self)

			
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(Home)

	
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()



class Home(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		
		label = ttk.Label(self, text ="Home", font = LARGEFONT)
		
		
		label.grid(row = 0, column = 1, columnspan=4 , padx = 10, pady = 10) 

		button1 = ttk.Button(self, text ="Menu ",
		command = lambda : controller.show_frame(Page1))
	
		
		button1.grid(row = 1, column = 1, padx = 130, pady = 50)

		
		button2 = ttk.Button(self, text ="Shopping cart ",
		command = lambda : controller.show_frame(Page2))
	
		
		button2.grid(row = 1, column = 2, padx = 130, pady = 50)

		button3 = ttk.Button(self, text ="About ",
							command = lambda : controller.show_frame(Page3))
	
		
		button3.grid(row = 1, column = 3, padx = 130, pady = 50)

		button4 = ttk.Button(self, text ="Contact ",
							command = lambda : controller.show_frame(Page4))
	
		
		button4.grid(row = 1, column = 4, padx = 130, pady = 50)

		


 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Menu", font = LARGEFONT)
		label.grid(row = 0, column = 1, columnspan=4 , padx = 10, pady = 10)

		def load_and_resize_image(image_path, width, height):
				original_image = Image.open(image_path)
				resized_image = original_image.resize((width, height), Image.ANTIALIAS)
				return ImageTk.PhotoImage(resized_image)

		product_image1 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label1 = ttk.Label(self, image=product_image1)
		image_label1.grid(row=2, column=1, padx=10, pady=10)
	
		description_label1 = ttk.Label(self, text="Product 1 Description")
		description_label1.grid(row=3, column=1, padx=10, pady=10)

		price_label1 = ttk.Label(self, text="$19.99")  # Update with actual price
		price_label1.grid(row=4, column=1, padx=10, pady=10)

		purchase_button1 = ttk.Button(self, text="Add To Cart", command=lambda: self.add_to_cart(controller))
		purchase_button1.grid(row=5, column=1, padx=10, pady=10)
		

			# Second product card
		product_image2 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label2 = ttk.Label(self, image=product_image2)
		image_label2.grid(row=2, column=2, padx=10, pady=10)

		description_label2 = ttk.Label(self, text="Product 2 Description")
		description_label2.grid(row=3, column=2, padx=10, pady=10)

		price_label2 = ttk.Label(self, text="$29.99")  # Update with actual price
		price_label2.grid(row=4, column=2, padx=10, pady=10)

		purchase_button2 = ttk.Button(self, text="Add To Cart", command=lambda: print("Button 2 clicked"))
		purchase_button2.grid(row=5, column=2, padx=10, pady=10)


		product_image2 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label2 = ttk.Label(self, image=product_image2)
		image_label2.grid(row=2, column=3, padx=10, pady=10)

		description_label2 = ttk.Label(self, text="Product 2 Description")
		description_label2.grid(row=3, column=3, padx=10, pady=10)

		price_label2 = ttk.Label(self, text="$29.99")  # Update with actual price
		price_label2.grid(row=4, column=3, padx=10, pady=10)

		purchase_button2 = ttk.Button(self, text="Add To Cart", command=lambda: print("Button 2 clicked"))
		purchase_button2.grid(row=5, column=3, padx=10, pady=10)


		product_image2 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label2 = ttk.Label(self, image=product_image2)
		image_label2.grid(row=2, column=4, padx=10, pady=10)

		description_label2 = ttk.Label(self, text="Product 2 Description")
		description_label2.grid(row=3, column=4, padx=10, pady=10)

		price_label2 = ttk.Label(self, text="$29.99")  # Update with actual price
		price_label2.grid(row=4, column=4, padx=10, pady=10)

		purchase_button2 = ttk.Button(self, text="Add To Cart", command=lambda: print("Button 2 clicked"))
		purchase_button2.grid(row=5, column=4, padx=10, pady=10)


		product_image2 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label2 = ttk.Label(self, image=product_image2)
		image_label2.grid(row=6, column=1, padx=10, pady=10)

		description_label2 = ttk.Label(self, text="Product 2 Description")
		description_label2.grid(row=7, column=1, padx=10, pady=10)

		price_label2 = ttk.Label(self, text="$29.99")  # Update with actual price
		price_label2.grid(row=8, column=1, padx=10, pady=10)

		purchase_button2 = ttk.Button(self, text="Add To Cart", command=lambda: print("Button 2 clicked"))
		purchase_button2.grid(row=9, column=1, padx=10, pady=10)


		product_image2 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label2 = ttk.Label(self, image=product_image2)
		image_label2.grid(row=6, column=2, padx=10, pady=10)

		description_label2 = ttk.Label(self, text="Product 2 Description")
		description_label2.grid(row=7, column=2, padx=10, pady=10)

		price_label2 = ttk.Label(self, text="$29.99")  # Update with actual price
		price_label2.grid(row=8, column=2, padx=10, pady=10)

		purchase_button2 = ttk.Button(self, text="Add To Cart", command=lambda: print("Button 2 clicked"))
		purchase_button2.grid(row=9, column=2, padx=10, pady=10)


		product_image2 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label2 = ttk.Label(self, image=product_image2)
		image_label2.grid(row=6, column=3, padx=10, pady=10)

		description_label2 = ttk.Label(self, text="Product 2 Description")
		description_label2.grid(row=7, column=3, padx=10, pady=10)

		price_label2 = ttk.Label(self, text="$29.99")  # Update with actual price
		price_label2.grid(row=8, column=3, padx=10, pady=10)

		purchase_button2 = ttk.Button(self, text="Add To Cart", command=lambda: print("Button 2 clicked"))
		purchase_button2.grid(row=9, column=3, padx=10, pady=10)


		product_image2 = PhotoImage(file="C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")  # Update with actual path
		image_label2 = ttk.Label(self, image=product_image2)
		image_label2.grid(row=6, column=4, padx=10, pady=10)

		description_label2 = ttk.Label(self, text="Product 2 Description")
		description_label2.grid(row=7, column=4, padx=10, pady=10)

		price_label2 = ttk.Label(self, text="$29.99")  # Update with actual price
		price_label2.grid(row=8, column=4, padx=10, pady=10)

		purchase_button2 = ttk.Button(self, text="Add To Cart", command=lambda: print("Button 2 clicked"))
		purchase_button2.grid(row=9, column=4, padx=10, pady=10)



			
		button1 = ttk.Button(self, text ="Home",
								command = lambda : controller.show_frame(Home))
		
		
		button1.grid(row = 1, column = 1, padx = 130, pady = 50)

		
		button2 = ttk.Button(self, text ="Shopping cart ",
							command = lambda : controller.show_frame(Page2))
	
		
		button2.grid(row = 1, column = 2, padx = 130, pady = 50)

		button3 = ttk.Button(self, text ="About ",
							command = lambda : controller.show_frame(Page3))
	
		
		button3.grid(row = 1, column = 3, padx = 130, pady = 50)

		button4 = ttk.Button(self, text ="Contact ",
							command = lambda : controller.show_frame(Page4))
	
		
		button4.grid(row = 1, column = 4, padx = 130, pady = 50)





class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Shopping cart ", font = LARGEFONT)
		label.grid(row = 0, column = 1, columnspan=4 , padx = 10, pady = 10)

		
		button1 = ttk.Button(self, text ="Menu ",
							command = lambda : controller.show_frame(Page1))
	
		
		button1.grid(row = 1, column = 1, padx = 130, pady = 50)

		
		button2 = ttk.Button(self, text ="Home",
							command = lambda : controller.show_frame(Home))
	
		
		button2.grid(row = 1, column = 2, padx = 130, pady = 50)

		button3 = ttk.Button(self, text ="About ",
							command = lambda : controller.show_frame(Page3))
	
		
		button3.grid(row = 1, column = 3, padx = 130, pady = 50)

		button4 = ttk.Button(self, text ="Contact ",
							command = lambda : controller.show_frame(Page4))
	
		
		button4.grid(row = 1, column = 4, padx = 130, pady = 50)
		


class Page3(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="About ", font = LARGEFONT)
		label.grid(row = 0, column = 1, columnspan=4 , padx = 10, pady = 10)

		
		button1 = ttk.Button(self, text ="Menu ",
							command = lambda : controller.show_frame(Page1))
	
		
		button1.grid(row = 1, column = 1, padx = 130, pady = 50)

		
		button2 = ttk.Button(self, text ="Home",
							command = lambda : controller.show_frame(Home))
	
		
		button2.grid(row = 1, column = 2, padx = 130, pady = 50)

		button3 = ttk.Button(self, text ="Shopping cart ",
							command = lambda : controller.show_frame(Page2))
	
		
		button3.grid(row = 1, column = 3, padx = 130, pady = 50)

		button4 = ttk.Button(self, text ="Contact ",
							command = lambda : controller.show_frame(Page4))
	
		
		button4.grid(row = 1, column = 4, padx = 130, pady = 50)
		


class Page4(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Contact ", font = LARGEFONT)
		label.grid(row = 0, column = 1, columnspan=4 , padx = 10, pady = 10)


		
		button1 = ttk.Button(self, text ="Menu ",
							command = lambda : controller.show_frame(Page1))
	
		
		button1.grid(row = 1, column = 1, padx = 130, pady = 50)

		
		button2 = ttk.Button(self, text ="Home",
							command = lambda : controller.show_frame(Home))
	
		
		button2.grid(row = 1, column = 2, padx = 130, pady = 50)

		button3 = ttk.Button(self, text ="Shopping cart ",
							command = lambda : controller.show_frame(Page2))
	
		
		button3.grid(row = 1, column = 3, padx = 130, pady = 50)

		button4 = ttk.Button(self, text ="About ",
							command = lambda : controller.show_frame(Page3))
	
		
		button4.grid(row = 1, column = 4, padx = 130, pady = 50)



			# Form for Name
		name_label = ttk.Label(self, text="Name:")
		name_label.grid(row=2, column=0, columnspan=4 , padx=10, pady=50)
		name_entry = ttk.Entry(self)
		name_entry.grid(row=2, column=1, columnspan=4, padx=10, pady=10)

			# Form for Phone Number
		phone_label = ttk.Label(self, text="Phone Number:")
		phone_label.grid(row=3,  column=0, columnspan=4 , padx=10, pady=50)
		phone_entry = ttk.Entry(self)
		phone_entry.grid(row=3,  column=1, columnspan=4 , padx=10, pady=10)

			# Form for Email
		email_label = ttk.Label(self, text="Email:")
		email_label.grid(row=4,  column=0, columnspan=4 , padx=10, pady=50)
		email_entry = ttk.Entry(self)
		email_entry.grid(row=4,  column=1, columnspan=4 , padx=10, pady=10)

			# Form for Address
		address_label = ttk.Label(self, text="Address:")
		address_label.grid(row=5,  column=0, columnspan=4 , padx=10, pady=50)
		address_entry = ttk.Entry(self)
		address_entry.grid(row=5,  column=1, columnspan=4 , padx=10, pady=10)

		
		



app = tkinterApp()
app.mainloop()




# import tkinter as tk
# from PIL import Image, ImageTk

# window = tk.Tk()

# image = Image.open(r"C:\\Users\\Yahya Qeyam\\Desktop\\shopp.png")
# image = image.resize((100, 100), Image.ANTIALIAS)

# tk_image = ImageTk.PhotoImage(image)

# image_label = tk.Label(window, image=tk_image)
# image_label.pack()

# window.mainloop()
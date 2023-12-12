from tkinter import *
import tkinter as tk
from tkinter import ttk


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

		
		



app = tkinterApp()
app.mainloop()

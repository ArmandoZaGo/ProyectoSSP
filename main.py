from tkinter import *

class LogIn():
	def __init__(self):
		self.Raiz = Tk()
		self.Raiz.title("INICIO DE SESION")
		self.Raiz.iconbitmap("login.ico")
		self.Frame = Frame(self.Raiz, width=900, height=600)
		self.Frame.pack()
		self.Entrada = Label(self.Frame, text="Bienvenido!!", font=("Times New Roman",40)).place(x=150,y=60)
		self.Correo = Label(self.Frame, text="Correo:", font=("Times New Roman",25)).place(x=80,y=230)
		self.CorreoE = Entry(self.Frame, font=("Times New Roman",14)).place(width=300,height=30,x=80,y=300)
		self.Contra = Label(self.Frame, text="Contraseña:", font=("Times New Roman",25)).place(x=80,y=380)
		self.ContraE = Entry(self.Frame, font=("Times New Roman",14)).place(width=300,height=30,x=80,y=450)
		self.Linea = Canvas(width=10,height=550,bg="blue").place(x=600,y=20)
		self.Raiz.mainloop()

app = LogIn()
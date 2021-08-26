from tkinter import *

class LogIn():
	def __init__(self):
		self.Raiz = Tk()
		self.Raiz.title("INICIO DE SESION")
		self.Raiz.iconbitmap("login.ico")
		self.Raiz.geometry("900x600+220+50")
		self.Raiz.resizable(0,0)
		self.Frame = Frame(self.Raiz, width=900, height=600)
		self.Frame.pack()
		self.Entrada = Label(self.Frame, text="Bienvenido!!", font=("Times New Roman",40)).place(x=150,y=60)
		self.Correo = Label(self.Frame, text="Correo:", font=("Times New Roman",25)).place(x=80,y=210)
		self.CorreoE = Entry(self.Frame, font=("Times New Roman",14)).place(width=300,height=30,x=80,y=280)
		self.Contra = Label(self.Frame, text="Contraseña:", font=("Times New Roman",25)).place(x=80,y=360)
		self.ContraE = Entry(self.Frame,show="*",font=20).place(width=300,height=30,x=80,y=430)
		self.RegistroL = Label(self.Frame, text="No tienes una cuenta aun?",font=("Times New Roman",14)).place(x=80,y=490)
		self.RegistroB = Button(self.Frame, text="Registrarse", font=("Times New Roman",12)).place(x=290,y=485)
		self.Linea = Canvas(width=10,height=550,bg="blue").place(x=600,y=20)
		self.Raiz.mainloop()

app = LogIn()
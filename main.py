from tkinter import *
import pandas as pd


class LogIn():
	def __init__(self):
		self.Raiz = Tk()
		self.Raiz.title("INICIO DE SESION")
		self.Raiz.iconbitmap("login.ico")
		self.x = self.Raiz.winfo_screenwidth()
		self.y = self.Raiz.winfo_screenheight()
		self.Raiz.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.Raiz.resizable(0,0)
		self.Frame = Frame(self.Raiz, width=900, height=600)
		self.Frame.pack()
		self.Entrada = Label(self.Frame, text="Bienvenido!!", font=("Times New Roman",40)).place(x=150,y=60)
		self.Correo = Label(self.Frame, text="Correo:", font=("Times New Roman",25)).place(x=80,y=210)
		self.CorreoE = Entry(self.Frame, font=("Times New Roman",14)).place(width=300,height=30,x=80,y=280)
		self.Contra = Label(self.Frame, text="Contraseña:", font=("Times New Roman",25)).place(x=80,y=360)
		self.ContraE = Entry(self.Frame,show="*",font=20).place(width=300,height=30,x=80,y=430)
		self.RegistroL = Label(self.Frame, text="No tienes una cuenta aun?",font=("Times New Roman",14)).place(x=80,y=490)
		self.RegistroB = Button(self.Frame, text="Registrarse", command=self.OpReg, font=("Times New Roman",12)).place(x=290,y=485)
		self.Linea = Canvas(width=10,height=550,bg="blue").place(x=600,y=20)
		self.Raiz.mainloop()

	def OpReg(self):
		self.Raiz.destroy()
		Open = Registro()

class Registro():
	def __init__(self):
		self.Raiz = Tk()
		self.Raiz.title("REGISTRO DE USUARIO")
		self.Raiz.iconbitmap("login.ico")
		self.x = self.Raiz.winfo_screenwidth()
		self.y = self.Raiz.winfo_screenheight()
		self.Raiz.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.Raiz.resizable(0,0)
		self.FrameR = Frame(self.Raiz, width=900, height=600)
		self.FrameR.pack()
		self.TextNE = StringVar()
		self.TextAE = StringVar()
		self.TextEE =  StringVar()
		self.TextSE = StringVar()
		self.TextCE = StringVar()
		self.TextDE = StringVar()
		self.TextCrE = StringVar()
		self.TextPE = StringVar()
		self.TextRe =  Label(self.FrameR, text="USUARIO",font=("Times New Roman",45)).place(x=300,y=60)
		self.Nombre = Label(self.FrameR, text="Nombre:", font=("Times New Roman",18)).place(x=100,y=160)
		self.NombreE = Entry(self.FrameR, textvariable=self.TextNE, font=("Times New Roman",14)).place(width=300,height=30,x=105,y=200)
		self.Apellido = Label(self.FrameR, text="Apellido:", font=("Times New Roman",18)).place(x=100,y=240)
		self.ApellidoE = Entry(self.FrameR, textvariable=self.TextAE, font=("Times New Roman",14)).place(width=300,height=30,x=105,y=280)
		self.Edad = Label(self.FrameR, text="Edad:", font=("Times New Roman",18)).place(x=100,y=320)
		self.EdadE = Entry(self.FrameR, textvariable=self.TextEE,font=("Times New Roman",14)).place(width=300,height=30,x=105,y=360)
		self.Sexo = Label(self.FrameR, text="Sexo:", font=("Times New Roman",18)).place(x=100,y=400)
		self.SexoE = Entry(self.FrameR, textvariable=self.TextSE,font=("Times New Roman",14)).place(width=300,height=30,x=105,y=440)
		self.Carrera = Label(self.FrameR, text="Carrera:", font=("Times New Roman",18)).place(x=500,y=160)
		self.CarreraE = Entry(self.FrameR, textvariable=self.TextCE,font=("Times New Roman",14)).place(width=300,height=30,x=505,y=200)
		self.Division = Label(self.FrameR, text="Division UG:", font=("Times New Roman",18)).place(x=500,y=240)
		self.DivsionE = Entry(self.FrameR, textvariable=self.TextDE,font=("Times New Roman",14)).place(width=300,height=30,x=505,y=280)
		self.Correo = Label(self.FrameR, text="Correo:", font=("Times New Roman",18)).place(x=500,y=320)
		self.CorreoE = Entry(self.FrameR, textvariable=self.TextCrE,font=("Times New Roman",14)).place(width=300,height=30,x=505,y=360)
		self.Password = Label(self.FrameR, text="Contraseña:", font=("Times New Roman",18)).place(x=500,y=400)
		self.PasswordE = Entry(self.FrameR, textvariable=self.TextPE,font=("Times New Roman",14)).place(width=300,height=30,x=505,y=440)
		self.BReg = Button(self.FrameR,text="Regresar",command=self.OpIni,font=("Times New Roman",15)).place(x=500,y=500)
		self.BEnv = Button(self.FrameR,text="Enviar", command=self.Ingreso,font=("Times New Roman",15)).place(x=600,y=500)
		self.Check = Label(self.FrameR)
		self.Raiz.mainloop()

	def OpIni(self):
		self.Raiz.destroy()
		Open = LogIn()

	def Ingreso(self):
		Texto_Nombre = self.TextNE.get()
		Texto_Apellido = self.TextAE.get()
		Texto_Edad = self.TextEE.get()
		Texto_Sexo = self.TextSE.get()
		Texto_Carrera = self.TextCE.get()
		Texto_Division = self.TextDE.get()
		Texto_Correo = self.TextCrE.get()
		Texto_Password = self.TextPE.get()
		
		file = open("DatosUsuario.csv","a")
		file.write(Texto_Nombre + ",")
		file.write(Texto_Apellido + ",")
		file.write(Texto_Edad + ",")
		file.write(Texto_Sexo + ",")
		file.write(Texto_Carrera + ",")
		file.write(Texto_Division + ",")
		file.write(Texto_Correo + ",")
		file.write(Texto_Password + "\n")
		file.close()

		self.Check.config(text="Registro realizado correctamente!",font=("Times New Roman",15),bg="green2")
		self.Check.place(x=120,y=500)

		self.Check.after(5000,self.OpIni)

class PanelAd():
	def __init__(self):
		self.Raiz = Tk()
		self.Raiz.title("ADMINISTRADOR")
		self.Raiz.iconbitmap("login.ico")
		self.x = self.Raiz.winfo_screenwidth()
		self.y = self.Raiz.winfo_screenheight()
		self.Raiz.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.Raiz.resizable(0,0)
		self.Frame = Frame(self.Raiz, width=900, height=600)
		self.Frame.pack()
		self.Titulo = Label(self.Frame, text="Panel de Administrador", font=("Times New Roman",45)).place(x=170,y=50)
		self.Raiz.mainloop()


#app = LogIn()
app = PanelAd()
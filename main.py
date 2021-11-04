from tkinter import *
from tkinter import ttk, filedialog
from os import remove
import pandas as pd


class LogIn():
	def __init__(self):
		self.IniSe = Tk()
		self.IniSe.title("INICIO DE SESION")
		self.IniSe.iconbitmap("login.ico")
		self.x = self.IniSe.winfo_screenwidth()
		self.y = self.IniSe.winfo_screenheight()
		self.IniSe.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.IniSe.resizable(0,0)
		self.Frame = Frame(self.IniSe, width=900, height=600)
		self.Frame.pack()
		self.EAdress = StringVar()
		self.Password = StringVar()
		self.Entrada = Label(self.Frame, text="Bienvenido!!", font=("Times New Roman",40)).place(x=150,y=60)
		self.Correo = Label(self.Frame, text="Correo:", font=("Times New Roman",25)).place(x=80,y=210)
		self.CorreoE = Entry(self.Frame, textvariable=self.EAdress, font=("Times New Roman",14))
		self.CorreoE.place(width=300,height=30,x=80,y=280)
		self.Contra = Label(self.Frame, text="Contraseña:", font=("Times New Roman",25)).place(x=80,y=340)
		self.ContraE = Entry(self.Frame, textvariable=self.Password,show="*",font=20)
		self.ContraE.place(width=300,height=30,x=80,y=390)
		self.RegistroL = Label(self.Frame, text="No tienes una cuenta aun?",font=("Times New Roman",14)).place(x=80,y=490)
		self.RegistroB = Button(self.Frame, text="Registrarse", command=self.OpReg, font=("Times New Roman",12)).place(x=290,y=485)
		self.Enviar = Button(self.Frame, text="Enviar", command=self.Check, font=("Times New Roman",14)).place(x=90,y=430)
		self.Reintentar = Button(self.Frame, text="Reintentar", command=self.Clave, font=("Times New Roman",14)).place(x=160,y=430)
		self.Linea = Canvas(width=10,height=550,bg="blue").place(x=600,y=20)
		self.AdvertenciaC = Label(self.Frame)
		self.AdvertenciaP = Label(self.Frame)
		self.IniSe.mainloop()

	def OpReg(self):
		self.Raiz.destroy()
		Open = Registro()

	def Check(self):
		Correo = self.EAdress.get()
		Pass = self.Password.get()
		Lista_Correo = []
		Lista_Password = []
		df = pd.read_csv("DatosUsuario.csv")

		for i in range(len(df.index)):
			Lista_Correo.append(df.Correo[i])
			Lista_Password.append(df.Password[i])

		if Correo in Lista_Correo:
			if Pass in Lista_Password:
				self.IniSe.destroy()
				Pantalla = Pantalla_1()
			else:
				self.AdvertenciaL(2)
		else:
			self.AdvertenciaL(1)

	def Clave(self):
		self.AdvertenciaL(3)

	def AdvertenciaL(self,Clave):
		if Clave == 1:
			self.AdvertenciaC.config(text="Correo no encontrado. Intente de nuevo o registrese", font=("Times New Roman",15), bg="red")
			self.AdvertenciaC.place(x=80,y=540)
		elif Clave == 2:
			self.AdvertenciaP.config(text="Contraseña no encontrada. Intente de nuevo o registrese", font=("Times New Roman",15), bg="red")
			self.AdvertenciaP.place(x=80,y=540)
		else:
			self.AdvertenciaC.destroy()
			self.AdvertenciaP.destroy()
			self.CorreoE.delete(0,END)
			self.ContraE.delete(0,END)

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
		self.var = StringVar(self.FrameR)
		self.Opciones = ["Campus Guanajato","Campus Irapuato-Salamanca","Campus Celaya-Salvatierra","Campus León","Colegio Nivel Medio Superior"]
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
		self.DivsionE = OptionMenu(self.FrameR, self.var, *self.Opciones)
		self.DivsionE.place(x=505,y=280)
		self.DivsionE.config(width=26, font=("Times New Roman",15))
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
		Campus = self.var.get()
		Texto_Nombre = self.TextNE.get()
		Texto_Apellido = self.TextAE.get()
		Texto_Edad = self.TextEE.get()
		Texto_Sexo = self.TextSE.get()
		Texto_Carrera = self.TextCE.get()
		Texto_Correo = self.TextCrE.get()
		Texto_Password = self.TextPE.get()
		
		file = open("DatosUsuario.csv","a")
		file.write(Texto_Nombre + ",")
		file.write(Texto_Apellido + ",")
		file.write(Texto_Edad + ",")
		file.write(Texto_Sexo + ",")
		file.write(Texto_Carrera + ",")
		file.write(Campus + ",")
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
		self.Pt1 = StringVar()
		self.Pt2 = StringVar()
		self.Pt3 = StringVar()
		self.Pt4 = StringVar() 
		self.Titulo = Label(self.Frame, text="Panel de Administrador", font=("Times New Roman",45)).place(x=170,y=50)
		self.TP_1 = Label(self.Frame, text="¿Cuántas veces se mostrará la Pantalla 1?", font=("Times New Roman",20)).place(x=20,y=170)
		self.TP_1_E = Entry(self.Frame, textvariable=self.Pt1, font=("Times New Roman",15)).place(width=200,height=30,x=500,y=175)
		self.TP_2 = Label(self.Frame, text="¿Cuántas veces se mostrará la Pantalla 2?", font=("Times New Roman",20)).place(x=20,y=230)
		self.TP_2_E = Entry(self.Frame, textvariable=self.Pt2, font=("Times New Roman",15)).place(width=200,height=30,x=500,y=235)
		self.TP_3 = Label(self.Frame, text="¿Cuántas veces se mostrará la Pantalla 3?", font=("Times New Roman",20)).place(x=20,y=290)
		self.TP_3_E = Entry(self.Frame, textvariable=self.Pt3, font=("Times New Roman",15)).place(width=200,height=30,x=500,y=295)
		self.TP_4 = Label(self.Frame, text="¿Cuántas veces se mostrará la Pantalla 4?", font=("Times New Roman",20)).place(x=20,y=350)
		self.TP_4_E = Entry(self.Frame, textvariable=self.Pt4, font=("Times New Roman",15)).place(width=200,height=30,x=500,y=355)
		self.C_T = Label(self.Frame, text="Seleccionar Carpeta de Imagenes", font=("Times New Roman",20)).place(x=20,y=410)
		self.C_S = Button(self.Frame, text="Examinar", command=self.Sel_Carpeta, font=("Times New Roman",15)).place(x=400,y=410)
		self.BReg =  Button(self.Frame, text="Regresar", font=("Times New Roman",15)).place(x=300,y=500)
		self.GCamb = Button(self.Frame, text="Guardar Cambios", command=self.GCambios, font=("Times New Roman",15)).place(x=400,y=500)
		self.Raiz.mainloop()
	
	def Sel_Carpeta(self):
		remove("DatosAdmin.csv")
		folder = filedialog.askdirectory()
		file = open("DatosAdmin.csv","a")
		file.write(folder + ",")
		file.close()	
	
	def GCambios(self):
		Pantalla_1 = self.Pt1.get()
		Pantalla_2 = self.Pt2.get()
		Pantalla_3 = self.Pt3.get()
		Pantalla_4 = self.Pt4.get()
		file = open("DatosAdmin.csv","a")
		file.write(Pantalla_1 + ",")
		file.write(Pantalla_2 + ",")
		file.write(Pantalla_3 + ",")
		file.write(Pantalla_4 + "\n")
		file.close()	

class Pantalla_1():
	def __init__(self):
		self.P1 = Tk()
		self.P1.title("PANTALLA 1")
		self.P1.iconbitmap("login.ico")
		self.x = self.P1.winfo_screenwidth()
		self.y = self.P1.winfo_screenheight()
		self.P1.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.P1.resizable(0,0)
		self.Frame = Frame(self.P1, width=900, height=600)
		self.Frame.pack()
		self.Img_1_G = PhotoImage(file="Comida/Agua.png")
		self.Img_1 = Button(self.Frame, image=self.Img_1_G).place(x=100,y=150)
		self.P1.mainloop()


#app = LogIn()
#app = Registro()
#app = PanelAd()
app = Pantalla_1()
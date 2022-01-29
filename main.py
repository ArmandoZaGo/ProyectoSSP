from tkinter import *
from tkinter import ttk, filedialog
from os import remove
import pandas as pd
from PIL import Image, ImageTk
import random
import datetime
import re

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
		self.Admin = Button(self.Frame, text="Administrador", command=self.Admin_Check, font=("Times New Roman",14)).place(x=260,y=430)
		self.Linea = Canvas(width=10,height=550,bg="blue").place(x=600,y=20)
		self.AdvertenciaC = Label(self.Frame)
		self.AdvertenciaP = Label(self.Frame)
		self.IniSe.mainloop()

	def OpReg(self):
		self.IniSe.destroy()
		Open = Registro()
	
	def Admin_Check(self):
		self.IniSe.destroy()

		Correo = self.EAdress.get()
		Pass = self.Password.get()
		if Correo == "admin":
			if Pass == "admin":
				app = PanelAd()


	def Check(self):
		date = datetime.datetime.now()
		Valor = date.strftime('%d/%m/%Y,%H:%M:%S')

		archivo = open("Historial.csv","a")
		archivo.write("\n")
		archivo.write(Valor + ",")
		archivo.close()

		df = pd.read_csv("DatosAdmin.csv")
		i = int(df.Pantalla_1[0])
		j = int(df.Pantalla_2[0])

		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(df.Carpeta[0] + ",")
		file.write(str(i) + ",")
		file.write(str(j) + "\n")
		file.close()

		Correo = self.EAdress.get()
		Pass = self.Password.get()
		print(Correo)
		print(Pass)
		Lista_Correo = []
		Lista_Password = []
		df = pd.read_csv("DatosUsuario.csv")

		for i in range(len(df.index)):
			if Correo == str(df.Correo[i]):
				k = i
			else:
				k = 0

		for i in range(len(df.index)):
			Lista_Correo.append(df.Correo[i])
			Lista_Password.append(df.Password[i])
			print(Lista_Password[i])

		for i in range(len(Lista_Correo)):
			if str(Correo) == Lista_Correo[i]:
				if str(Pass) == str(Lista_Password[i]):
					self.IniSe.destroy()
					archivo = open("Historial.csv","a")
					archivo.write(df.Nombre[k] + ",")
					archivo.write(df.Apellidos[k] + ",")
					archivo.write(df.Correo[k])
					archivo.close()
					app = Call_Func().Call()
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
			self.IniSe.destroy()
			pp = LogIn()

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
		self.var = StringVar(self.Frame)
		self.Opciones = ["Comida"]
		self.Titulo = Label(self.Frame, text="Panel de Administrador", font=("Times New Roman",45)).place(x=170,y=50)
		self.TP_1 = Label(self.Frame, text="¿Cuántas veces se mostrará la Pantalla 1?", font=("Times New Roman",20)).place(x=20,y=170)
		self.TP_1_E = Entry(self.Frame, textvariable=self.Pt1, font=("Times New Roman",15)).place(width=200,height=30,x=500,y=175)
		self.TP_2 = Label(self.Frame, text="¿Cuántas veces se mostrará la Pantalla 2?", font=("Times New Roman",20)).place(x=20,y=240)
		self.TP_2_E = Entry(self.Frame, textvariable=self.Pt2, font=("Times New Roman",15)).place(width=200,height=30,x=500,y=245)
		self.TP_4 = Label(self.Frame, text="Preguntas (Pantalla 3)", font=("Times New Roman",20)).place(x=230,y=310)
		self.TP_4_E = Entry(self.Frame, textvariable=self.Pt3, font=("Times New Roman",15)).place(width=200,height=30,x=500,y=315)
		self.Inst = Label(self.Frame, text="Ingrese cada una de las preguntas a evaluar en el siguiente", font=("Times New Roman",10), bg="yellow").place(x=155,y=350)
		self.Inst_2 = Label(self.Frame, text="recuadro separando por espacios en blanco cada una de ellas", font=("Times New Roman",10), bg="yellow").place(x=142,y=370)
		self.C_T = Label(self.Frame, text="Seleccionar Carpeta de Imagenes", font=("Times New Roman",20)).place(x=20,y=420)
		self.C_S = OptionMenu(self.Frame, self.var, *self.Opciones)
		self.C_S.place(x=390,y=420)
		self.C_S.config(font=("Times New Roman",15))
		self.BReg =  Button(self.Frame, text="Regresar", command=self.Return,  font=("Times New Roman",15)).place(x=300,y=500)
		self.GCamb = Button(self.Frame, text="Guardar Cambios", command=self.GCambios, font=("Times New Roman",15)).place(x=400,y=500)
		self.Raiz.mainloop()	
	
	def GCambios(self):
		remove("DatosAdmin.csv")
		Carpeta = self.var.get()
		Pantalla_1 = self.Pt1.get()
		Pantalla_2 = self.Pt2.get()
		Pantalla_3 = self.Pt3.get()
		print(Pantalla_3)
		Lista_p3 = re.split(",",Pantalla_3)
		file = open("DatosAdmin.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(Pantalla_1 + ",")
		file.write(Pantalla_2 + "\n")
		file.close()

		remove("Preguntas_P3.csv")
		for i in range(len(Lista_p3)):
			if i == len(Lista_p3)-1:
				file = open("Preguntas_P3.csv","a")
				file.write("Pregunta" + str(i+1))
				file.close()
			else:
				file = open("Preguntas_P3.csv","a")
				file.write("Pregunta" + str(i+1) + ",")
				file.close()
		file = open("Preguntas_P3.csv","a")
		file.write("\n")
		file.close()

		for i in range(len(Lista_p3)):
			if i == len(Lista_p3)-1:
				file = open("Preguntas_P3.csv","a")
				file.write(Lista_p3[i])
				file.close()
			else:
				file = open("Preguntas_P3.csv","a")
				file.write(Lista_p3[i] + ",")
				file.close()
		file = open("Preguntas_P3.csv","a")
		file.write("\n")
		file.close()

		remove("NumPe.csv")
		if Pantalla_3 == "":
			file = open("NumPe.csv","a")
			file.write("Numero" + ",")
			file.write("\n" + "0" + ",")
			file.close()
		else:
			file = open("NumPe.csv","a")
			file.write("Numero" + ",")
			file.write("\n" + "1" + ",")
			file.close()
	
	def Return(self):
		self.Raiz.destroy()
		app = LogIn()

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
		self.B1 = Button(self.Frame, command=self.BT1)
		self.B2 = Button(self.Frame, command=self.BT2)
		self.B3 = Button(self.Frame, command=self.BT3)
		self.B4 = Button(self.Frame, command=self.BT4)
		self.BB = Button(self.Frame, command=self.Asign_Img, text="¿Qué eliges?", font=("Times New Roman",35)).place(x=100,y=30)
		self.P1.mainloop()

	def Asign_Img(self):
		df = pd.read_csv("Comida.csv")
		df_DA = pd.read_csv("DatosAdmin.csv")
		L = []
		for i in range(len(df)):
			i=i+1
			L.append(i)
			random.shuffle(L)

		esc = open("Auxi.csv","a")
		esc.write("Imagen1" + ",")
		esc.write("Imagen2" + ",")
		esc.write("Imagen3" + ",")
		esc.write("Imagen4" + "\n")
		esc.close()

		print(L)
		self.PImg1 = Image.open(df_DA.Carpeta[0] + "/" + str(L[0]) + ".png")
		self.Img1 = ImageTk.PhotoImage(self.PImg1)
		self.B1.config(image=self.Img1)
		self.B1.place(x=80,y=150)
		esc = open("Auxi.csv","a")
		esc.write(str(L[0]) + ",")
		esc.close()

		self.PImg2 = Image.open(df_DA.Carpeta[0] + "/" + str(L[1]) + ".png")
		self.Img2 = ImageTk.PhotoImage(self.PImg2)
		self.B2.config(image=self.Img2)
		self.B2.place(x=460,y=150)
		esc = open("Auxi.csv","a")
		esc.write(str(L[1]) + ",")
		esc.close()

		self.PImg3 = Image.open(df_DA.Carpeta[0] + "/" + str(L[2]) + ".png")
		self.Img3 = ImageTk.PhotoImage(self.PImg3)
		self.B3.config(image=self.Img3)
		self.B3.place(x=80,y=370)
		esc = open("Auxi.csv","a")
		esc.write(str(L[2]) + ",")
		esc.close()

		self.PImg4 = Image.open(df_DA.Carpeta[0] + "/" + str(L[3]) + ".png")
		self.Img4 = ImageTk.PhotoImage(self.PImg4)
		self.B4.config(image=self.Img4)
		self.B4.place(x=460,y=370)
		esc = open("Auxi.csv","a")
		esc.write(str(L[3]) + "\n")
		esc.close()

	def BT1(self):
		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen1[0])
		i -= 1
		de = pd.read_csv("Comida.csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de.Comida[i])
		new.close()

		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		i -= 1
		j = int(df.Pantalla_2[0])

		Carpeta = df.Carpeta[0]
		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(str(i) + ",")
		file.write(str(j) + "\n")
		file.close()

		remove("Auxi.csv")

		app = Call_Func()
		app.Call()
	
	def BT2(self):
		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen2[0])
		i -= 1
		de = pd.read_csv("Comida.csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de.Comida[i])
		new.close()

		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		i -= 1
		j = int(df.Pantalla_2[0])

		Carpeta = df.Carpeta[0]
		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(str(i) + ",")
		file.write(str(j) + "\n")
		file.close()

		remove("Auxi.csv")

		app = Call_Func()
		app.Call()

	def BT3(self):
		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen3[0])
		i -= 1
		de = pd.read_csv("Comida.csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de.Comida[i])
		new.close()

		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		i -= 1
		j = int(df.Pantalla_2[0])

		Carpeta = df.Carpeta[0]
		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(str(i) + ",")
		file.write(str(j) + "\n")
		file.close()

		remove("Auxi.csv")

		app = Call_Func()
		app.Call()

	def BT4(self):
		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen4[0])
		i -= 1
		de = pd.read_csv("Comida.csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de.Comida[i])
		new.close()

		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		i -= 1
		j = int(df.Pantalla_2[0])

		Carpeta = df.Carpeta[0]
		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(str(i) + ",")
		file.write(str(j) + "\n")
		file.close()

		remove("Auxi.csv")

		app = Call_Func()
		app.Call()

class Pantalla_2():
	def __init__(self):
		self.P2 = Tk()
		self.P2.title("PANTALLA 2")
		self.P2.iconbitmap("login.ico")
		self.x = self.P2.winfo_screenwidth()
		self.y = self.P2.winfo_screenheight()
		self.P2.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.P2.resizable(0,0)
		self.Frame = Frame(self.P2, width=900, height=600)
		self.Frame.pack()
		self.B1 = Button(self.Frame, command=self.BT1)
		self.B2 = Button(self.Frame, command=self.BT2)
		self.vs = Label(self.Frame, text="VS", font=("Times New Roman",40), bg="green").place(x=415,y=310)
		self.BB = Button(self.Frame, command=self.Asign_Img, text="De las siguientes opciones, ¿qué prefieres?", font=("Times New Roman",35)).place(x=28,y=30)
		self.P2.mainloop()
	
	def Asign_Img(self):
		df = pd.read_csv("Comida.csv")
		df_DA = pd.read_csv("DatosAdmin.csv")
		L = []
		for i in range(len(df)):
			i=i+1
			L.append(i)
			random.shuffle(L)

		esc = open("Auxi.csv","a")
		esc.write("Imagen1" + ",")
		esc.write("Imagen2" + "\n")
		esc.close()

		self.PImg1 = Image.open(df_DA.Carpeta[0] + "/" + str(L[0]) + ".png")
		self.Img1 = ImageTk.PhotoImage(self.PImg1)
		self.B1.config(image=self.Img1)
		self.B1.place(x=40,y=250)
		esc = open("Auxi.csv","a")
		esc.write(str(L[0]) + ",")
		esc.close()

		self.PImg2 = Image.open(df_DA.Carpeta[0] + "/" + str(L[1]) + ".png")
		self.Img2 = ImageTk.PhotoImage(self.PImg2)
		self.B2.config(image=self.Img2)
		self.B2.place(x=506,y=250)
		esc = open("Auxi.csv","a")
		esc.write(str(L[1]) + "\n")
		esc.close()
	
	def BT1(self):
		self.P2.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen1[0])
		i -= 1
		de = pd.read_csv("Comida.csv")

		new = open("Historial.csv","a")
		new.write("," + "P_2:" + de.Comida[i])
		new.close()

		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		j = int(df.Pantalla_2[0])
		j -= 1

		Carpeta = df.Carpeta[0]
		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(str(i) + ",")
		file.write(str(j) + "\n")
		file.close()

		remove("Auxi.csv")

		app = Call_Func()
		app.Call()
	
	def BT2(self):
		self.P2.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen2[0])
		i -= 1
		de = pd.read_csv("Comida.csv")

		new = open("Historial.csv","a")
		new.write("," + "P_2:" + de.Comida[i])
		new.close()

		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		j = int(df.Pantalla_2[0])
		j -= 1

		Carpeta = df.Carpeta[0]
		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(str(i) + ",")
		file.write(str(j) + "\n")
		file.close()

		remove("Auxi.csv")

		app = Call_Func()
		app.Call()

class Pantalla_3():
	def __init__(self):
		self.P3 = Tk()
		self.P3.title("PANTALLA 3")
		self.P3.iconbitmap("login.ico")
		self.x = self.P3.winfo_screenwidth()
		self.y = self.P3.winfo_screenheight()
		self.P3.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.P3.resizable(0,0)
		self.Frame = Frame(self.P3, width=900, height=600)
		self.Frame.pack()
		self.B1 = Button(self.Frame, text="SI", font=("Times New Roman",40), command=self.Positiva).place(x=200,y=350, width=200, height=80)
		self.B2 = Button(self.Frame, text="NO", font=("Times New Roman",40), command=self.Negativa).place(x=500,y=350, width=200, height=80)
		self.B3 = Button(self.Frame, text="Mostrar Pregunta", font=("Times New Roman",20), command=self.Most_Preg).place(x=340,y=50)
		self.Pregunta = Label(self.Frame)
		self.P3.mainloop()
	
	def Most_Preg(self):
		ds = pd.read_csv("AuxPre.csv")

		df = pd.read_csv("Preguntas_P3.csv")
		i = int(ds.Numero[0])
		
		if i > 0 and i <= len(df.axes[1]):
			self.Pregunta.config(text=df.iloc[0]["Pregunta"+str(i)], bg="green", font=("Times New Roman",40))
			self.Pregunta.place(x=48,y=120,width=800,height=70)

	def Positiva(self):
		ds = pd.read_csv("AuxPre.csv")
		i = int(ds.Numero[0])
		df = pd.read_csv("Preguntas_P3.csv")
		new = open("Historial.csv","a")
		new.write("," + df.iloc[0]["Pregunta"+str(i)] + ": " + "SI")
		new.close()

		remove("AuxPre.csv")
		file = open("AuxPre.csv","a")
		file.write("Numero"+",")
		file.write("\n" + str(i+1) + ",")
		file.close()

		self.P3.destroy()

		if i <= len(df.axes[1])-1:
			app = Pantalla_3()

	def Negativa(self):
		ds = pd.read_csv("AuxPre.csv")
		i = int(ds.Numero[0])
		df = pd.read_csv("Preguntas_P3.csv")
		new = open("Historial.csv","a")
		new.write("," + df.iloc[0]["Pregunta"+str(i)] + ": " + "NO")
		new.close()

		remove("AuxPre.csv")
		file = open("AuxPre.csv","a")
		file.write("Numero"+",")
		file.write("\n" + str(i+1) + ",")
		file.close()
		
		self.P3.destroy()

		if i <= len(df.axes[1])-1:
			app = Pantalla_3()

class Call_Func():
	
	def Call(self):
		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		j = int(df.Pantalla_2[0])

		if i > 0 or j > 0:
			numero = random.randint(1,2)
			if numero == 1 and i > 0:
				app = Pantalla_1()
			else:
				app = Pantalla_2()
		else:
			remove("AuxPre.csv")
			dr = pd.read_csv("NumPe.csv")
			file = open("AuxPre.csv","a")
			file.write("Numero"+",")
			file.write("\n" + str(dr.Numero[0]) + ",")
			file.close()
			app = Pantalla_3()

app = LogIn()
#app = Registro()
#app = PanelAd()
#app = Pantalla_1()
#app = Call_Func().Call()
#app.Call()
#app =  Pantalla_3()

#df = pd.read_csv("Historial.csv")
#print(df.Fecha["07/01/2022"])
from tkinter import *
from tkinter import ttk, filedialog
from os import remove
import pandas as pd
from PIL import Image, ImageTk
import random
import datetime
import re
import mysql.connector as sql


#_______________________________________________________Ventana LOGIN________________________________________________________________________________
class LogIn():
	def __init__(self):

		#Diseño de la ventana
		self.IniSe = Tk()
		self.IniSe.title("INICIO DE SESION")
		self.IniSe.iconbitmap("login.ico")
		
		self.x = self.IniSe.winfo_screenwidth()
		self.y = self.IniSe.winfo_screenheight()

		self.IniSe.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.IniSe.resizable(0,0) #para no poder editar el ancho de la ventana
		#Insertar imagen de fondo 
		
		self.IniSe.configure(bg = "#ffffff")
		canvas = Canvas(
			self.IniSe,
			bg = "#ffffff",
			height = 600,
			width = 900,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge")
		canvas.place(x = 0, y = 0)
		
		background_img = PhotoImage(file = f"background.png")
		background = canvas.create_image(
			367.0, 225.0,
			image=background_img)
		canvas.pack()

		
		self.EAdress = StringVar()
		self.Password = StringVar()

	# linea para escribir correo
		self.CorreoE = Entry(textvariable=self.EAdress, font=("Times New Roman",15), bg="#ffc0c0")
		self.CorreoE.place(width=300,height=35,x=80,y=260)

	# linea para escribir contraseña
		self.ContraE = Entry(textvariable=self.Password,show="*",font=20, bg='#ffc0f5')
		self.ContraE.place(width=300,height=30,x=80,y=380)

	# Botones 

		#--------------------ENVIAR----------------------------------------------------------
		enviar_btn= PhotoImage(file = "img1.png")
		img_label= Label(image=enviar_btn)
		self.Enviar = Button(command=self.Check, image=enviar_btn, borderwidth=0,bg="#ffffff").place(x=90, y=430)
		#--------------------REINTENTAR----------------------------------------------------------
		reintentar_btn= PhotoImage(file = "img0.png")
		img_label= Label(image=reintentar_btn)
		self.Reintentar = Button(command=self.Clave, image=reintentar_btn, borderwidth=0,bg="#ffffff").place(x=370, y=430)

		#---------------------ADMIN----------------------------------------------------------
		admin_btn= PhotoImage(file = "img2.png")
		img_label= Label(image=admin_btn)
		self.Admin = Button(command=self.Admin_Check, image=admin_btn, borderwidth=0,bg="#ffffff").place(x=230,y=430)

		#--------------------REGISTRO----------------------------------------------------------
		registro_btn= PhotoImage(file = "img3.png")
		img_label= Label(image=registro_btn)
		self.RegistroB = Button(command=self.OpReg, image=registro_btn, borderwidth=0,bg="#ffffff").place(x=577,y=483)
		
		self.AdvertenciaC = Label(self.IniSe)
		self.AdvertenciaP = Label(self.IniSe)

		self.IniSe.mainloop()


#_______________________Cierra la página para ingresar a la pag de REGISTRO_______________________________
	def OpReg(self):
		self.IniSe.destroy()
		Open = Registro()

#_______________________Cierra la página para ingresar a la Pagina de ADMIN (solo tenemos un correo)_______________________________	
	def Admin_Check(self):
		self.IniSe.destroy()

		Correo = self.EAdress.get()
		Pass = self.Password.get()
		if Correo == "admin":
			if Pass == "admin":
				app = PanelAd()

 #_______________________Una vez que se igrese coantraseña y correo, se buscaran en la base de datos_______________________________
	def Check(self):
		date = datetime.datetime.now()
		Valor = date.strftime('%d/%m/%Y,%H:%M:%S')

		archivo = open("Historial.csv","a")
		archivo.write("\n")
		archivo.write(Valor + ",")
		archivo.close()

		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)

		cursor = db.cursor()
		
		cursor.execute("SELECT * FROM datosadmin;")

		r = cursor.fetchall()

		remove("CopiaDA.csv")
		file = open("CopiaDA.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(r[0][0] + ",")
		file.write(r[0][1] + ",")
		file.write(r[0][2] + "\n")
		file.close()

		Correo = self.EAdress.get()
		Pass = self.Password.get()
		print(Correo)
		print(Pass)
		Lista_Correo = []
		Lista_Password = []
		
		cursor = db.cursor()
		
		cursor.execute("SELECT * FROM datosusuario;")

		r = cursor.fetchall()

		for i in r:
			Lista_Correo.append(i[7])

		for i in r:
			Lista_Password.append(i[8])

		for i in range(len(Lista_Correo)):
			if str(Correo) == Lista_Correo[i]:
				if str(Pass) == str(Lista_Password[i]):
					
					db = sql.connect(
						host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
						user="uiut865c60fxqdsj",
						passwd="wqeOsle44ltxwCFtn9dM",
						database="bgkjpnpib5jxjik9loxw"
					)
					

					cursor = db.cursor()

					x = Lista_Correo[i]
					inst = "SELECT Nombre, Apellidos FROM datosusuario WHERE Correo = %s"
					val = (x,)

					cursor.execute(inst, val)

					r = cursor.fetchall()

					self.IniSe.destroy()
					archivo = open("Historial.csv","a")
					archivo.write(r[0][0] + ",")
					archivo.write(r[0][1] + ",")
					archivo.write(Correo)
					archivo.close()
					app = Call_Func().Call()
				else:
					self.AdvertenciaL(2)
			else:
				self.AdvertenciaL(1)

 #_______________________Se acativara cuando se escriba correo o contraseña incorrecta (se puede activar con el boton "Reintentar")_______________________________
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



#______________________________________________VENTANA REGISTRO	__________________________________________________________________________________________________________________#

class Registro():
	def __init__(self):
		self.Raiz = Tk()
		self.Raiz.title("REGISTRO DE USUARIO")
		self.Raiz.iconbitmap("regist.ico")
		
		self.x = self.Raiz.winfo_screenwidth()
		self.y = self.Raiz.winfo_screenheight()
		self.Raiz.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		
		self.Raiz.configure(bg = "#ffffff")
		canvas = Canvas(
			self.Raiz,
			bg = "#ffffff",
			height = 600,
			width = 900,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge")
		canvas.place(x = 0, y = 0)

		background_img = PhotoImage(file = "registro/background.png")
		background = canvas.create_image(
			458.5, 339.5,
			image=background_img)
		canvas.pack()

		#_____________Declaracion de las variables de Entrada tipo string______________________
		self.TextNE = StringVar()
		self.TextAE = StringVar()
		self.TextEE =  StringVar()
		self.TextSE = StringVar()
		self.TextCE = StringVar()
		self.TextDE = StringVar()
		self.TextCrE = StringVar()
		self.TextPE = StringVar()
		self.var = StringVar(self.Raiz)
		self.div = StringVar(self.Raiz)

#_________________Menu desplegable con campus y divisiones___________________
		self.OpcionesCamp = ["Campus Guanajato","Campus Irapuato-Salamanca","Campus Celaya-Salvatierra","Campus León","Colegio Nivel Medio Superior"]
		self.OpcionesDiv_1 = ["Division de Arquitectura, Arte y Diseño", "Division de Ciencias Economico - Administrativas", "Division de Ciencias Naturales y Exactas", "Division de Ciencias Sociales y humanidades", "Division de Derecho, Politica y Gobierno", "Division de Ingenierias"]
		self.OpcionesDiv_2 = ["Division de Ciencias de la Vida", "Division de Ingenierias"]
		self.OpcionesDiv_3 = ["Division de Ciencias de la Salud e Ingenierias", "Division de Ciencias Sociales y Administrativas"]
		self.OpcionesDiv_4 = ["Division de Ciencias e Ingenierias", "Division de Ciencias de la Salud", "Division de Ciencias Sociales y Humanidades"]

# _____________________Cuadros de entrada___________________________________

		self.NombreE = Entry(textvariable=self.TextNE, font=("Times New Roman",14)).place(width=300,height=30,x=184,y=110)
		self.ApellidoE = Entry(textvariable=self.TextAE, font=("Times New Roman",14)).place(width=300,height=30,x=184,y=165)
		self.CorreoE = Entry(textvariable=self.TextCrE,font=("Times New Roman",14)).place(width=300,height=30,x=184,y=220)
		self.PasswordE = Entry(textvariable=self.TextPE,font=("Times New Roman",14)).place(width=300,height=30,x=184,y=275)
		self.EdadE = Entry(textvariable=self.TextEE,font=("Times New Roman",14)).place(width=130,height=30,x=393,y=352)
		self.SexoE = Entry(textvariable=self.TextSE,font=("Times New Roman",14)).place(width=130,height=30,x=393,y=424)
		self.CarreraE = Entry(textvariable=self.TextCE,font=("Times New Roman",14)).place(width=250,height=30,x=595,y=355)
		self.CampusE = OptionMenu(self.Raiz, self.var, *self.OpcionesCamp)
		self.CampusE.place(x=570,y=159)
		self.CampusE.config(width=25, font=("Times New Roman",15), bg="#FFFFFF")
		self.DivisionE = 0

# _________________________BOTONES_____________________________________________________________________________		
		#Boton de regreso
		regresar_btn= PhotoImage(file = f"registro/img1.png")
		img_label= Label(image=regresar_btn)
		self.BReg = Button(command=self.OpIni, image=regresar_btn, borderwidth=0,bg="#ffffff").place(x=633, y=484)
		
		#botod de registro
		registro_btn= PhotoImage(file = f"registro/img0.png")
		img_label= Label(image=registro_btn)
		self.BEnv = Button(command=self.Ingreso, image=registro_btn, borderwidth=0,bg="#ffffff").place(x=616, y=416)
		
		#boton de Guardar (para el campus)
		Gcamp_btn= PhotoImage(file = f"registro/img2.png")
		img_label= Label(image=Gcamp_btn)
		self.BCamp = Button(command=self.Divisiones, image=Gcamp_btn, borderwidth=0,bg="#ffffff").place(x=728, y=99)
		self.Check = Label(self.Raiz)

		
		self.Raiz.resizable(0,0)
		self.Raiz.mainloop()


#___________Regrear a la pantalla de login  (se activa con el boton regrear)_______________________________________
	def OpIni(self):
		self.Raiz.destroy()
		Open = LogIn()

#____________________Hace el registro en la base de dator (se activa con el boton registrarse)______________________________
	def Ingreso(self):
		Division = self.div.get()
		Texto_Correo = self.TextCrE.get()
		Texto_Password = self.TextPE.get()
		
		file = open("DatosUsuario.csv","a")
		file.write(Division + ",")
		file.write(Texto_Correo + ",")
		file.write(Texto_Password + "\n")
		file.close()

		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)
		
		cursor = db.cursor()

		inst = "UPDATE datosusuario SET Division=%s WHERE Division=%s"
		val = (Division, "NULL")

		cursor.execute(inst, val)

		inst = "UPDATE datosusuario SET Correo=%s WHERE Correo=%s"
		val = (Texto_Correo, "NULL")

		cursor.execute(inst, val)

		inst = "UPDATE datosusuario SET Password=%s WHERE Password=%s"
		val = (Texto_Password, "NULL")

		cursor.execute(inst, val)

		db.commit()	

		self.Check.config(text="Registro realizado correctamente!",font=("Times New Roman",15),bg="green2")
		self.Check.place(x=505,y=545)

		self.Check.after(5000,self.OpIni)


#______________El boton de "guardar" nos indicara la opcion de que campus se ha elegido para ver las opciones de divisiones___________
	
	def Divisiones(self):
		Campus = self.var.get()
		if Campus == "Campus Guanajato":
			self.DivisionE = OptionMenu(self.Raiz, self.div, *self.OpcionesDiv_1)
			self.DivisionE.place(x=570,y=257)
			self.DivisionE.config(width=33, font=("Times New Roman",12),bg="#ffffff")
		elif Campus == "Campus Irapuato-Salamanca":
			self.DivisionE = OptionMenu(self.Raiz, self.div, *self.OpcionesDiv_2)
			self.DivisionE.place(x=570,y=257)
			self.DivisionE.config(width=33, font=("Times New Roman",12),bg="#ffffff")
		elif Campus == "Campus Celaya-Salvatierra":
			self.DivisionE = OptionMenu(self.Raiz, self.div, *self.OpcionesDiv_3)
			self.DivisionE.place(x=570,y=257)
			self.DivisionE.config(width=33, font=("Times New Roman",12),bg="#ffffff")
		elif Campus == "Campus León":
			self.DivisionE = OptionMenu(self.Raiz, self.div, *self.OpcionesDiv_4)
			self.DivisionE.place(x=570,y=257)
			self.DivisionE.config(width=33, font=("Times New Roman",12),bg="#ffffff")

		Texto_Nombre = self.TextNE.get()
		Texto_Apellido = self.TextAE.get()
		Texto_Edad = self.TextEE.get()
		Texto_Sexo = self.TextSE.get()
		Texto_Carrera = self.TextCE.get()

		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)
		
		cursor = db.cursor()

		inst = "INSERT INTO datosusuario (Nombre, Apellidos, Edad, Sexo, Carrera, Campus, Division, Correo, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

		val = (Texto_Nombre, Texto_Apellido, Texto_Edad, Texto_Sexo, Texto_Carrera, Campus, "NULL", "NULL", "NULL")

		cursor.execute(inst, val)

		db.commit()

#_________________________VENTANA DE ADMINISTRADOR_____________________________

class PanelAd():
	def __init__(self):
		self.Raiz = Tk()
		self.Raiz.title("ADMINISTRADOR")
		self.Raiz.iconbitmap("admin.ico")

		self.x = self.Raiz.winfo_screenwidth()
		self.y = self.Raiz.winfo_screenheight()
		self.Raiz.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		self.Raiz.configure(bg = "#ffffff")
		canvas = Canvas(
			self.Raiz,
			bg = "#ffffff",
			height = 600,
			width = 900,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge")
		canvas.place(x = 0, y = 0)
		
		background_img = PhotoImage(file = f"admin/background.png")
		ackground = canvas.create_image(
			445.0, 318.0,
			image=background_img)
		canvas.pack()


	#____________declaracion de variales en tipo string_______________
		self.Pt1 = StringVar()
		self.Pt2 = StringVar()
		self.Pt3 = StringVar()
		self.var = StringVar(self.Raiz)

		self.Opciones = ["Comida","Deportes"]

	#___________Diseño de ventana_______________________
	
		self.TP_1_E = Entry(textvariable=self.Pt1, font=("Times New Roman",15)).place(width=200,height=30,x=580,y=162)
		self.TP_2_E = Entry(textvariable=self.Pt2, font=("Times New Roman",15)).place(width=200,height=30,x=580,y=226)
		self.TP_4_E = Entry(textvariable=self.Pt3, font=("Times New Roman",15)).place(width=200,height=30,x=580,y=286)
		self.C_S = OptionMenu(self.Raiz, self.var, *self.Opciones)
		self.C_S.place(x=580,y=415)
		self.C_S.config(font=("Times New Roman",15), bg="white")

#_____________________________Botones__________________________________

	#Boton de regreso
		regresar_btn= PhotoImage(file = f"admin/img0.png")
		img_label= Label(image=regresar_btn)
		self.BReg = Button(command=self.Return, image=regresar_btn, borderwidth=0,bg="#ffffff").place(x=470, y=493)
	
	#Boton de guardar cambios
		gcamb_btn= PhotoImage(file = f"admin/img1.png")
		img_label= Label(image=gcamb_btn)
		self.GCamb = Button(command=self.GCambios, image=gcamb_btn, borderwidth=0,bg="#ffffff").place(x=659, y=493)	
	
		
		self.Raiz.resizable(0,0)
		self.Raiz.mainloop()	
	
#_______________________Declaracion de funciones usadas en registro_____________	
	def GCambios(self):
		
		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)

		cursor = db.cursor()

		cursor.execute("DELETE FROM datosadmin")

		db.commit()

		Carpeta = self.var.get()
		Pantalla_1 = self.Pt1.get()
		Pantalla_2 = self.Pt2.get()
		Pantalla_3 = self.Pt3.get()
		print(Pantalla_3)
		Lista_p3 = re.split(",",Pantalla_3)
		
		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)
		
		cursor = db.cursor()

		inst = "INSERT INTO datosadmin (Carpeta, Pantalla_1, Pantalla_2) VALUES (%s, %s, %s)"

		val = (Carpeta, Pantalla_1, Pantalla_2)

		cursor.execute(inst, val)

		db.commit()

		
		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)
		
		cursor = db.cursor()
		cursor.execute("DELETE FROM preguntas_p3")
		db.commit()

		for i in range(len(Lista_p3)):

			db = sql.connect(
				host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
				user="uiut865c60fxqdsj",
				passwd="wqeOsle44ltxwCFtn9dM",
				database="bgkjpnpib5jxjik9loxw"
			)
			cursor = db.cursor()
			inst = "INSERT INTO preguntas_p3 (id, Preguntas) VALUES (%s, %s)"
			val = (str(i+1),Lista_p3[i])
			cursor.execute(inst, val)
			db.commit()


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

		remove("Carpeta.csv")
		carpeta = self.var.get()
		file = open("Carpeta.csv","a")
		file.write("Carpeta"+",")
		file.write("\n" + carpeta + ",")
		file.close()

		remove("DatosAdmin.csv")
		file = open("DatosAdmin.csv","a")
		file.write("Carpeta" + ",")
		file.write("Pantalla_1" + ",")
		file.write("Pantalla_2" + "\n")
		file.write(Carpeta + ",")
		file.write(Pantalla_1 + ",")
		file.write(Pantalla_2 + "\n")
		file.close()
	
	def Return(self):
		self.Raiz.destroy()
		app = LogIn()


#___________________________Pantalla 1________________________________
class Pantalla_1():
	def __init__(self):
		self.P1 = Tk()
		self.P1.title("PANTALLA 1")
		self.P1.iconbitmap("pant.ico")
		
		self.x = self.P1.winfo_screenwidth()
		self.y = self.P1.winfo_screenheight()
		self.P1.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))

		self.P1.configure(bg = "#ffffff")
		canvas = Canvas(
			self.P1,
			bg = "#ffffff",
			height = 600,
			width = 900,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge")
		canvas.place(x = 0, y = 0)
		
		background_img = PhotoImage(file = f"P1/background.png")
		background = canvas.create_image(
			450.0, 300.0,
			image=background_img)
		canvas.pack()

		self.P1.resizable(0,0)


		#_____________________Definicion de botones________________________
		self.B1 = Button(self.P1, command=self.BT1)
		self.B2 = Button(self.P1, command=self.BT2)
		self.B3 = Button(self.P1, command=self.BT3)
		self.B4 = Button(self.P1, command=self.BT4)
		
		#Boton para visualizar las imagenes
		prefieres_btn= PhotoImage(file = f"P1/img0.png")
		img_label= Label(image=prefieres_btn)
		self.BB = Button(self.P1, command=self.Asign_Img, image=prefieres_btn, borderwidth=0,bg="#ffffff").place(x=176, y=29)
		
		self.P1.mainloop()

	#____________________Declaracion de funciones___________________________
	def Asign_Img(self):
		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)
		df = pd.read_csv(nombre + ".csv")
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

		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)

		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen1[0])
		i -= 1
		de = pd.read_csv(nombre + ".csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de[nombre][i])
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

		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)

		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen2[0])
		i -= 1
		de = pd.read_csv(nombre + ".csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de[nombre][i])
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

		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)

		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen3[0])
		i -= 1
		de = pd.read_csv(nombre + ".csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de[nombre][i])
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

		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)

		self.P1.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen4[0])
		i -= 1
		de = pd.read_csv(nombre + ".csv")

		new = open("Historial.csv","a")
		new.write("," + "P_1:" + de[nombre][i])
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

# ___________________________Pantalla 2________________________________

class Pantalla_2():
	def __init__(self):
		self.P2 = Tk()
		self.P2.title("PANTALLA 2")
		self.P2.iconbitmap("pant.ico")
		
		self.x = self.P2.winfo_screenwidth()
		self.y = self.P2.winfo_screenheight()
		self.P2.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))

		self.P2.configure(bg = "#ffffff")
		canvas = Canvas(
			self.P2,
			bg = "#ffffff",
			height = 600,
			width = 900,bd = 0,
			highlightthickness = 0,
			relief = "ridge")
		canvas.place(x = 0, y = 0)
		
		background_img = PhotoImage(file = f"P2/background.png")
		background = canvas.create_image(
			450.0, 300.0, 
			image=background_img)
		canvas.pack()

		
		#______________Botones____________________
		
		self.B1 = Button(self.P2, command=self.BT1)
		self.B2 = Button(self.P2, command=self.BT2)
	
	#Boton para visualizar las imagenes
		prefieres_btn= PhotoImage(file = f"P2/img0.png")
		img_label= Label(image=prefieres_btn)
		self.BB = Button(self.P2, command=self.Asign_Img, image=prefieres_btn, borderwidth=0,bg="#ffffff").place(x=221, y=76)
		
		
		self.P2.resizable(0,0)
		self.P2.mainloop()

#______________Definimos las funciones________________
	
	def Asign_Img(self):
		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)
		df = pd.read_csv(nombre + ".csv")
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

		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)

		self.P2.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen1[0])
		i -= 1
		de = pd.read_csv(nombre + ".csv")

		new = open("Historial.csv","a")
		new.write("," + "P_2:" + de[nombre][i])
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

		dk = pd.read_csv("Carpeta.csv")
		nombre = dk.Carpeta[0]
		print(nombre)

		self.P2.destroy()

		da = pd.read_csv("Auxi.csv")
		i = int(da.Imagen2[0])
		i -= 1
		de = pd.read_csv(nombre + ".csv")

		new = open("Historial.csv","a")
		new.write("," + "P_2:" + de[nombre][i])
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

#___________________________Pantalla 3________________________________

class Pantalla_3():
	def __init__(self):
		self.P3 = Tk()
		self.P3.title("PANTALLA 3")
		self.P3.iconbitmap("preg.ico")
		self.x = self.P3.winfo_screenwidth()
		self.y = self.P3.winfo_screenheight()
		self.P3.geometry("900x600"+"+"+str(int(self.x/7))+"+"+str(int(self.y/20)))
		
		self.P3.configure(bg = "#ffffff")
		canvas = Canvas(
			self.P3,
			bg = "#ffffff",
			height = 600,
			width = 900,
			bd = 0,
			highlightthickness = 0,
			relief = "ridge")
		canvas.place(x = 0, y = 0)

		background_img = PhotoImage(file = f"P3/background.png")
		background = canvas.create_image(
			440.5, 300.0,
			image=background_img)
		canvas.pack()

		
		#_________________botones______________________________________
		
		#Boton si
		b1_btn= PhotoImage(file = f"P3/img1.png")
		img_label= Label(image=b1_btn)
		self.B1 = Button(self.P3, command=self.Positiva, image=b1_btn, borderwidth=0,bg="white").place(x=467, y=317)

		#Boton NO
		b2_btn= PhotoImage(file = f"P3/img2.png")
		img_label= Label(image=b2_btn)
		self.B2 = Button(self.P3, command=self.Negativa, image=b2_btn, borderwidth=0,bg="white").place(x=467, y=430)
		
		#Boton 	MOSTRAR
		b3_btn= PhotoImage(file = f"P3/img0.png")
		img_label= Label(image=b3_btn)
		self.B3 = Button(self.P3, command=self.Most_Preg, image=b3_btn, borderwidth=0,bg="#FFFFFF").place(x=255, y=46)
		self.Pregunta = Label(self.P3)
		

		self.P3.resizable(0,0)
		self.P3.mainloop()
	
	#______________________Definicion de funciones____________________________
	
	#Mostrar la pregunta
	def Most_Preg(self):

		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)

		cursor = db.cursor()
		cursor.execute("SELECT * FROM preguntas_p3;")
		r = cursor.fetchall()

		Lista_Preg = ["null"]

		for i in r:
			Lista_Preg.append(i[1])

		ds = pd.read_csv("AuxPre.csv")
		i = int(ds.Numero[0])
		
		if i > 0 and i <= len(Lista_Preg):
			self.Pregunta.config(text=Lista_Preg[i], bg="#FBD276", font=("Yu Gothic Medium",33))
			self.Pregunta.place(x=100,y=170,width=650,height=60)

	#Respuesta "si"
	def Positiva(self):

		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)

		cursor = db.cursor()
		cursor.execute("SELECT * FROM preguntas_p3;")
		r = cursor.fetchall()

		Lista_Preg = ["null"]

		for i in r:
			Lista_Preg.append(i[1])

		ds = pd.read_csv("AuxPre.csv")
		i = int(ds.Numero[0])
		new = open("Historial.csv","a")
		new.write("," + Lista_Preg[i] + ": " + "SI")
		new.close()

		remove("AuxPre.csv")
		file = open("AuxPre.csv","a")
		file.write("Numero"+",")
		file.write("\n" + str(i+1) + ",")
		file.close()

		self.P3.destroy()

		if i <= len(Lista_Preg)-2:
			app = Pantalla_3()

	#Respuesta "no"
	def Negativa(self):

		db = sql.connect(
			host="bgkjpnpib5jxjik9loxw-mysql.services.clever-cloud.com",
			user="uiut865c60fxqdsj",
			passwd="wqeOsle44ltxwCFtn9dM",
			database="bgkjpnpib5jxjik9loxw"
		)

		cursor = db.cursor()
		cursor.execute("SELECT * FROM preguntas_p3;")
		r = cursor.fetchall()

		Lista_Preg = ["null"]

		for i in r:
			Lista_Preg.append(i[1])

		ds = pd.read_csv("AuxPre.csv")
		i = int(ds.Numero[0])
		new = open("Historial.csv","a")
		new.write("," + Lista_Preg[i] + ": " + "NO")
		new.close()

		remove("AuxPre.csv")
		file = open("AuxPre.csv","a")
		file.write("Numero"+",")
		file.write("\n" + str(i+1) + ",")
		file.close()
		
		self.P3.destroy()

		if i <= len(Lista_Preg)-2:
			app = Pantalla_3()

#___________________________Funcion de llamado________________________________

class Call_Func():
	
	def Call(self):
		df = pd.read_csv("CopiaDA.csv")
		i = int(df.Pantalla_1[0])
		j = int(df.Pantalla_2[0])

		if i > 0 or j > 0:
			numero = random.randint(1,2)
			if numero == 1 and i > 0:
				app = Pantalla_1()
			elif j > 0:
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


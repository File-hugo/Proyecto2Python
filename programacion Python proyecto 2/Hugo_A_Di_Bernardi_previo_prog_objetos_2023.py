import tkinter as tk#importo tkinter como tk
from tkinter import *#de tkinter importa todo (no buena practica)
import datetime
from datetime import datetime#Importo modulo para fecha y hora de ingreso y egreso
import cv2

from PIL import Image, ImageTk#modulo para imagenes 
import csv#modulo para trabajar con datos
import sqlite3#modulo de base de datos
#-
root=tk.Tk()#Creo ventana principal
root.geometry("800x500")#dimensiones de ventana
newWindow=Toplevel(root)# Ventana de usuario administrador
newWindow.geometry("900x800")#Dimension de la ventana
newWindow.title("Ventana 2")#Titulo de ventana
newWindow.withdraw()#Oculta la ventana creada
newWindowDos=Toplevel(root)
newWindowDos.geometry("900x500")
newWindowDos.title("Ventana de no admin")
newWindowDos.withdraw()#Oculta la ventana
#Para no poder maximizar ventana
root.resizable(width=0,height=0)
newWindow.resizable(width=0,height=0)
newWindowDos.resizable(width=0,height=0)
#-
miConexion=sqlite3.connect("Garage.db")#Abro la base de datos
miCursor=miConexion.cursor()#Creo objeto cursor
#-
patenteGarage=StringVar()#Creo variables de tipo string para ponerlas dentro de los entries
colorGarage=StringVar()
marcaGarage=StringVar()
modeloGarage=StringVar()
entradaAlGarage=StringVar()
salidaAlGarage=StringVar()
movimientoGarage=StringVar()

#-
fechaActual = datetime.now() # Pone la fecha actual con now y datetime usa su modulo importado
date_time = fechaActual.strftime("%m/%d/%Y, %H:%M:%S")
#M es mes,D es dia,Y es año. H es hora, M es minutos y S es segundos
#datos=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]

#---
#ID INTEGER PRIMARY KEY AUTOINCREMENT,
datos=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]
#Almaceno los datos en una lista y los obtengo con .get() de manera global       
def creoBBDD():
#Si no existe la tabla, la crea vacía. Execute es para ejecutar consultas.
#Insert inserta cosas en la tabla.
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()
    miCursor.execute('''
        CREATE TABLE IF NOT EXISTS movimientos(
        patente VARCHAR(30),
        marca VARCHAR(30),
        modelo VARCHAR (30),
        color VARCHAR (30),
        fechaYhora DATETIME,
        movimiento VARCHAR(30),
        entrada VARCHAR(30),
        salida VARCHAR (30)
        )''')
    miConexion.commit()
creoBBDD()#Crea la base de datos al correr el programa
#----------
textoUsuarioPatente=tk.Label(newWindow,text="Ingresa patente",font="Times 15")#Crea texto
textoUsuarioPatente.grid(row=0,column=0,sticky="WN",pady=100,padx=0)#Lo ubica
#Crea campo de texto
ingresaUsuarioPatente=tk.Entry(newWindow,font="Times 15",width=10,border=5,textvariable=patenteGarage)
#Ubica el stringVar
ingresaUsuarioPatente.grid(row=0,column=0,sticky="WN",pady=100,padx=190)
ingresaUsuarioPatente.focus()#Focusea el entry no haciendo falta cliquear para escribir
#-  
textoUsuarioMarca=tk.Label(newWindow,text="Ingresa marca",font="Times 15")
textoUsuarioMarca.grid(row=0,column=0,sticky="WN",pady=200)
ingresaUsuarioMarca=tk.Entry(newWindow,font="Times 15",width=15,border=5,textvariable=marcaGarage)
ingresaUsuarioMarca.grid(row=0,column=0,sticky="WN",pady=200,padx=190)
#-
textoUsuarioModelo=tk.Label(newWindow,text="Ingresa modelo",font="Times 15")
textoUsuarioModelo.grid(row=0,column=0,sticky="WN",pady=290)
ingresaUsuarioModelo=tk.Entry(newWindow,font="Times 15",width=10,border=5,textvariable=modeloGarage)
ingresaUsuarioModelo.grid(row=0,column=0,sticky="WN",pady=290,padx=190)
#-
textoUsuarioColor=tk.Label(newWindow,text="Ingresa color",font="Times 15")
textoUsuarioColor.grid(row=0,column=0,sticky="WN",pady=390)
ingresaUsuarioColor=tk.Entry(newWindow,font="Times 15",width=10,border=5,textvariable=colorGarage)
ingresaUsuarioColor.grid(row=0,column=0,sticky="WN",pady=390,padx=190)
#-
textoEntrada=tk.Label(newWindow,text="Entrada",font="Times 15")
textoEntrada.grid(row=0,column=0,sticky="WN",pady=490)
ingresaEntrada=tk.Entry(newWindow,font="Times 15",width=10,border=5,textvariable=entradaAlGarage)
ingresaEntrada.grid(row=0,column=0,sticky="WN",pady=490,padx=130)
#-
#Debe poner si o no
#labelMensajeEntrada=tk.Label(newWindow,text="Pon SI o NO",font="Times 15 underline")
#labelMensajeEntrada.grid(row=0,column=0,sticky="WN",pady=490,padx=300)
#labelMensajeSalida=tk.Label(newWindow,text="Pon SI o NO",font="Times 15 underline")
#labelMensajeSalida.grid(row=0,column=0,sticky="WN",pady=540,padx=300)
#---------------
textoSalida=tk.Label(newWindow,text="Salida",font="Times 15")
textoSalida.grid(row=0,column=0,pady=540,sticky="WN")
ingresaSalida=tk.Entry(newWindow,font="Times 15",width=10,border=5,textvariable=salidaAlGarage)
ingresaSalida.grid(row=0,column=0,sticky="WN",pady=540,padx=130)
#-
labelSalidaMensaje=tk.Label(newWindow,text="si/Si en salir para borrar registro",font="Times 14 bold")#Fuente en negrita
labelSalidaMensaje.grid(padx=400,pady=460,row=0,column=0,sticky="WN")
labelSalidaMensaje.after(9000, labelSalidaMensaje.grid_forget)#mensaje temporal que se va a los 9000 milisegundos
#-
textoMovimiento=tk.Label(newWindow,text="Movimiento",font="Times 15")
textoMovimiento.grid(row=0,column=0,sticky="WN",pady=640,padx=250)
#-
#insertoMovimiento=tk.Entry(newWindow,font="Times 15",width=12,border=5,textvariable=movimientoGarage)
#insertoMovimiento.grid(row=0,column=0,sticky="WN",pady=640,padx=410) 
#-----
pagadoLabel=tk.Label(newWindow,font="Times 14",text="Pagado")
pagadoLabel.grid(column=0,row=0,sticky="WN",pady=640,padx=0)                
#---------
textoUsuario=tk.Label(root,text="Ingresa usuario:",font="Times 15")
textoUsuario.grid(row=0,column=0,sticky="WN",pady=50,padx=50)
ingresaUsuario=tk.Entry(root,font="Times 15",border=5,width=15)
ingresaUsuario.grid(row=0,column=0,sticky="WN",padx=250,pady=50)
#-
textoContraseña=tk.Label(root,text="Ingresa contraseña:",font="Times 15")
textoContraseña.grid(row=0,column=0,sticky="WN",pady=140,padx=10)
ingresaContraseña=tk.Entry(root,font="Times 15",border=5,width=15)
ingresaContraseña.grid(row=0,column=0,sticky="WN",pady=140,padx=250)
#-
datosVacios=True#valor booleano (o es True o es False)
#-
contraseñasUsuarioAdmin=["A123"]
contraseñasUsuarioGenerico=["12345"]
opcionesUsuarioAdmin=["Administrador"]
opcionesUsuarioGenerico=["Hugo",",","Diego",",","Rosario",",","Celeste",",","Maria",","]
opcionesUsuarioGenericoDos=["Leonardo"]

coloresAuto=["gris","plateado","dorado","purpura","celeste","marron","naranja","verde","violeta","rojo","azul","amarillo","negro","rosa","blanco"]
opcionesUsuarioLabel=tk.Label(root,text=opcionesUsuarioAdmin,font="Times 13")
opcionesUsuarioLabel.grid(row=0,column=0,padx=10,pady=320,sticky="WN")

opcionesUsuarioLabelDos=tk.Label(root,text="Estos son los usuarios admin:",font="Times 13 bold")
opcionesUsuarioLabelDos.grid(row=0,column=0,padx=10,pady=280,sticky="WN")
textoContraseñasUsuarioAdmin=tk.Label(root,font="Times 13 bold",text="Contraseña para administra-\ndores es:",anchor="e", justify=LEFT)
textoContraseñasUsuarioAdmin.grid(row=0,column=0,sticky="WN",pady=360,padx=10)
contraseñaUsuariosAdmin=tk.Label(root,font="Times 13",text=contraseñasUsuarioAdmin)
contraseñaUsuariosAdmin.grid(row=0,column=0,sticky="WN",pady=392,padx=120)

textoUsuarioGenericoLabel=tk.Label(root,font="Times 13 bold",text="Usuarios no administradores es:",anchor="e", justify=LEFT)
textoUsuarioGenericoLabel.grid(row=0,column=0,sticky="WN",pady=280,padx=360)
textoUsuarioGenericoLabelDos=tk.Label(root,font="Times 13",text=opcionesUsuarioGenerico)
textoUsuarioGenericoLabelDos.grid(row=0,column=0,sticky="WN",pady=320,padx=360)
textoUsuarioGenericoLabelDosParteDos=tk.Label(root,font="Times 13",text=opcionesUsuarioGenericoDos)
textoUsuarioGenericoLabelDosParteDos.grid(row=0,column=0,sticky="WN",pady=355,padx=360)

contraseñaGenericoLabel=tk.Label(root,font="Times 13 bold",text="Contraseñas para no administradores\nes:",anchor="e", justify=LEFT)
contraseñaGenericoLabel.grid(row=0,column=0,sticky="WN",pady=390,padx=360)
contraseñaGenericoLabelDos=tk.Label(root,font="Times 13",text="12345",anchor="e", justify=LEFT)
contraseñaGenericoLabelDos.grid(row=0,column=0,sticky="WN",pady=423,padx=400)

#-----------------
valorNombreJugador=tk.StringVar()
count=0

ventanaAdmin=True
ventanaNoAdmin=True
#------
def ventanaDos(*args):
    global opcionesUsuarioGenerico
    global opcionesUsuarioGenericoDos
    global contadorVentanasNewWindow
    global contadorVentanasNewWindowDos
    usuarios=ingresaUsuario.get()
    contraseñas=ingresaContraseña.get()
    #ax = ' '.join([str(elem) for elem in opciones])
    #bx = ' '.join([str(elem) for elem in opciones])
    if usuarios!="" and contraseñas!="" and contraseñas == contraseñasUsuarioAdmin[0] and usuarios == opcionesUsuarioAdmin[0]:
    ###Abre ventana Admin###
        datosVacios=True
        newWindow.deiconify()#Visualiza la ventana creada
        
        if newWindow.winfo_exists() and newWindowDos.winfo_exists():
#Si ventana admin existe primero y la no admin luego tambien, oculto la no admin
            #print("EXISTE ventana admin")
            newWindowDos.withdraw()
            root.withdraw()
        #root.withdraw()#muestra ventana
#Abre imagen con dimensiones width primero y luego height
        photo=ImageTk.PhotoImage(Image.open("lupa imagen.png").resize((50,50))) 
        labelImage = Label(image=photo)
#Lo pasa a label para poder introducirlo en el boton
        ingresaBuscar=tk.Button(newWindow,image=photo,text="Buscar (por patente)",font="Times 14 bold",
            command=buscar, compound= "right",width=310,anchor="w")
        ingresaBuscar.grid(row=0,column=0,sticky="WN",padx=450,pady=90)
                
        botonSalida=tk.Button(newWindow,text="SALE_||",font="Times 14 bold",command=eliminar)
        botonSalida.grid(column=0,row=0,sticky="WN",padx=701,pady=510)                

    ###Abre ventana no Admin###
    if usuarios!="" and contraseñas!="" and contraseñas in contraseñasUsuarioGenerico[0] and usuarios in opcionesUsuarioGenerico or usuarios in opcionesUsuarioGenericoDos:
#     if usuarios.lower() in opcionesUsuario:#Abre ventana usuario admin
        datosVacios=True

        newWindowDos.deiconify()#muestra ventana
#Si ventana no admin existe primero y la  admin luego tambien, oculto la admin
        if newWindowDos.winfo_exists():
            print("Existe ventana NO admin")
        if newWindowDos.winfo_exists() and newWindow.winfo_exists():
            print("Existe ventana admin")
            newWindow.withdraw()
            root.withdraw()
            
        textoUsuarioPatenteDos=tk.Label(newWindowDos,text="Ingresa patente",font="Times 15")
        textoUsuarioPatenteDos.grid(row=0,column=0,sticky="WN",pady=100,padx=0)
                                                     #-
        ingresaUsuarioPatenteDos=tk.Entry(newWindowDos,font="Times 15",width=10,border=5,textvariable=patenteGarage)
        ingresaUsuarioPatenteDos.grid(row=0,column=0,sticky="WN",pady=100,padx=190)
        ingresaUsuarioPatenteDos.focus()
                                                       
        textoUsuarioMarcaDos=tk.Label(newWindowDos,text="Ingresa marca",font="Times 15")
        textoUsuarioMarcaDos.grid(row=0,column=0,sticky="WN",pady=200)
        ingresaUsuarioMarcaDos=tk.Entry(newWindowDos,font="Times 15",width=15,border=5,textvariable=marcaGarage)
        ingresaUsuarioMarcaDos.grid(row=0,column=0,sticky="WN",pady=200,padx=190)
        #-
        textoUsuarioModeloDos=tk.Label(newWindowDos,text="Ingresa modelo",font="Times 15")
        textoUsuarioModeloDos.grid(row=0,column=0,sticky="WN",pady=290)
        ingresaUsuarioModeloDos=tk.Entry(newWindowDos,font="Times 15",width=10,border=5,textvariable=modeloGarage)
        ingresaUsuarioModeloDos.grid(row=0,column=0,sticky="WN",pady=290,padx=190)
                                                     #-
        textoUsuarioColorDos=tk.Label(newWindowDos,text="Ingresa color",font="Times 15")
        textoUsuarioColorDos.grid(row=0,column=0,sticky="WN",pady=390)
        ingresaUsuarioColorDos=tk.Entry(newWindowDos,font="Times 15",width=10,border=5,textvariable=colorGarage)
        ingresaUsuarioColorDos.grid(row=0,column=0,sticky="WN",pady=390,padx=190)
                                  
        photoDos=ImageTk.PhotoImage(Image.open("lupa imagen.png").resize((50,50)))
        labelImageDos = Label(image=photoDos)
        ingresaBuscarDos=tk.Button(newWindowDos,image=photoDos,text="Buscar (por patente)",font="Times 14 bold",
            command=buscarVentanaNoAdmin, compound= "right",width=310,anchor="w")
        ingresaBuscarDos.grid(row=0,column=0,sticky="WN",padx=450,pady=90)              
    #Si valor usuario y contraseña esta vacio       
    elif usuarios=="" and contraseñas=="" or contraseñas != contraseñasUsuarioAdmin[0] or usuarios != opcionesUsuarioAdmin[0]:
        datosVacios=False
        messagebox.showinfo("Aviso","Datos vacios o erroneos")   
    newWindow.mainloop()      
    newWindowDos.mainloop()     
#---------            
def preguntoCierroVentana():#Pregunta si queres cerrar o no la ventana
    if messagebox.askokcancel("Aviso: salir", "¿Deseas salir?"):
        newWindowDos.destroy()#Destroy cierra ventana
        newWindow.destroy()
        root.destroy() 
#-------------       
newWindowDos.protocol("WM_DELETE_WINDOW", preguntoCierroVentana)#Protocolo que va con la funcion
root.protocol("WM_DELETE_WINDOW", preguntoCierroVentana)
newWindow.protocol("WM_DELETE_WINDOW", preguntoCierroVentana)
#------------
def validoEntradaSalida():
    boolValidoEntradasalida=True#Valor booleano
    miConexion=sqlite3.connect("Garage.db")#Abre localmente la ventana
    miCursor=miConexion.cursor()#Crea cursor de la base datos para
    color=colorGarage.get()#Creo variable igual al valor.get
    coloresAuto=["gris","plateado","dorado","purpura","celeste","marron","naranja","verde","violeta","rojo","azul","amarillo","negro","rosa","blanco"]
    if color not in coloresAuto:#Si no esta el color en la lista
        boolValidoEntradasalida=False
        labelAvisoMalColor=tk.Label(newWindow,text="Color incorrecto o invalido",font="Times 15 bold")
        labelAvisoMalColor.grid(padx=460,pady=240,row=0,column=0,sticky="WN")
        labelAvisoMalColor.after(4000, labelAvisoMalColor.grid_forget)
        messagebox.showinfo("Error","Color incorrecto")#mensaje o pop up
    elif color in coloresAuto:#Si el valor esta
        boolValidoEntradasalida=True

#-------------
def editar():
    patenteIgual=False
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()    
    nuevo=open("Garage.csv","w")
    #-
    contadorDigitos=0
    contadorLetras=0
    global adminNoAdmin
    valoresEntrada=["Si","si"]
    valoresSalida=["No","no"]

    booleanoDeEntrada=True
    #-
    datosEditar=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]
    #datosEditar=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get()]
    #now = datetime.now() # current date and time
    #date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    color=colorGarage.get()
    entrada=entradaAlGarage.get()
    salida=salidaAlGarage.get()

    if patenteGarage.get()=="":
        #messagebox.showinfo("Aviso","Debe introducir patente para ver sus registros",parent=newWindowDos)
        labelAvisoPagoEditarUno=tk.Label(newWindow,text="La patente no debe estar vacia",font="Times 15 bold")
        labelAvisoPagoEditarUno.grid(padx=50,pady=30,row=0,column=0,sticky="WN")
        labelAvisoPagoEditarUno.after(9000, labelAvisoPagoEditarUno.grid_forget)
        messagebox.showinfo("Aviso","Introduce una patente")    
        pass
    if patenteGarage.get():
        for c in patenteGarage.get():
            if c in ("0123456789"):
                contadorDigitos+=1
            #print(contadorDigitos,"Numeros")
            if contadorDigitos>3:
                patenteIgual=False
            if contadorDigitos<=2:
                patenteIgual=False
            elif contadorDigitos==3:
                patenteIgual=True
    if patenteGarage.get():
        for cc in patenteGarage.get():
            if cc not in ("0123456789"):
                contadorLetras+=1
            #print(contadorDigitos,"Numeros")
            if contadorLetras>3:
                patenteIgual=False
            if contadorLetras<=2:
                patenteIgual=False
            elif contadorLetras==3:
                patenteIgual=True
        

        if color in coloresAuto and patenteIgual==True and entrada in valoresEntrada and booleanoDeEntrada==True and salida in valoresSalida and booleanoDeEntrada==True:
            if marcaGarage.get() not in 'marca':
                miCursor.execute("UPDATE movimientos SET marca=?WHERE patente=?",[datosEditar[1]] +[datosEditar[0]] )
                print("valor editado")
                miConexion.commit()            
            if modeloGarage.get() not in 'modelo':
                miCursor.execute("UPDATE movimientos SET modelo=?WHERE patente=?",[datosEditar[2]] +[datosEditar[0]] )
                print("valor editado")
                miConexion.commit()    
            if colorGarage.get() not in 'color':
                miCursor.execute("UPDATE movimientos SET color=?WHERE patente=?",[datosEditar[3]] +[datosEditar[0]] )
                print("valor editado")
                miConexion.commit()
            if date_time not in 'fechaYhora':
                miCursor.execute("UPDATE movimientos SET fechaYhora=?WHERE patente=?",[datosEditar[4]] +[datosEditar[0]] )
                print("valor editado")
                miConexion.commit()
                #if movimientoGarage.get() not in 'movimiento':
                #    miCursor.execute("UPDATE movimientos SET movimiento=?WHERE patente=?",[datosEditar[5]] +[datosEditar[0]] )
                #    print("valor editado")
                #    miConexion.commit()
            if entradaAlGarage.get() not in 'entrada':
                miCursor.execute("UPDATE movimientos SET entrada='Si' WHERE patente=?",[datosEditar[0]] )
                print("valor editado")
                miConexion.commit()
                booleanoDeEntrada=True              
            if salidaAlGarage.get() not in 'salida':
                miCursor.execute("UPDATE movimientos SET salida='No' WHERE patente=?",[datosEditar[0]] )
                print("valor editado")
                miConexion.commit()
                booleanoDeEntrada=True              

            if (marcaGarage.get() not in 'marca' or modeloGarage.get() not in 'modelo' or colorGarage.get() not in 'color' or movimientoGarage.get() not in 'movimiento' or date_time not in 'fechaYHora'
                or entradaAlGarage.get() not in 'entrada' or salidaAlGarage.get() not in 'salida' and patenteIgual==True and contadorLetras==3
                and contadorDigitos==3 and valoresEntrada=="Si" and valoresSalida=="No"): 
                messagebox.showinfo("BBDD","Registro actualizado con exito")            
            else:
                messagebox.showinfo("BBDD","Debe introducir un campo a modificar")               
               
        elif color not in coloresAuto and color!="":
            boolValidoEntradasalida=False
            labelAvisoMalColor=tk.Label(newWindow,text="Color incorrecto o invalido",font="Times 15 bold")
            labelAvisoMalColor.grid(padx=460,pady=240,row=0,column=0,sticky="WN")
            labelAvisoMalColor.after(6000, labelAvisoMalColor.grid_forget)
            messagebox.showinfo("Error","Color incorrecto")
        elif entrada.lower()!="Si" or salida.lower()!="No":
            booleanoDeEntrada=False
            messagebox.showinfo("BBDD","Debe escribir si/Si y No/no")
    if patenteIgual==False:
        messagebox.showinfo("Aviso","Debe tener 3 numeros y 3 letras")
       
#--------------
def insertoDatos():
    miConexion=sqlite3.connect("Garage.db")
    nuevo=open("Garage.csv","w")
    miCursor=miConexion.cursor()
    salirPatente=True
    boolTrue=True    
    global adminNoAdmin
    #stringNoPago="No pago"
    #miCursor.execute("SELECT patente FROM movimientos WHERE patente=?",[patenteGarage.get()])
    miCursor.execute("SELECT patente FROM movimientos")
    verificoPatente=miCursor
    
    a = ','.join(str(x) for x in verificoPatente)#La lista con tupla anidada ahora es solo tupla
    #print(s)#es ahora tupla
           #labelEntradaBuscandoPatente=tk.Label(newWindow,text="El auto está adentro",font="Times 25 bold")
    verificoPatenteSinComa=a.replace(",","")
    
    fechaActual = datetime.now() # current date and time
    fecha = fechaActual.strftime("%m/%d/%Y, %H:%M:%S")
    print("date and time:",fecha)                           
            
    datosInsertoDatos=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]
    #Null porque el id es autonumerico, luego pondremos 5 ? o parametros porque tenemos 5 campos mas aparte del null        if items=="":
    color=colorGarage.get()
    
    patenteIgual=True            
    if patenteGarage.get() in verificoPatenteSinComa:
        messagebox.showinfo("Aviso","La patente ya esta insertada")
        patenteIgual=False
        
    elif patenteGarage.get() not in verificoPatenteSinComa:
        patenteIgual=False
    
    contadorDigitos=0
    contadorLetras=0
    if patenteGarage.get():
        for c in patenteGarage.get():
            if c in ("0123456789"):
                contadorDigitos+=1
        #print(contadorDigitos,"Numeros")
            if contadorDigitos>3:
                patenteIgual=False
            if contadorDigitos<=2:
                patenteIgual=False
            elif contadorDigitos==3:
                patenteIgual=True
    if patenteGarage.get():
        for cc in patenteGarage.get():
            if cc not in ("0123456789"):
                contadorLetras+=1
        #print(contadorDigitos,"Numeros")
            if contadorLetras>3:
                patenteIgual=False
            if contadorLetras<=2:
                patenteIgual=False
            elif contadorLetras==3:
                patenteIgual=True      
        if patenteIgual==False:
            messagebox.showinfo("Aviso","Debe tener 3 numeros y 3 letras")
            #print(contadorDigitos)
        if not (datosInsertoDatos[0] and datosInsertoDatos[1] and datosInsertoDatos[2] and datosInsertoDatos[3] and datosInsertoDatos[4] and datosInsertoDatos[6] and datosInsertoDatos[7]):
            messagebox.showinfo("Error","Complete los campos vacios",parent=newWindow)    
        elif color in coloresAuto and contadorDigitos==3 and contadorLetras==3:
            if (datosInsertoDatos[0] and datosInsertoDatos[1] and datosInsertoDatos[2] and datosInsertoDatos[3] and datosInsertoDatos[4] and datosInsertoDatos[5] and datosInsertoDatos[6] and datosInsertoDatos[7]):
                miCursor.execute("INSERT INTO movimientos VALUES(:patente,:marca,:modelo,:color,:fechaYhora,:movimiento,:entrada,:salida)",
                {'patente':patenteGarage.get(),
                    'marca':marcaGarage.get(),
                    'modelo':modeloGarage.get(),
                    'color':colorGarage.get(),
                    'fechaYhora':date_time,
                    'movimiento':movimientoGarage.get(),
                    'entrada':entradaAlGarage.get(),
                    'salida':salidaAlGarage.get()
                    })
                #nuevo.write(str(datos))
                messagebox.showinfo("BBDD","Registro insertado con exito")
                patenteGarage.set("")
                marcaGarage.set("")
                modeloGarage.set("")
                colorGarage.set("")
                movimientoGarage.set("")
                entradaAlGarage.set("")
                salidaAlGarage.set("")
                miConexion.commit()
        if color not in coloresAuto and color !="":
            boolValidoEntradasalida=False
            labelAvisoMalColor=tk.Label(newWindow,text="Color incorrecto o invalido",font="Times 15 bold")
            labelAvisoMalColor.grid(padx=460,pady=240,row=0,column=0,sticky="WN")
            labelAvisoMalColor.after(6000, labelAvisoMalColor.grid_forget)
            messagebox.showinfo("Error","Color incorrecto")
#------

#-'movimiento':movimientoGarage.get(),
      
        # Result from count matches with result from len()
        #result = datosDos.count(datosDos[0]) == len(datosDos)
        #if (datos):
        #    messagebox.showinfo("Aviso","Algunos elementos no pueden coincidir")
    #         patenteGarage.set("")
    #         marcaGarage.set("")
    #         modeloGarage.set("")
    #         colorGarage.set("")
    #         entradaAlGarage.set("")
    #        salidaAlGarage.set("") 
            #for stringMovimiento in movimientoGarage.get():
            #    print(stringMovimiento,end="")
        
        #if movimientoGarage.get().lower() !="pago" or movimientoGarage.get().lower()!="abono" or movimientoGarage.get().lower()!="no pago" and movimientoGarage.get().lower()!="no abono":
        #    messagebox.showinfo("Error","El movimiento debe decir pago/abono o no pago/abono")
        #    labelAvisoPagoUno=tk.Label(newWindow,text="El movimiento debe decir pago/abono o no pago/abono",font="Times 13")
          #  labelAvisoPagoUno.grid(padx=400,pady=700,row=0,column=0,sticky="WN")
         #   labelAvisoPagoUno.after(9000, labelAvisoPagoUno.grid_forget)
        #else:



#-------------------------------------------------       
def buscoAuto():
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()   
    miCursor.execute("SELECT patente FROM movimientos WHERE patente = 'patenteGarage.get()")
    #if micursor.fetchone():
    #    botonEntrada=tk.Button()
    #    botonEntrada.grid(padx=430,pady=510,row=0,column=0,sticky="WN")
    #    botonEntrada.config("the car is enter: ")

#-----

buscoPatente=True        
def buscar():
    root.withdraw()   
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()    
    miCursor.execute("SELECT * FROM movimientos WHERE patente=?",[patenteGarage.get()])
    myResult = miCursor.fetchall()  
    #myResult = miCursor#con o sin fetchall es lo mismo 
    #botonEntrada=tk.Button(newWindow,text="|_ENTRA|",font="Times 14 bold",command=insertoDatos)
    nuevo=open("Garage.csv","w")
    #global adminNoAdmin
    #datos=[patenteGarage.get()]
    pago="pago"
    noPago="no pago"
    stringPago=pago.lower()
    stringNoPago=noPago.lower()

    fechaActual = datetime.now() # fecha de ingresar el dato
    date_time = fechaActual.strftime("%m/%d/%Y, %H:%M:%S")
    #-print("date and time:",date_time)  

    if patenteGarage.get()=="":
        messagebox.showinfo("Aviso","Debe introducir patente para ver sus registros",parent=newWindowDos)
        patenteGarage.set("")
        colorGarage.set("")
        modeloGarage.set("")
        marcaGarage.set("")
        movimientoGarage.set("")
        entradaAlGarage.set("")
        salidaAlGarage.set("")
    else:
        pass

    datosTotales=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]
    
    #datosPatente="".join(datoParaBuscarPatente)    
    
    datosPatente="".join(datosTotales[0])    
    #if all(datosTotales):
    #    messagebox.showinfo("Aviso","Algunos elementos no pueden coincidir")

    s = ','.join(str(x) for x in myResult)#La lista con tupla anidada ahora es solo tupla
    #print(s)#es ahora tupla
    sSinComa=s.replace(",","")
    print(sSinComa)

    #labelEstaPatente=tk.Label(newWindow)   
    #labelNoEstaPatente=tk.Label(newWindow)
    varEstaONoPatente = tk.StringVar()
    #varNoEstaPatente = tk.StringVar()
    labelEstaONoPatente=tk.Label(newWindow,font="Times 20 bold",textvariable=varEstaONoPatente)
    labelEstaONoPatente.grid(padx=450,pady=180,row=0,column=0,sticky="WN")        
    #labelNoEstaPatente=tk.Label(newWindow,font="Times 20 bold",textvariable=varNoEstaPatente)
    #labelNoEstaPatente.grid(padx=450,pady=180,row=0,column=0,sticky="WN")        
    if datosPatente in sSinComa:
        varEstaONoPatente.set("El auto esta adentro")
        labelEstaONoPatente.after(2500, labelEstaONoPatente.grid_forget)
        botonQueActivaPagado['state']=tk.ACTIVE
        pagadoNoBoton['state']=tk.ACTIVE
        pagadoSiBoton['state']=tk.ACTIVE

        buscoPatente=True
        for usuario in myResult:
            marcaGarage.set(usuario[1])
            modeloGarage.set(usuario[2])
            colorGarage.set(usuario[3])
            movimientoGarage.set(usuario[5])
            entradaAlGarage.set(usuario[6])
            salidaAlGarage.set(usuario[7])

    elif datosPatente not in sSinComa:
        buscoPatente=False
        varEstaONoPatente.set("No esta esa patente")
        labelEstaONoPatente.after(2500, labelEstaONoPatente.grid_forget)
        botonEntrada['state']=tk.ACTIVE
        botonEditar['state']=tk.DISABLED
        pagadoNoBoton['state']=tk.DISABLED
        pagadoSiBoton['state']=tk.DISABLED
        marcaGarage.set("")
        modeloGarage.set("")
        colorGarage.set("")
        movimientoGarage.set("")
        entradaAlGarage.set("")
        salidaAlGarage.set("")


#----------------------------------------------
ponePatenteParaBuscarla=tk.Label(newWindowDos,text="Introduce patente para buscarla con sus datos",fg="brown",font="Times 20 bold")
ponePatenteParaBuscarla.grid(column=0,sticky="WN",padx=110,pady=20)

def buscarVentanaNoAdmin():
    #root.withdraw()
    miConexion=sqlite3.connect("Garage.db")
    nuevo=open("Garage.csv","w")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM movimientos WHERE patente=?",[patenteGarage.get()])
    datosInsertoDatosDos=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get()]
    myResult = miCursor.fetchall()    
    datosPatente="".join(patenteGarage.get())
    
    if datosPatente=="":
        messagebox.showinfo("Aviso","Patente vacia")
        marcaGarage.set("")
        modeloGarage.set("")
        colorGarage.set("")
        movimientoGarage.set("")
        entradaAlGarage.set("")
        salidaAlGarage.set("")
        
    patenteIgual=True
    contadorDigitos=0
    contadorLetras=0
    if patenteGarage.get():
        for c in patenteGarage.get():
            if c in ("0123456789"):
                contadorDigitos+=1
            if contadorDigitos>3:
                patenteIgual=False
            if contadorDigitos<=2:
                patenteIgual=False
            elif contadorDigitos==3:
                patenteIgual=True
    #-
    if datosPatente:
        for cc in datosPatente:
            if cc not in ("0123456789"):
                contadorLetras+=1
            if contadorLetras>3:
                patenteIgual=False
            if contadorLetras<=2:
                patenteIgual=False
            elif contadorLetras==3:
                patenteIgual=True
        if patenteIgual==False:
            messagebox.showinfo("Aviso","Debe tener 3 numeros y 3 letras")
    
        labelEntradaBuscandoPatenteDos=tk.Label(newWindowDos,text="No esta esa patente",font="Times 25 bold")
        labelEntradaBuscandoPatenteDos.grid(padx=450,pady=180,row=0,column=0,sticky="WN")
        labelEntradaBuscandoPatenteDos.after(3000, labelEntradaBuscandoPatenteDos.grid_forget)
        marcaGarage.set("")
        modeloGarage.set("")
        colorGarage.set("")        
    pasoATupla = ','.join(str(x) for x in myResult)#La lista con tupla anidada ahora es solo tupla
    #print(s)#es ahora tupla
           #labelEntradaBuscandoPatente=tk.Label(newWindow,text="The car is enter",font="Times 25 bold")
    convertidoATupla=pasoATupla.replace(",","")
    #print(convertidoATupla)
    
    if datosPatente in convertidoATupla:
        labelEntradaBuscandoPatente=tk.Label(newWindow,text="El auto esta adentro",font="Times 25 bold")
        labelEntradaBuscandoPatenteDos=tk.Label(newWindowDos,text="El auto esta adentro",font="Times 25 bold")  
        labelEntradaBuscandoPatente.grid(padx=450,pady=180,row=0,column=0,sticky="WN")
        labelEntradaBuscandoPatente.after(3000, labelEntradaBuscandoPatente.grid_forget)
        labelEntradaBuscandoPatenteDos.grid(padx=450,pady=180,row=0,column=0,sticky="WN")
        labelEntradaBuscandoPatenteDos.after(3000, labelEntradaBuscandoPatenteDos.grid_forget)
        botonQueActivaPagado['state']=tk.ACTIVE
        botonEntrada['state']=tk.DISABLED   
        for usuario in myResult:
            marcaGarage.set(usuario[1])
            modeloGarage.set(usuario[2])
            colorGarage.set(usuario[3])
            buscoPatente=True
            
#---------
eliminarBool=True
def eliminar():
    eliminarBool=True
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()
    nuevo=open("Garage.csv","w")
    
    global adminNoAdmin
    datosTotales=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]    


    if salidaAlGarage.get()!="si" or salidaAlGarage.get()!="Si" and entradaAlGarage.get().lower()!="no" :
        messagebox.showinfo("Aviso","Debe escribir si/Si para borrar 1 o mas registros")
        labelSalidaMensaje.after(3000, labelSalidaMensaje.grid_forget)
        eliminarBool=True
    else:
        eliminarBool=False
    datos=[salidaAlGarage.get()]
    #datosDos=[marcaGarage.get()]
    try: 
        datosSalida="".join(datos)
        #datosMarca="".join(datosDos)
        #if salidaAlgarage.get()==datosSalida:
        if salidaAlGarage.get().lower()=='si':
            miCursor.execute("UPDATE movimientos SET salida=?WHERE patente=?",[datosTotales[7]] +[datosTotales[0]] )
            print("valor editado")
            miConexion.commit()
            pass                 
        if salidaAlGarage.get().lower()=="si" and entradaAlGarage.get().lower()=="no" :       
            if datosSalida== salidaAlGarage.get():
            #miCursor.execute("DELETE FROM movimientos WHERE salida=?",[datosSalida])            
            #miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" +miId.get())
                miCursor.execute("DELETE FROM movimientos WHERE salida=?",[datosTotales[7]])            

        #if datosMarca== marcaGarage.get():
        #    miCursor.execute("DELETE FROM movimientos WHERE marca=?",(datosDos))            

        #miCursor.execute("DELETE FROM movimientos WHERE patente='patenteGarage.get()'")
         #print(patenteGarage.get())
                miConexion.commit()
                #miConexion.close()
                messagebox.showinfo("BBDD","Registro borrado con exito")
                patenteGarage.set("")
                marcaGarage.set("")
                modeloGarage.set("")
                colorGarage.set("")
                movimientoGarage.set("")
                entradaAlGarage.set("")
                #nuevo.write(str(datosSalida))
                salidaAlGarage.set("")

    except:
        messagebox.showinfo("Aviso","Ese registro no se encuentra o no existe")
#------------
def siEsDistintoSiNoEntradaSalida():
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()
    if entradaAlGarage.get().lower()!="si" and entradaAlGarage.get().lower()!="no" :
        entradaAlGarage.set("")
    if salidaAlGarage.get().lower()!="si" and salidaAlGarage.get().lower()!="no":
        salidaAlGarage.set("")

#-

def exportoBaseDatosNewWindow():
#https://datatofish.com/export-sql-table-to-csv-python/
    nuevo=open("Garage.csv","w",newline="")
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM movimientos;")
    myResult = miCursor.fetchall()    
       
    campos=["Patente","Marca","Modelo","Color","Fecha y hora","Movimiento","Entrada","Salida"]
    writer = csv.writer(nuevo,delimiter=";")
    writer.writerow(campos)  
    writer.writerows(myResult)  

#-----------Boton importar y exportar datos----------------

exportarDatosButton=tk.Button(newWindow,font="Times 14",width=21,border=5,text="|_EXPORTAR DATOS_||",command=exportoBaseDatosNewWindow)
exportarDatosButton.grid(row=0,column=0,sticky="WN",pady=730,padx=500)   
exportarDatosLabel=tk.Label(newWindow,font="Times 11")
exportarDatosLabel.grid(column=0,row=0,sticky="WN",padx=420,pady=720)    

importarDatosButton=tk.Button(newWindow,font="Times 14",width=21,border=5,text="|_EXPORTAR DATOS_||",command=exportoBaseDatosNewWindow)
exportarDatosButton.grid(row=0,column=0,sticky="WN",pady=730,padx=500)   
exportarDatosLabel=tk.Label(newWindow,font="Times 11")
exportarDatosLabel.grid(column=0,row=0,sticky="WN",padx=420,pady=720) 

#----
def importoBaseDatosRoot():
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()
    for row in miCursor.execute('SELECT * FROM movimientos;'):
        print(row)
    miConexion.close()

#-----

importarDatosLabel=tk.Label(newWindow,font="Times 11")
importarDatosLabel.grid(column=0,row=0,sticky="WN",padx=10,pady=720)
importarDatosButton=tk.Button(newWindow,font="Times 14",width=21,border=5,text="|_IMPORTAR DATOS_||",command=importoBaseDatosRoot)
importarDatosButton.grid(row=0,column=0,sticky="WN",pady=730,padx=20) 
#----
def noPago():
    pongoPagado="Pagado"
    pongoNoPagado="No pagado"
    global botonQueActivaPagado
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()    
    nuevo=open("Garage.csv","w")
    pagadoNoBoton=tk.Button(newWindow)
    
    datosPagar=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]     
    labelPagarTrue=tk.Label(root,font="Times 13")
    labelPagarTrue.grid(column=0,row=0,sticky="WN",padx=450,pady=720) 
    insertoMovimiento=movimientoGarage.get()
    if movimientoGarage.get()=="" or movimientoGarage.get()!="":
        miCursor.execute("UPDATE movimientos SET movimiento='No pagado' WHERE patente=?",[datosPagar[0]])
        miConexion.commit()
        pagadoNoBoton.configure(bg="lightgreen")
        pagadoSiBoton.configure(bg="SystemButtonFace")
        messagebox.showinfo("Aviso","Figura no pagado")   

#----
def siPago():
    pongoPagado="Pagado"
    pongoNoPagado="No pagado"
    global botonQueActivaPagado
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()    
    nuevo=open("Garage.csv","w")
    pagadoNoBoton=tk.Button(newWindow)
    datosPagar=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]     
    
    labelPagarTrue=tk.Label(root,font="Times 13")
    labelPagarTrue.grid(column=0,row=0,sticky="WN",padx=450,pady=720) 
    insertoMovimiento=movimientoGarage.get()
    
    if movimientoGarage.get()=="" or movimientoGarage.get()!="":
        miCursor.execute("UPDATE movimientos SET movimiento='Pagado' WHERE patente=?",[datosPagar[0]])
        miConexion.commit()
        pagadoNoBoton.configure(bg="SystemButtonFace")
        pagadoSiBoton.configure(bg="lightgreen")
        messagebox.showinfo("Aviso","Figura Pagado")   

#-------------
def pagar():
    pongoPagado="Pagado"
    pongoNoPagado="No pagado"
    global botonQueActivaPagado
    miConexion=sqlite3.connect("Garage.db")
    miCursor=miConexion.cursor()    
    nuevo=open("Garage.csv","w")
    pagadoNoBoton=tk.Button(newWindow)
    datosPagar=[patenteGarage.get(),marcaGarage.get(),modeloGarage.get(),colorGarage.get(),date_time,movimientoGarage.get(),entradaAlGarage.get(),salidaAlGarage.get()]     
    
    labelPagarTrue=tk.Label(root,font="Times 13")
    labelPagarTrue.grid(column=0,row=0,sticky="WN",padx=450,pady=720) 
    insertoMovimiento=movimientoGarage.get()
    #if botonQueActivaPagado.invoke():
    #- Sino pago, ahora figura pagado
    if movimientoGarage.get()=="" or movimientoGarage.get()!="":
        miCursor.execute("UPDATE movimientos SET movimiento='Pagado' WHERE patente=?",[datosPagar[0]])
        miConexion.commit()        

#----------------

botonQueActivaPagado=tk.Button(newWindow,font="Times 14",text="|_PAGAR_||",command= pagar)
#botonQueActivaPagado=tk.Button(newWindow,font="Times 14",text="|_PAGAR_||",command=pagar,command= lambda t= "Button-2 Clicked": pagar(t))
botonQueActivaPagado.grid(row=0,column=0,sticky="WN",pady=620,padx=620)
botonQueActivaPagado['state']=tk.DISABLED

pagadoSiBoton=tk.Button(newWindow,font="Times 14 bold",text="[SI]",state=tk.DISABLED,command= siPago)
pagadoSiBoton.grid(row=0,column=0,sticky="WN",pady=630,padx=100)
              
pagadoNoBoton=tk.Button(newWindow,font="Times 14 bold",text="[No]",state=tk.DISABLED,command= noPago)
pagadoNoBoton.grid(row=0,column=0,sticky="WN",pady=630,padx=160)

botonEntrada=tk.Button(newWindow,text="|_ENTRA|",font="Times 14 bold",command=insertoDatos)
botonEntrada.grid(padx=560,pady=510,row=0,column=0,sticky="WN")       
botonEntrada['state']=tk.DISABLED

botonEntrada=tk.Button(newWindowDos,text="|_ENTRA|",font="Times 14 bold",command=insertoDatos)


labelActivaPagadoONo=tk.Label(newWindow,font="Times 14",text="Pon pagado o no pagado")
labelActivaPagadoONo.grid(column=0,row=0,sticky="WN",padx=400,pady=580)
             
#-----------Boton inicia sesion----------------
btnIniciaSesion=tk.Button(root,text = 'Inicia sesión',height=2,font="Times 15",fg = 'black',
        bg = "yellow",bd=5,command=ventanaDos)
btnIniciaSesion.grid(row=0,column=0,pady=200,padx=150,sticky="NW")
btnIniciaSesion.config(height=1,width=8)
#----
botonEditar=tk.Button(newWindow,font="Times 14 bold",text="Editar",command=editar)
botonEditar.grid(row=0,column=0,sticky="WN",pady=400,padx=520)  
#-
root.mainloop()


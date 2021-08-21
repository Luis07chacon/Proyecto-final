import tkinter as tk
import time
from tkinter import *
import os
from tkinter import messagebox as Messagebox

def ventana_inicio():  
    global ventanaprincipal
    ventanaprincipal=tk.Tk()
    ventanaprincipal.config(bg="#213241")
    ventanaprincipal.geometry("400x350")
    ventanaprincipal.resizable(0,0)
    ventanaprincipal.title("ATM Banco de Puriscal")
    ventanaprincipal.iconbitmap("C:\\Users\\Luis Miguel\\OneDrive\\Escritorio\\iconoatm_wLP_icon.ico")
    tiempo_label=tk.Label(text=time.strftime('%I:%M %p'),font=("ornitron",12),fg="black",bg="#E4E1DF",pady=5,padx=5)
    tiempo_label.place(x=319,y=317)
    print(tiempo_label["text"])
    visa_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\visa.png")
    visa_label = Label(image=visa_photo)
    visa_label.place(x=0,y=322)
    visa_label.image = visa_photo
    mastercard_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\mastercard.png")
    mastercard_label = Label(image=mastercard_photo)
    mastercard_label.place(x=28,y=322)
    mastercard_label.image = mastercard_photo
    american_express_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\american-express.png")
    american_express_label = Label(image=american_express_photo)
    american_express_label.place(x=55,y=322)
    american_express_label.image = american_express_photo
    Label(text="Seleccione la opción", bg="#63A791", width="300", height="2", font=("Cambria")).pack()
    Label(bg="#213241").pack()
    Button(text="Iniciar sesión",font=("Cambria"), height="1", width="15", bg="#63A791", command=login).pack()
    Label(bg="#213241").pack()
    Button(text="Registrarse", font=("Cambria"),height="1", width="15", bg="#63A791", command=registro).pack() 
    Label(bg="#213241").pack()
    Button(ventanaprincipal,text="Ayuda",font=("Cambria"),height="1", width="15",bg="#63A791",command=help).pack()
    Label(bg="#213241").pack()
    Button(ventanaprincipal,text="Salir",font=("Cambria"),height="1", width="15",bg="#63A791").pack()
    
    def update_clock():
        time_now=time.strftime('%I:%M %p')
        if tiempo_label["text"]!=time_now:
            tiempo_label["text"] = time_now
        ventanaprincipal.after(1000,update_clock)
    
    update_clock()
    ventanaprincipal.mainloop()

def registro():
    global ventanaregistro
    ventanaregistro = Toplevel(ventanaprincipal)
    ventanaregistro.config(bg="#213241")
    ventanaregistro.title("Ventana de Registro")
    ventanaregistro.geometry("400x350")
    ventanaregistro.iconbitmap("C:\\Users\\Luis Miguel\\OneDrive\\Escritorio\\iconoatm_wLP_icon.ico")
    tiempo_label=tk.Label(ventanaregistro,text=time.strftime('%I:%M %p'),font=("ornitron",12),fg="black",bg="#E4E1DF",pady=5,padx=5)
    tiempo_label.place(x=319,y=317)
    print(tiempo_label["text"])
    visa_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\visa.png")
    visa_label = Label(ventanaregistro,image=visa_photo)
    visa_label.place(x=0,y=322)
    visa_label.image = visa_photo
    mastercard_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\mastercard.png")
    mastercard_label = Label(ventanaregistro,image=mastercard_photo)
    mastercard_label.place(x=28,y=322)
    mastercard_label.image = mastercard_photo
    american_express_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\american-express.png")
    american_express_label = Label(ventanaregistro,image=american_express_photo)
    american_express_label.place(x=55,y=322)
    american_express_label.image = american_express_photo
    
    def update_clock():
        time_now=time.strftime('%I:%M %p')
        if tiempo_label["text"]!=time_now:
            tiempo_label["text"] = time_now
        ventanaprincipal.after(1000,update_clock)
    
    update_clock()

    global nombreusuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombreusuario = StringVar() 
    clave = StringVar()

    Label(ventanaregistro, text="Introduzca datos",width="300", height="2", font=("Cambria"), bg="#63A791").pack()
    Label(ventanaregistro, bg="#213241").pack()
    etiqueta_nombre = Label(ventanaregistro, text="Nombre de usuario: ")
    etiqueta_nombre.place(x=5,y=70)
    entrada_nombre = Entry(ventanaregistro, textvariable=nombreusuario) 
    entrada_nombre.place(x=121,y=71)
    etiqueta_clave = Label(ventanaregistro, text="Contraseña: ")
    etiqueta_clave.place(x=5,y=120)
    entrada_clave = Entry(ventanaregistro, textvariable=clave, show='*') 
    entrada_clave.place(x=79,y=121)
    Button(ventanaregistro, text="Registrarse", width=10, height=1, bg="white", command = registro_usuario).place(x=115,y=175) 



def login():
    global ventanalogin
    ventanalogin = Toplevel(ventanaprincipal)
    ventanalogin.title("Ventana de Inicio de Sesión")
    ventanalogin.geometry("400x350")
    ventanalogin.config(bg="#213241")
    Label(ventanalogin, text="Introduzca su nombre de usuario y contraseña",bg="#63A791",width="300", height="2").pack()
    Label(ventanalogin,bg="#213241").pack()
    ventanalogin.iconbitmap("C:\\Users\\Luis Miguel\\OneDrive\\Escritorio\\iconoatm_wLP_icon.ico")
    tiempo_label=tk.Label(ventanalogin,text=time.strftime('%I:%M %p'),font=("ornitron",12),fg="black",bg="#E4E1DF",pady=5,padx=5)
    tiempo_label.place(x=319,y=317)
    print(tiempo_label["text"])
    visa_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\visa.png")
    visa_label = Label(ventanalogin,image=visa_photo)
    visa_label.place(x=0,y=322)
    visa_label.image = visa_photo
    mastercard_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\mastercard.png")
    mastercard_label = Label(ventanalogin,image=mastercard_photo)
    mastercard_label.place(x=28,y=322)
    mastercard_label.image = mastercard_photo
    american_express_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\american-express.png")
    american_express_label = Label(ventanalogin,image=american_express_photo)
    american_express_label.place(x=55,y=322)
    american_express_label.image = american_express_photo
    
    def update_clock():
        time_now=time.strftime('%I:%M %p')
        if tiempo_label["text"]!=time_now:
            tiempo_label["text"] = time_now
        ventanaprincipal.after(1000,update_clock)
    
    update_clock()
    
    global verificausuario
    global verificaclave

    verificausuario = StringVar()
    verificaclave = StringVar()

    global entradalogin_usuario
    global entradalogin_clave

    Label(ventanalogin, text="Nombre usuario: ").place(x=5,y=70)
    entradalogin_usuario = Entry(ventanalogin, textvariable=verificausuario)
    entradalogin_usuario.place(x=105,y=71)
    Label(ventanalogin,bg="#FF5733")
    Label(ventanalogin, text="Contraseña: ").place(x=5,y=120)
    entradalogin_clave = Entry(ventanalogin, textvariable=verificaclave, show= '*')
    entradalogin_clave.place(x=79,y=121)
    Label(ventanalogin,bg="#FF5733")
    Button(ventanalogin, text="Iniciar sesión", width=10, height=1, command = verificalogin).place(x=115,y=175) 



def verificalogin():
    usuario1 = verificausuario.get()
    clave1 = verificaclave.get()
    entradalogin_usuario.delete(0, END) 
    entradalogin_clave.delete(0, END) 

    archivos = os.listdir() 

    if usuario1 in archivos:
        archivo1 = open(usuario1, "r")
        verifica = archivo1.read().splitlines() 
        if clave1 in verifica:
            exito_login()

        else:
            no_clave() 

    else:
        no_usuario() 


def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventanalogin)
    ventana_exito.title("Exitoso")
    ventana_exito.geometry("150x100")
    ventana_exito.config(bg="#213241")
    ventana_exito.iconbitmap("C:\\Users\\Luis Miguel\\OneDrive\\Escritorio\\iconoatm_wLP_icon.ico")
    Label(ventana_exito, text="Inicio exitoso").pack()
    Label(ventana_exito,bg="#213241").pack
    Button(ventana_exito, text="OK", command=borrarexito_login).pack()


def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventanalogin)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña Incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrarno_clave).pack() 
    

def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventanalogin)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("250x200")
    Label(ventana_no_usuario,bg="#213241")
    Label(ventana_no_usuario, text="Usuario Incorrecto").pack()
    Button(ventana_no_usuario, text="Intentar de nuevo", command=borrarno_usuario).place(x=175,y=100) 

saldoactual = 1000
dinero = 0

def borrarexito_login():
        global ventanamenu
        ventanamenu = Toplevel(ventanalogin)
        ventanamenu.title("Menu de transacciones")
        ventanamenu.geometry("650x550")
        ventanamenu.resizable(0,0)
        ventanamenu.config(bg="#213241")
        Label(ventanamenu,text="Menu de transacciones",font=("Cambria", 14),bg="#63A791",fg="black",width="500",height="2").pack()
        Label(ventanamenu,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanamenu,text="Consulta de Saldo",font=("Cambria", 14),bg="#63A791",command=consultasaldo).pack()
        Label(ventanamenu,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanamenu,text="Retirar dinero",font=("Cambria", 14),bg="#63A791",command=retirardinero).pack()
        Label(ventanamenu,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanamenu,text="Ingresar dinero",font=("Cambria", 14),bg="#63A791",command=ingresardinero).pack()
        Label(ventanamenu,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanamenu,text="Cambio de moneda",font=("Cambria", 14),bg="#63A791").pack()
        Label(ventanamenu,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanamenu,text="Fondo de ahorro",font=("Cambria", 14),bg="#63A791").pack()
        Label(ventanamenu,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanamenu,text="Salir",font=("Cambria", 14),bg="#63A791",command=exit).pack()
        ventanamenu.iconbitmap("C:\\Users\\Luis Miguel\\OneDrive\\Escritorio\\iconoatm_wLP_icon.ico")
        tiempo_label=tk.Label(ventanamenu,text=time.strftime('%I:%M %p'),font=("ornitron",12),fg="black",bg="#E4E1DF",pady=5,padx=5)
        tiempo_label.place(x=569,y=517)
        print(tiempo_label["text"])
        visa_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\visa.png")
        visa_label = Label(ventanamenu,image=visa_photo)
        visa_label.place(x=0,y=523)
        visa_label.image = visa_photo
        mastercard_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\mastercard.png")
        mastercard_label = Label(ventanamenu,image=mastercard_photo)
        mastercard_label.place(x=28,y=523)
        mastercard_label.image = mastercard_photo
        american_express_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\american-express.png")
        american_express_label = Label(ventanamenu,image=american_express_photo)
        american_express_label.place(x=55,y=523)
        american_express_label.image = american_express_photo
        
        def update_clock():
            time_now=time.strftime('%I:%M %p')
            if tiempo_label["text"]!=time_now:
                tiempo_label["text"] = time_now
            ventanaprincipal.after(1000,update_clock)
    
            update_clock()

def consultasaldo():
        global saldoactual
        Messagebox.showinfo(title="ATM Banco de Puriscal",message="El saldo de su cuenta es de: ₡" + str(saldoactual) + " Colones")

def operacionretiro():
        global saldoactual
        global dinero
        print(saldoactual)
        if (dinero.get() <= saldoactual):
            saldoNuevo = (saldoactual - dinero.get())
            saldoactual = saldoNuevo
            Messagebox.showinfo(title="ATM Banco de Puriscal",message="Retiro exitoso.")
        else:
            Messagebox.showinfo(title="ATM Banco de Puriscal",message="Saldo insuficiente.")

def operacioningreso():
        global saldoactual
        global dineroi
        print(saldoactual)
        saldoNuevo = (saldoactual + dineroi.get())
        saldoactual = saldoNuevo
        Messagebox.showinfo(title="ATM Banco de Puriscal",message="Ingreso exitoso.")

def retirardinero():
        global dinero
        ventanaretiro = Toplevel(ventanamenu)
        ventanaretiro.title("ATM Banco de Puriscal")
        ventanaretiro.geometry("400x200")
        ventanaretiro.resizable(0,0)
        ventanaretiro.config(bg="#213241")
        ventanaretiro.iconbitmap("C:\\Users\\Luis Miguel\\OneDrive\\Escritorio\\iconoatm_wLP_icon.ico")
        tiempo_label=tk.Label(ventanaretiro,text=time.strftime('%I:%M %p'),font=("ornitron",12),fg="black",bg="#E4E1DF",pady=5,padx=5)
        tiempo_label.place(x=319,y=167)
        print(tiempo_label["text"])
        visa_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\visa.png")
        visa_label = Label(ventanaretiro,image=visa_photo)
        visa_label.place(x=0,y=173)
        visa_label.image = visa_photo
        mastercard_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\mastercard.png")
        mastercard_label = Label(ventanaretiro,image=mastercard_photo)
        mastercard_label.place(x=28,y=173)
        mastercard_label.image = mastercard_photo
        american_express_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\american-express.png")
        american_express_label = Label(ventanaretiro,image=american_express_photo)
        american_express_label.place(x=55,y=173)
        american_express_label.image = american_express_photo
        Label(ventanaretiro,text="Retiro de dinero",font=("Cambria", 14),bg="#FF5733",fg="black",width="500",height="1").pack()
        Label(ventanaretiro,text="",bg="#213241",width="500",height="1").pack()
        dinero = IntVar()
        Entry(ventanaretiro,textvariable=dinero).pack()
        print(dinero.get())
        Label(ventanaretiro,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanaretiro,text="Retirar",font=("Cambria", 14),bg="#FF5733",command=lambda:[operacionretiro()]).pack()

        def update_clock():
            time_now=time.strftime('%I:%M %p')
            if tiempo_label["text"]!=time_now:
                tiempo_label["text"] = time_now
            ventanaprincipal.after(1000,update_clock)
    
            update_clock()

def ingresardinero():
        global dineroi
        ventanaingreso = Toplevel(ventanamenu)
        ventanaingreso.title("ATM Banco de Puriscal")
        ventanaingreso.geometry("400x200")
        ventanaingreso.resizable(0,0)
        ventanaingreso.config(bg="#213241")
        ventanaingreso.iconbitmap("C:\\Users\\Luis Miguel\\OneDrive\\Escritorio\\iconoatm_wLP_icon.ico")
        tiempo_label=tk.Label(ventanaingreso,text=time.strftime('%I:%M %p'),font=("ornitron",12),fg="black",bg="#E4E1DF",pady=5,padx=5)
        tiempo_label.place(x=319,y=167)
        print(tiempo_label["text"])
        visa_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\visa.png")
        visa_label = Label(ventanaingreso,image=visa_photo)
        visa_label.place(x=0,y=173)
        visa_label.image = visa_photo
        mastercard_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\mastercard.png")
        mastercard_label = Label(ventanaingreso,image=mastercard_photo)
        mastercard_label.place(x=28,y=173)
        mastercard_label.image = mastercard_photo
        american_express_photo = PhotoImage(file=R"C:\Users\Luis Miguel\OneDrive\Escritorio\american-express.png")
        american_express_label = Label(ventanaingreso,image=american_express_photo)
        american_express_label.place(x=55,y=173)
        american_express_label.image = american_express_photo
        Label(ventanaingreso,text="Ingreso de dinero",font=("Cambria", 14),bg="#FF5733",fg="black",width="500",height="1").pack()
        Label(ventanaingreso,text="",bg="#213241",width="500",height="1").pack()
        dineroi = IntVar()
        Entry(ventanaingreso,textvariable=dineroi).pack()
        print(dineroi.get())
        Label(ventanaingreso,text="",bg="#213241",width="500",height="1").pack()
        Button(ventanaingreso,text="Ingresar",font=("Cambria", 14),bg="#FF5733",command=lambda:[operacioningreso()]).pack()
    
        def update_clock():
            time_now=time.strftime('%I:%M %p')
            if tiempo_label["text"]!=time_now:
                tiempo_label["text"] = time_now
            ventanaprincipal.after(1000,update_clock)
    
            update_clock()

def borrarno_clave():
    ventana_no_clave.destroy()


def borrarno_usuario():
    ventana_no_usuario.destroy()


def registro_usuario():

    usuario_info = nombreusuario.get()
    clave_info = clave.get()

    file = open(usuario_info, "w") 
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()

    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)

    Label(ventanaregistro, text="Registro completado con éxito", fg="green", font=("Cambria", 11)).place(x=55,y=205) 


ventana_inicio()          



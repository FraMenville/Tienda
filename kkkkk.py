import tkinter as tk
import pymysql
from tkinter import messagebox

# Funciones para los botones
#conecion mysql
bod=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tienda"
    )

def iniciar_sesion(entradal1,entradal2,bod):
    mi_cursor_a = bod.cursor()
    usuario = entradal1.get()
    contraseña = entradal2.get()
    enlace = "SELECT * FROM `admin_window` WHERE Usuario = %s AND contraseña = %s"
    mi_cursor_a.execute(enlace,(usuario, contraseña))
    conexion = mi_cursor_a.fetchone()
    if conexion:
        bod.commit()
        messagebox.showinfo("Datos correctos", "¡Inicio de sesion exitoso!")
        #iniciar_admin(ae1,e2)
    else:
        messagebox.showerror("Error de datos","Usuario o contraseña incorrecta")

def guardar(entrya2,entrya3,entrya4,bod,iniciar_rastreo):
    mi_cursor = bod.cursor()
    articulo = entrya2.get()
    precio = entrya3.get()
    descripcion = entrya4.get('1.0','end')
    mensaje =f"Articulo: {articulo},Precio: {precio}, Descripcion: {descripcion}"
    sql_save = "INSERT INTO `productos1`(`Articulo`, `Precio`, `Descripcion`) VALUES ('{}','{}','{}')".format(articulo,precio,descripcion)
    print(sql_save)
    mi_cursor.execute(sql_save)
    bod.commit()
    messagebox.showinfo(mensaje,"El producto a sido registrado")

def buscar(entradau1,entradau2,entradau3,descripcioniu):
    mi_cursor = bod.cursor()
    mensaje = "Error"
    id = entradau1.get()
    sql = f"select * from `productos1` where Id = '{id}'"
    mi_cursor.execute(sql)
    bod.commit()
    #messagebox.showinfo(mensaje,"El producto a sido registrado")
    result = mi_cursor.fetchall()
    for i in result:
        #Id_2 = i[0]
        Articulo_b = i[1]
        Precio_b = i[2]
        Descripcion_b = i[3]
        
    #entradau1.insert(0, Id_2)
    #entradau1.config(width=len(Id_2))
    entradau2.insert(0, Articulo_b)
    #entradau2.config(width=len(Articulo_b))
    entradau3.insert(0, Precio_b)
    #entradau3.config(width=len(Precio_b))
    descripcioniu.insert(0, Descripcion_b)
    descripcioniu.config(width=len(Descripcion_b))

def mensaje_box():
    mensaje_u = ""
    messagebox.showinfo(mensaje_u,"El producto que a pedido esta en proceso de envio, espere 3 dias habiles")
    
    

#sub ventana de Admin
def iniciar_rastreo():
    ventana_admin = tk.Toplevel(root)
    ventana_admin.title("Administrador")
    ventana_admin.geometry("600x450")
    ventana_admin.configure(bg="lightblue")
    #label_id = tk.Label(ventana_admin, text="ID")
    #label_id.place(x=80,y=90)
    label_articulo = tk.Label(ventana_admin, text="Artículo")
    label_articulo.place(x=50,y=120)
    label_precio = tk.Label(ventana_admin, text="Precio")
    label_precio.place(x=62,y=150)
    label_descripcion = tk.Label(ventana_admin, text="Descripción")
    label_descripcion.place(x=38,y=180)
    #entrya1 = tk.Entry(ventana_admin)
    #entrya1.place(x=110,y=90)
    entrya2 = tk.Entry(ventana_admin)
    entrya2.place(x=110,y=120)
    entrya3 = tk.Entry(ventana_admin)
    entrya3.place(x=110,y=150)
    entrya4 = tk.Text(ventana_admin, height=8, width=50)
    #entrya4.configure(height=15,width=15)
    entrya4.place(x=110,y=180)
    boton_envio = tk.Button(ventana_admin, height=5, width=10, text="Guardar", command=lambda: guardar(entrya2, entrya3, entrya4, bod, iniciar_rastreo))
    boton_envio.place(x=270,y=330)




# Funciones Admin
def iniciar_admin():
    admin_window = tk.Toplevel(root)
    admin_window.title("Ventana de Administrador")
    admin_window.geometry("600x450")
    admin_window.configure(bg="lightblue")
    etiquetal1 = tk.Label(admin_window,text="Ingrese el Usuario")
    etiquetal1.place(x=105,y=200)
    etiquetal2 = tk.Label(admin_window, text="Ingrese la Contraseña")
    etiquetal2.place(x=105,y=270)
    entradal1 = tk.Entry(admin_window)
    entradal1.place(x=250,y=200)
    entradal2 = tk.Entry(admin_window)
    entradal2.place(x=250,y=270)
    label_admin = tk.Label(admin_window)
    label_admin.configure(width=40,height=10,bg="light sea green",bd=5,text=(f"Esta es la ventada de inicio de sesion\n de administrador, si eres un usuario normal\n y entrastes por error en esta ventana se\n le pide amablemente que la cierre y vuelva\n a la ventana de usuario"))
    label_admin.pack()
    boton_init = tk.Button(admin_window, text="Siguiente", width=20, height=6, command=iniciar_rastreo)
    boton_init.place(x=250, y=350)
    # Aquí puedes agregar widgets para el inicio de sesión como administrador

def iniciar_usuario():
    usuario_window = tk.Toplevel(root)
    usuario_window.title("Ventana de Productos")
    usuario_window.geometry("600x450")
    usuario_window.configure(bg="lightblue")
    etiquetau1 = tk.Label(usuario_window,text="ID")
    etiquetau1.place(x=80,y=90)
    etiquetau2 = tk.Label(usuario_window,text="Articulo")
    etiquetau2.place(x=50,y=130)
    etiquetau3 = tk.Label(usuario_window,text="Precio")
    etiquetau3.place(x=60,y=170)
    etiquetau4 = tk.Label(usuario_window,text="Descripcion")
    etiquetau4.place(x=32,y=210)
    descripcioniu = tk.Entry(usuario_window)
    descripcioniu.place(x=110,y=210)
    entradau1 = tk.Entry(usuario_window)
    entradau1.place(x=120,y=90)
    entradau2 = tk.Entry(usuario_window)
    entradau2.place(x=120,y=130)
    entradau3 = tk.Entry(usuario_window)
    entradau3.place(x=120,y=170)
    boton_botonazo = tk.Button(usuario_window, height=2, width=8, text="Search", command=lambda:buscar(entradau1,entradau2,entradau3,descripcioniu))
    boton_botonazo.place(x=200,y=350)
    boton_compra = tk.Button(usuario_window, height=2, width=8, text="Buy", command=mensaje_box)
    boton_compra.place(x=400,y=350)


# Crear la ventana
root = tk.Tk()
root.title("Fruterias El Gordo")
root.geometry("950x650+250+40")
root.minsize(200,200)
root.configure(bg="lightblue")
imagen = tk.PhotoImage(file="Captura de pantalla (22).png")
label_root = tk.Label(root)
label_root.configure(width=40,height=10,bg="light sea green",bd=5,text="Bienvenidos a esta tienda de frutas\n la cual esta en su fase beta\n si se presenta un BUG\n presentar una queja en la administracion")
label_root.place(x=330,y=400)

#imagen
etiqueta = tk.Label(root, image=imagen)
etiqueta.place(x=330,y=100)
# Agregar un logo (debes tener un archivo de imagen en el mismo directorio)

# Botones
admin_button = tk.Button(root, text="Iniciar como Admin", width=20,height=2,command=iniciar_admin)
admin_button.place(x=100,y=500)

usuario_button = tk.Button(root, text="Iniciar como Usuario", width=20,height=2,command=iniciar_usuario)
usuario_button.place(x=700,y=500)

# Ejecutar la ventana
root.mainloop()
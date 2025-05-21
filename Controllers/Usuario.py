from tkinter import messagebox
from Models.ConexionBD import ConexionesDB

class Usuario():
    def __init__(self, nombreUsuario, password):
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.rol = ""

    def iniciaSesion(self, nombreUsuario, password):
        miConexion = ConexionesDB()
        miConexion.crearConexion()
        conn = miConexion.getconection()
        cursor = conn.cursor()
        cursor.execute("select * from Usuario")
        listaUsuarios = cursor.fetchall
        for usuario in listaUsuarios:
            if (usuario[1] == nombreUsuario and usuario[2] == password):
                self.rol = usuario[3]
                if (self.rol == "admin"):
                    messagebox.showinfo("informacion" , "acesso correcto administrador!")
                else:
                    messagebox.showinfo("informacion" , "acesso correcto digitador!")
                miConexion.cerrarConexion()
                return
        messagebox.showwarning("advertencia" , "el nombre de usuario y/o contraseña no existen , verifique e intente nuevamente!")
        

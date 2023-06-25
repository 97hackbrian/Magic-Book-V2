import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from passlib.context import CryptContext
from form.login_form import Ui_login_form
from form.CreateAccount_form import Ui_CreateAccount_form

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.contexto= CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )
        # use the Ui_login_form
        self.ui = Ui_login_form()       
        self.ui.setupUi(self)       
        self.ui.pushButton.clicked.connect(self.authenticate)
        # show the login window
        self.show()

    def authenticate(self):
        user = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        #print(user,"  ",password)
        (userDesp,passwordDesp)= self.cargar_datos('clave.key')
        
        ##print("aqui:  ",userDesp,"     pass: ",passwordDesp)
        
        
        if self.contexto.verify(user,userDesp)and self.contexto.verify(password,passwordDesp):
            print("Usuario y contraseña válidos.")
        else:
            print("Usuario y/o contraseña incorrectos.")

    def cargar_datos(self, archivo):
        with open(archivo, 'rb') as f:
            datos = f.readline().decode('utf-8')

        #print(datos)
        user, passw = datos.split(" ")
        return (user, passw) 
    
class CreateAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.contexto= CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )
        if not os.path.exists('clave.key'):
            
            # use the Ui_CreateAccount_form
            self.ui = Ui_CreateAccount_form()       
            self.ui.setupUi(self)       
            self.ui.CrearCuenta.clicked.connect(self.Create)
            # show the Create account window
            self.show()


    def encriptar_datos(self,usuario,contrasena):
        '''contexto= CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )'''
        return (self.contexto.hash(usuario),self.contexto.hash(contrasena))

    def guardar_datos(self, datos, archivo):
        (Dusuario,Dcontrasena)=datos
        #print("encripting: ",(Dusuario,Dcontrasena))
        
        with open(archivo, 'wb') as f:
            f.write(Dusuario.encode('utf-8')+b" ")
            f.write(Dcontrasena.encode('utf-8'))

    def Create(self):
        usuario = self.ui.CreateUsuario.text()
        contrasena = self.ui.CreatePassword.text()

        #print(type(usuario),"  ",type(contrasena))


        
        self.guardar_datos(self.encriptar_datos(usuario,contrasena),'clave.key')

        print("Datos encriptados y guardados correctamente.")



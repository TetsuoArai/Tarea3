from flask import flash, render_template
import sqlite3

class DatosRegistrados():
    def __init__(self):
        self.conexion = sqlite3.connect('peliculas.db')
        self.cursor = self.conexion.cursor()
    
    def Comparar_datos(self, datos, nombre):
        validar_datos = False
        for extraer_datos in datos:
            for datos_recorridos in extraer_datos:
                if datos_recorridos == nombre:
                    validar_datos = True
            if validar_datos == True:
                break
        return validar_datos
    
#Funcion de InicioSesion
    def InicioSesion(self, correo, contraseña):
        self.cursor.execute(f'SELECT correo FROM persona')
        correoOBT = self.cursor.fetchall()

        if self.Comparar_datos(correoOBT, correo) == True:
            self.cursor.execute(f'SELECT contraseña FROM persona')
            contraseñaOBT = self.cursor.fetchall()
            if self.Comparar_datos(contraseñaOBT, contraseña) == True:
                return render_template('index.html')
            
            else:
                flash('La contraseña es incorrecta', 'danger')
                return render_template('login.html')
        else:
            flash('El correo es incorrecto', 'danger')
            return render_template('login.html')
        
#Funcion de registrar
    def Registrar(self, nombre, usuario, correo, contraseña):
        self.cursor.execute(f'SELECT usuario FROM persona')
        usuarioOBT = self.cursor.fetchall()
        self.cursor.execute(f'SELECT correo FROM persona')
        correoOBT = self.cursor.fetchall()

        if self.Comparar_datos(usuarioOBT, usuario) == True:
            flash('Este usuario se encuentra en uso', 'danger')
            return render_template('registrarse.html')
        
        elif self.Comparar_datos(correoOBT, correo) == True:
            flash('Hay un correo con esta cuenta', 'danger')
            return render_template('registrarse.html')
        
        else:
            flash('Se ha registrado', 'success')
            self.cursor.execute(f"INSERT INTO persona(nombre, usuario, correo, contraseña) VALUES('{nombre}','{usuario}','{correo}', '{contraseña}')")
            self.conexion.commit()
            return render_template('registrarse.html')
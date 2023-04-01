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
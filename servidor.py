from flask import Flask, render_template, request
from main import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Tarea3'

#rutas
@app.route('/')
def main():
    return render_template('LandingPage.html')

@app.route('/login')
def mostrar_login():
    return render_template('login.html')

@app.route('/registrar')
def mostrar_registrar():
    return render_template('registrarse.html')

@app.route('/index')
def mostrar_index():
    return render_template('index.html')

@app.route('/agg')
def mostrar_agg():
    return render_template('agregar.html')

@app.route('/pelicula')
def mostrar_pelicula():
    datos = DatosRegistrados()
    datosOBT = datos.traer_datos()
    return render_template('pelicula.html', datosDB=datosOBT)

#funciones
@app.route('/iniciarSesion', methods=['post'])
def extraer_datos():
    correo = request.form['usuario']
    contraseña = request.form['contraseña']
    usuario = DatosRegistrados()
    return usuario.InicioSesion(correo, contraseña)

@app.route('/Registrar', methods=['post'])
def registrar():
    nombre = request.form['nombre']
    usu = request.form['usuario']
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    usuario = DatosRegistrados()
    return usuario.Registrar(nombre, usu, correo, contraseña)

@app.route('/AggPelicula', methods=['post'])
def AggPelicula():
    imagen = request.form['imagen_peli']
    nombre = request.form['nombre_peli']
    tipo = request.form['movie-type']
    descripcion = request.form['movie-description']
    pelicula = DatosRegistrados()
    return pelicula.agregar_pelicula(imagen, nombre, tipo, descripcion)

if __name__ == '__main__':
    app.run(debug=True)
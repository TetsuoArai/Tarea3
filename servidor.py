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


#funciones
@app.route('/iniciarSesion', methods=['post'])
def extraer_datos():
    correo = request.form['usuario']
    contraseña = request.form['contraseña']
    usuario = DatosRegistrados()
    return usuario.InicioSesion(correo, contraseña)

if __name__ == '__main__':
    app.run(debug=True)
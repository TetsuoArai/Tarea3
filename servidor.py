from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Tarea3'

@app.route('/')
def main():
    return render_template('LandingPage.html')

if __name__ == '__main__':
    app.run(debug=True)
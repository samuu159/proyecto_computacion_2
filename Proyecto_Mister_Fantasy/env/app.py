from flask import Flask, render_template, request, redirect, url_for
import equipo
#import mercado

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar_scrapeo', methods=['POST'])
def iniciar_scrapeo():
    # Aquí llamas a la función de tu script de Python que inicia el scrapeo
    equipo.ejecutar_scrapeo()
    # Puedes redirigir al usuario a otra página o simplemente mostrar un mensaje de éxito
    return "Scrapeo completado con éxito!"

if __name__ == '__main__':
    app.run(debug=True)
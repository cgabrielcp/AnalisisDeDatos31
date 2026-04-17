from flask import Flask

app = Flask(__name__)

# Ruta 1 : Retorna un saludo simplet
@app.route('/api/hello')
def hello():
    """
    GET /api/hello
    Retorna: "Hola Mundo desde Docker
    """
    return "Hola Mundo desde Docker"

# Ruta 2 : Retrne un mensaje de texto
@app.route('/api/getData')
def getData():
    """
    GET /api/getData
    Retorna: "Mensajes"
    """
    resultado = 'Mensajes'

    return resultado

# iniciar el Servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)
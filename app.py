from flask import Flask, render_template, request
from model import Cliente
from pathlib import Path

app = Flask(__name__)

Cliente.cargar_datos(Path('data') / 'clientes.csv')

@app.route('/')
def index():
    # TODO: Cargar lista de clientes dende o modelo e pasala á vista clientes.html
    pass

@app.route('/clientes/<int:id>')
def detalle_cliente(id):
    # TODO: Cargar cliente dende o modelo e pasalo á vista detalle_cliente.html
    pass



if __name__ == '__main__':
    app.run(debug=True)
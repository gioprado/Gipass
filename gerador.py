from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-senha', methods=['POST'])
def gerar_senha():
    dados = request.get_json()
    tamanho = dados.get('tamanho', 8)
    caracteres = 'abcdefghijklmnopqrstuvwxyz!@#$*.'
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return jsonify({'senha': senha})

if __name__ == '__main__':
    app.run(debug=True)

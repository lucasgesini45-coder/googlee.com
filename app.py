

import os
import csv
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(PASTA, "registros.csv")

def salvar_demonstracao(email, senha, evento):
    novo_arquivo = not os.path.exists(ARQUIVO)

    with open(ARQUIVO, "a", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")

        if novo_arquivo:
            escritor.writerow([
                "data_hora",
                "email",
                "senha",
                "evento"
            ])

        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            email,
            senha,
            evento
        ])

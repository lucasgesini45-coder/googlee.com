
import csv
from pathlib import Path
from datetime import datetime

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

ARQUIVO_CSV = Path(__file__).resolve().parent / "dados.csv"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/evento", methods=["POST"])
def registrar_dados():
    dados = request.get_json(silent=True) or {}

    email = str(dados.get("email", "")).strip()
    idade_texto = str(dados.get("idade", "")).strip()

    if not email or "@" not in email:
        return jsonify({"erro": "Informe um e-mail válido."}), 400

    try:
        idade = int(idade_texto)
        if not 1 <= idade <= 120:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"erro": "Informe uma idade entre 1 e 120."}), 400

    arquivo_existe = ARQUIVO_CSV.exists() and ARQUIVO_CSV.stat().st_size > 0

    with ARQUIVO_CSV.open(
        "a",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        campos = ["data_hora", "email", "idade"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if not arquivo_existe:
            escritor.writeheader()

        escritor.writerow({
            "data_hora": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            "email": email,
            "idade": idade
        })

    return jsonify({"sucesso": True}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

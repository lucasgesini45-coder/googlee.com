
import csv
import os
from datetime import datetime

ARQUIVO = "registros.csv"

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

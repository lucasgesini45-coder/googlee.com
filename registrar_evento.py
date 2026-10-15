
import csv
import os
from datetime import datetime

ARQUIVO = "registros.csv"

def registrar_evento(evento, resultado):
    novo_arquivo = not os.path.exists(ARQUIVO)

    with open(ARQUIVO, "a", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")

        if novo_arquivo:
            escritor.writerow([
                "id", "data_hora", "evento", "resultado"
            ])

        escritor.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            evento,
            resultado
        ])

if __name__ == "__main__":
    registrar_evento(
        "botao_clicado",
        "redirecionamento_para_google"
    )
    print("Evento registrado em registros.csv")

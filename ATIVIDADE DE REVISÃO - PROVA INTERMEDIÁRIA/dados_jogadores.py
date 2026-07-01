from app import criar_app
from models import Jogador, db

JOGADORES = [
    {"nome": "Alisson", "posicao": "Goleiro", "clube": "Liverpool", "cabeceio": 5, "forca": 6},
    {"nome": "Marquinhos", "posicao": "Defensor", "clube": "PSG", "cabeceio": 8, "forca": 7},
    {"nome": "Casemiro", "posicao": "Meio-campista", "clube": "Manchester United", "cabeceio": 7, "forca": 8},
    {"nome": "Vinicius Jr", "posicao": "Atacante", "clube": "Real Madrid", "cabeceio": 6, "forca": 7},
    {"nome": "Rodrygo", "posicao": "Atacante", "clube": "Real Madrid", "cabeceio": 6, "forca": 6},
]


def popular():
    app = criar_app()
    with app.app_context():
        if Jogador.query.count() == 0:
            for dados in JOGADORES:
                db.session.add(Jogador(**dados))
            db.session.commit()
            print(f"{len(JOGADORES)} jogadores cadastrados.")
        else:
            print("Já existem jogadores cadastrados.")


if __name__ == "__main__":
    popular()

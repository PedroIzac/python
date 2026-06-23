from flask import Blueprint, render_template
from models import Filme
from models import Sala
from models import Sessao


# Nome que você escolher
bp = Blueprint("dashboard", __name__)

@bp.route("/")
def index():
    return render_template(
        "index.html",
        total_filme=Filme.query.count(),
        total_salas=Sala.query.count(),
        total_sessoes=Sessao.query.count()
    )

# Exemplo:
# total_clientes = Cliente.query.count()
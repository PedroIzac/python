from flask import Flask

from controllers import dashboard_bp, jogador_bp
from models import db


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jogadores.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(jogador_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = criar_app()
    app.run(debug=True)

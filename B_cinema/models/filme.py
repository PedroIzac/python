from . import db
from .base import ModeloBase


class Filme(ModeloBase):
    __tablename__ = "filmes"

    titulo = db.Column(db.String(150), nullable=False)
    duracao_min = db.Column(db.int, nullable=False)
    classificacao = db.Column(db.String(5), nullable=False)
    sessao_id = db.Column(db.Integer, db.ForeignKey("sessao.id"), nullable=False)
    # TODO ALUNO: relationship sessoes
    sessoes = db.relationship("Sessao", back_populates = "filme")

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.titulo).all()

from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

from .operacao import Operacao

__all__ = ["db", "Operacao"]
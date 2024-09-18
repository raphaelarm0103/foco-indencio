from flask import Flask
from config import Config
from models import db
from focos_incendio import focos_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar o banco de dados
    db.init_app(app)

    # Registrar o blueprint
    app.register_blueprint(focos_blueprint)

    # Criar as tabelas se elas ainda não existirem
    with app.app_context():
        db.create_all()

    return app

from app import db

# Modelo FocoIncendio
class FocoIncendio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=True)

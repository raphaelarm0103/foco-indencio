from flask import Blueprint, jsonify, request
from models import db, FocoIncendio, Usuario

focos_blueprint = Blueprint('focos', __name__)

@focos_blueprint.route('/api/get_focos', methods=['GET'])
def get_focos():
    focos = FocoIncendio.query.all()
    resultado = []
    for foco in focos:
        resultado.append({
            'endereco': foco.endereco,
            'latitude': foco.latitude,
            'longitude': foco.longitude,
            'descricao': foco.descricao
        })
    return jsonify({'focos': resultado})

@focos_blueprint.route('/api/cadastrar_foco', methods=['POST'])
def cadastrar_foco():
    data = request.get_json()
    novo_foco = FocoIncendio(
        usuario_id=data['usuario_id'],
        endereco=data['endereco'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        descricao=data.get('descricao', '')
    )
    db.session.add(novo_foco)
    db.session.commit()
    return jsonify({'message': 'Foco de incêndio cadastrado com sucesso!'})

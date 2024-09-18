from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração da URI de conexão com o MySQL usando o driver pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://raphael:raphael123@localhost:3306/foco_incendio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o SQLAlchemy
db = SQLAlchemy(app)


# Modelo para FocoIncendio
class FocoIncendio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.Text, nullable=True)


# Rota para visualizar o HTML
@app.route('/')
def index():
    return render_template('index.html')


# Rota para buscar focos de incêndio no banco de dados
@app.route('/api/get_focos', methods=['GET'])
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


# Rota para cadastrar um novo foco de incêndio
@app.route('/api/cadastrar_foco', methods=['POST'])
def cadastrar_foco():
    data = request.get_json()
    novo_foco = FocoIncendio(
        endereco=data['endereco'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        descricao=data.get('descricao', '')
    )
    try:
        db.session.add(novo_foco)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        print(f"Erro ao cadastrar foco: {e}")
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run(debug=True)

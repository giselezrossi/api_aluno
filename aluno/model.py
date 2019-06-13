import sqlalchemy as db
engine = db.create_engine('postgresql://postgres:postgres@localhost/tutorial_flask')


class Aluno():
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    sobrenome = db.Column(db.String(80), nullable=False)
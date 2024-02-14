import json

from config import db, ma


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_json(self) -> str:
        schema = UserSchema().dump(self)
        return json.dumps(schema)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        sqla_session = db.session

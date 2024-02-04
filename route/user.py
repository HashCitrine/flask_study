import json

from flask import Blueprint, Response, request

from config import db
from dto.response import ResponseEntity as Res
from entity.user import UserModel, UserSchema

bp = Blueprint('user', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@bp.route('/users', methods=['post'])
def create_user() -> Response:
    user = user_schema.load(request.json)
    db.session.add(user)
    db.session.commit()

    name = {'name': user.name}
    return Res(json.dumps(name))


@bp.route('/users', methods=['GET'])
def get_users() -> Response:
    users = UserModel.query.all()

    schema = users_schema.dump(users)
    res = json.dumps(schema)
    return Res(res)


@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> Response:
    users = UserModel.query.filter(UserModel.id == user_id)

    schema = users_schema.dump(users)
    res = json.dumps(schema)
    return Res(res)


@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id: int) -> Response:
    updated_user = user_schema.load(request.json)

    user = UserModel.query.filter(UserModel.id == user_id)

    if user.count() == 0:
        raise Exception('Unregistered user')

    updated_user.id = user_id

    db.session.merge(updated_user)
    db.session.commit()

    schema = user_schema.dump(updated_user)
    res = json.dumps(schema)
    return Res(res)



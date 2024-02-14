import json

from flask import Blueprint, Response, request

from dto.response import ResponseEntity as Res
from model.user_model import UserSchema
from service import user_service

bp = Blueprint('user', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@bp.route('/users', methods=['post'])
def create_user() -> Response:
    user = user_service.create_user(request.json)

    name = {'name': user.name}
    return Res(json.dumps(name))


@bp.route('/users', methods=['GET'])
def get_users() -> Response:
    users = user_service.get_users()

    schema = users_schema.dump(users)
    res = json.dumps(schema)
    return Res(res)


@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> Response:
    users = user_service.get_user(user_id)

    schema = users_schema.dump(users)
    res = json.dumps(schema)
    return Res(res)


@bp.route('/users/<int:user_id>', methods=['PUT'])
async def update_user(user_id: int) -> Response:
    updated_user = user_service.update_user(user_id)

    schema = user_schema.dump(updated_user)
    res = json.dumps(schema)
    return Res(res)



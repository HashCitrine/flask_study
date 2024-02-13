from flask import request

from config import db
from entity.user import UserModel, UserSchema

user_schema = UserSchema()


def create_user(json) -> UserModel:
    user = user_schema.load(json)
    db.session.add(user)
    db.session.commit()

    return user


def get_users() -> list[UserModel]:
    users = UserModel.query.all()

    return users


def get_user(user_id: int) -> list[UserModel]:
    users = UserModel.query.filter(UserModel.id == user_id)

    return users


def update_user(user_id: int) -> UserModel:
    updated_user = user_schema.load(request.json)

    user = UserModel.query.filter(UserModel.id == user_id)

    if user.count() == 0:
        raise Exception('Unregistered user')

    updated_user.id = user_id

    db.session.merge(updated_user)
    db.session.commit()

    return updated_user

from flask import request

from config import db
from model.user_model import UserModel, UserSchema
from decorator.log import service_log

user_schema = UserSchema()


@service_log
def create_user(json) -> UserModel:
    user = user_schema.load(json)
    db.session.add(user)
    db.session.commit()

    return user


@service_log
def get_users() -> list[UserModel]:
    users = UserModel.query.all()

    return users


@service_log
def get_user(user_id: int) -> list[UserModel]:
    users = UserModel.query.filter(UserModel.id == user_id)

    return users


@service_log
def update_user(user_id: int) -> UserModel:
    updated_user = user_schema.load(request.json)

    user = UserModel.query.filter(UserModel.id == user_id)

    if user.count() == 0:
        raise Exception('Unregistered user')

    updated_user.id = user_id

    db.session.merge(updated_user)
    db.session.commit()

    return updated_user

from flask import Blueprint, Response

bp = Blueprint('test', __name__)


@bp.route('/', methods=['GET'])
def hello_world() -> Response:
    return Response('Hello world', 200)


@bp.route('/error', methods=['GET'])
def error():
    raise Exception('test error')

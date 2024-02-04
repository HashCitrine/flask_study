from flask import Blueprint

from dto.response import ResponseEntity as Res
import json

bp = Blueprint('exception', __name__)


@bp.app_errorhandler(Exception)
def global_exception_handler(error: Exception):
    res = {'message': error.args[0]}
    return Res(json.dumps(res), 500)

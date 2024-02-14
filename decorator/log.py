import json
from functools import wraps

from flask import current_app
from model.user_model import UserModel

from io import StringIO


def service_log(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        message = None

        if isinstance(result, list):
            string_builder = None
            for user_model in result:
                if string_builder is None:
                    string_builder = StringIO()
                    string_builder.write("\n[")
                else:
                    string_builder.write("\n, ")

                string_builder.write(user_model.to_json())
            string_builder.write("]")
            message = string_builder.getvalue()
        elif isinstance(result, UserModel):
            message = result.to_json()

        if message is not None:
            current_app.logger.info("%s 실행 결과 : %s", func.__name__, message)
        return result

    return wrap

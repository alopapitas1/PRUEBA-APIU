from flask import jsonify
from functools import wraps
from flask_jwt_extended import get_jwt_identity,verify_jwt_in_request
import json

def jwt_requiered(fn):

    @wraps(fn)
    def warpeds(*args,**kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args,**kwargs)
        except Exception as e:
            jsonify({"error":str(e)}),401
    return warpeds


def roles_required(roles=[]):
    def decorator(fn):
        @wraps(fn)
        def warped(*args,**kwargs):
            try:
                verify_jwt_in_request()
                username=get_jwt_identity()
                user_roles=json.loads(username.get("roles",[]))
                if not set(user_roles).intersection(roles):
                    return jsonify({"error":"acceso no autorizado"}),403
                return fn(*args,**kwargs)
            except Exception as e:
                return jsonify({"error":str(e)}),401
        return warped
    return decorator

        
from flask import Blueprint,jsonify,request
import json
from flask_jwt_extended import create_access_token
from app.models.user_model import User
from werkzeug.security import check_password_hash

user_bp=Blueprint("user",__name__) 

@user_bp.route("/register",methods=["POST"])
def register():
    data=request.json
    username=data.get("username")
    password=data.get("password")
    roles=data.get("roles")
    
    if username is None or password is None:
        return jsonify({"error":"Se requiere usario o contraseña"}),401
    
    exist_user=User.find_username(username)
    if exist_user:
        return jsonify({"error":"El nombre de usuario ya está en uso"}),400
    
    new_user=User(username,password,roles)
    new_user.save()
    return ({"message":"Usuario creado exitosamente"}),201
    

@user_bp.route("/login",methods=["POST"])
def login():
    data=request.json
    username=data.get("username")
    password=data.get("password")
    
    user=User.find_username(username)
    if user and check_password_hash(user.password, password):
        access_token=create_access_token(identity={"username":username, "roles":user.roles})
        return jsonify(access_token=access_token),200
    else:
        return jsonify({"error":"Credenciales inválidas"}),401
    
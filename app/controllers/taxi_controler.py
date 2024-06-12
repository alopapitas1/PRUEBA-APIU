from flask import jsonify,request,Blueprint
from app.views.taxis_view import render_taxis_detail,render_taxis_list
from app.utils.decorator import jwt_requiered,roles_required
from app.models.taxis_model import Taxi
from app.models.user_model import User
import json

taxi_bp=Blueprint("taxi",__name__)

@taxi_bp.route("/taxis",methods=["GET"])
@jwt_requiered
@roles_required(roles=["user","admin"])
def get_taxis():
    taxis=Taxi.get_all()
    return jsonify(render_taxis_list(taxis))

@taxi_bp.route("/taxis/<int:id>",methods=["GET"])
@jwt_requiered
@roles_required(roles=["admin","user"])
def get_by_id(id):
    taxi=Taxi.get_id(id)
    if not taxi:
        return jsonify({"error":"taxi no encontrado"}),404
    return jsonify(render_taxis_detail(taxi))


@taxi_bp.route("/taxis",methods=["POST"])
@jwt_requiered
@roles_required(roles=["admin"])
def new_taxi():
    data=request.json
    chofer=data.get("chofer")
    color=data.get("color")
    frec=data.get("frec")
    ingresos=data.get("ingresos")

    if chofer is None or color is None or frec is None or frec is None or frec is None or ingresos is None:
        return jsonify({"error":"Faltan datos requeridos"}),400
    taxi=Taxi(chofer=chofer, color=color, frec=bool(frec),ingresos=float(ingresos))
    taxi.save()
    
    return jsonify(render_taxis_detail(taxi)),201
    
@taxi_bp.route("/taxis/<int:id>",methods=["PUT"])
@jwt_requiered
@roles_required(roles=["admin"])
def actu_taxi(id):
    taxi =Taxi.get_id(id)
    if not taxi:
        return jsonify({"error":"taxi no encontrado"}),404
    data=request.json
    chofer=data.get("chofer")
    color=data.get("color")
    frec=data.get("frec")
    ingresos=data.get("ingresos")
    taxi.update(chofer=chofer, color=color, frec=bool(frec),ingresos=float(ingresos))
    return jsonify(render_taxis_detail(taxi))

@taxi_bp.route("/taxis/<int:id>",methods=["DELETE"])
@jwt_requiered
@roles_required(roles=["admin"])
def delete_taxi(id):
    taxi=Taxi.get_id(id)
    if not taxi:
        return jsonify({"error":"taxi no encontrado"}),404
    taxi.delete()
    return "",204
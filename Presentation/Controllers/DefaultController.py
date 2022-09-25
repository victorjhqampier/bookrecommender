from flask import Blueprint
from Domain.Core.StatusCode import StatusCode
from Domain.Entities.Response import Response
from datetime import datetime

defaultController = Blueprint("defaultController",__name__)

@defaultController.route("/",methods=["GET"])
def AxDefaultController():
    return StatusCode(200,Response(success=1,message="AX-TATA Corporation - Todos los derechos reservados",data={"message":"Recomendacion de libros - Running","date":datetime.now()}))

from Domain.Entities.Data.AuthDataEntity import AuthDataEntity
from Domain.Enums.TokenEnum import TokenEnum
from Infrastructure.Oauth.AutenticacionDatabase import AutenticacionDatabase
from flask_cors import CORS, cross_origin
from Domain.Common.EasyResponseCommon import EasyResponseCommon
from Domain.Core.StatusCode import FromBody, StatusCode
from Domain.Entities.Request.AuthRequestEntity import AuthRequestEntity

from Domain.Interfaces.IAutenticacion import IAutenticacion
from Domain.Interfaces.IEasyResponse import IEasyResponse
from flask import request, Blueprint
from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

EasyResponse:IEasyResponse = EasyResponseCommon()
Authentication:IAutenticacion = AutenticacionDatabase()

authenticationController = Blueprint("authenticationController",__name__)
CORS(authenticationController)

# @cross_origin
@authenticationController.route("/login", methods=["POST"])
def IniciarSesion():
    try:
        inputBody = FromBody(request.get_json(), AuthRequestEntity)
        idUsuario:int = Authentication.IniciarSesion(inputBody.cUser,inputBody.cPassword)

        if idUsuario == 0:
            return StatusCode(200, EasyResponse.EasyErrorRespond(cErrorCode="97", cErrorMessage="Usuario o contraseña incorrectos", cMessage="La petición no pudo completarse debido a que la solicitud no fue válida")) 

        nExpire:int = int(TokenEnum.Expire)
        newObjToken: AuthDataEntity = AuthDataEntity(
            cToken=create_access_token(identity=str(idUsuario),expires_delta=timedelta(nExpire)),
            nExpireIn=nExpire
            )
        return StatusCode(200,EasyResponse.EasySuccessRespond(newObjToken))
    
    except Exception as ex:        
        return StatusCode(200,EasyResponse.EasyErrorRespond("99","Error general interno. " + str(ex)))

#Para verificar
#REQUIERE TOKEN Y corn
@authenticationController.route("/log",methods=["POST"])
@jwt_required()
def axroute_verify_token():
    user = get_jwt_identity()
    # return StatusCode(200,IndexInterface(status=200,message=user))
    return StatusCode(200,EasyResponse.EasySuccessRespond({"message":user}))
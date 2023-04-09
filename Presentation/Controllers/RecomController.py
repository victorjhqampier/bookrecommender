from flask import Blueprint, request
from Domain.Core.StatusCode import StatusCode, FromBody
from Domain.Interfaces.IBook import IBook
from Domain.Interfaces.IEasyResponse import IEasyResponse
from Domain.Common.EasyResponseCommon import EasyResponseCommon
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required

from Domain.Interfaces.IRecomInfrastructure import IRecomInfrastructure
from Infrastructure.Neo4j.Programmabilities.RecomMethod import RecomMethod

#=======================================================================
#   © Victor JCaxi - All rights reserved
#-----------------------------------------------------------------------
#   Aim         : Recomendar libros sobre Neo4j Database
#   Created     : 22-03-2023
#   By          : Victor JCaxi
#-----------------------------------------------------------------------
#   Changes:
#   By        Date       Aim
#=======================================================================

EasyResponse: IEasyResponse = EasyResponseCommon()
objRecom:IRecomInfrastructure = RecomMethod()

recomController = Blueprint("recomController", __name__)
CORS(recomController)

@recomController.route("/jaccard-index", methods=["POST"])
@jwt_required()
def JaccardIndexRecom():
    try:
        idTitle:str = request.get_json()["idTitle"]

        # objRecom:IRecomInfrastructure = RecomMethod()     

        result:list = objRecom.GetJaccardIndexRecom(int(idTitle))
        if(len(result) == 0):
            return StatusCode(200, EasyResponse.EasyEmptyRespond())
        
        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))

@recomController.route("/co-responsibility", methods=["POST"])
@jwt_required()
def CoResponsibilityRecom():
    try:
        idTitle:str = request.get_json()["idTitle"]

        # objRecom:IRecomInfrastructure = RecomMethod()

        result:list = objRecom.GetCoResponsibilityRecom(int(idTitle))
        if(len(result) == 0):
            return StatusCode(200, EasyResponse.EasyEmptyRespond())
        
        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))

@recomController.route("/classification", methods=["POST"])
@jwt_required()
def ClassificationRecom():
    try:
        idTitle:str = request.get_json()["idTitle"]

        # objRecom:IRecomInfrastructure = RecomMethod()

        result:list = objRecom.GetClassificationRecom(int(idTitle))
        if(len(result) == 0):
            return StatusCode(200, EasyResponse.EasyEmptyRespond())
        
        return StatusCode(200, EasyResponse.EasySuccessRespond(result))

    except Exception as e:
        return StatusCode(500, EasyResponse.EasyErrorRespond("99", "Error general interno. " + str(e)))
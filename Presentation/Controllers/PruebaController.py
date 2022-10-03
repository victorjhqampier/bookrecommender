from flask import Blueprint,request
from Domain.Core.StatusCode import StatusCode,FromBody
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Entities.Response import Response
from datetime import datetime

from Domain.Interfaces.IAuthor import IAuthor
from Domain.Interfaces.IEasyResponse import IEasyResponse
from Infrastructure.Neo4j.Nodes.AuthorNode import AuthorNode
from Domain.Common.EasyResponseCommon import EasyResponseCommon

Autor : IAuthor = AuthorNode()
EasyResponse:IEasyResponse = EasyResponseCommon()

pruebaController = Blueprint("pruebaController",__name__)

@pruebaController.route("/prueba",methods=["POST"])
def PruebaController():

    arrInput:list = request.get_json()
    arrAuthorIn:list =[]
    for item in arrInput["responsibles"]:
        item["idAuthor"] = ''        
        InputEmperesa:AuthorDataEntity = FromBody(item, AuthorDataEntity)
        arrAuthorIn.append(InputEmperesa)
    arrGuardarEmpre:list = Autor.MergeAuthors(arrAuthorIn)
    return StatusCode(200,EasyResponse.EasySuccessRespond(arrGuardarEmpre)) 

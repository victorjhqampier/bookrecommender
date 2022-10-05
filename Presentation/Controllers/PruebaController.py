from flask import Blueprint,request
from Domain.Core.StatusCode import StatusCode,FromBody
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Response import Response
from datetime import datetime

from Domain.Interfaces.IAuthor import IAuthor
from Domain.Interfaces.IEasyResponse import IEasyResponse
from Domain.Interfaces.IPublisher import IPublisher
from Infrastructure.Neo4j.Nodes.AuthorNode import AuthorNode
from Domain.Common.EasyResponseCommon import EasyResponseCommon
from Infrastructure.Neo4j.Nodes.PublisherNode import PublisherNode

# Autor : IAuthor = AuthorNode()
Publisher: IPublisher = PublisherNode()
EasyResponse:IEasyResponse = EasyResponseCommon()

pruebaController = Blueprint("pruebaController",__name__)

@pruebaController.route("/prueba",methods=["POST"])
def PruebaController():

    arrInput:list = request.get_json()
    arrAuthorIn:list =[]
    for item in arrInput["publishers"]:
        item["idPublisher"] = ''        
        InputEmperesa:PublisherDataEntity = FromBody(item, PublisherDataEntity)
        arrAuthorIn.append(InputEmperesa)
    arrGuardarEmpre:list = Publisher.MergePublisher(arrAuthorIn)
    return StatusCode(200,EasyResponse.EasySuccessRespond(arrGuardarEmpre)) 

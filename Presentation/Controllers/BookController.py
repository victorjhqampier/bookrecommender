from flask import Blueprint,request
from Domain.Core.StatusCode import StatusCode,FromBody
from Domain.Entities.Data.AuthorDataEntity import AuthorDataEntity
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.CopyDataEntity import CopyDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Entities.Response import Response
from datetime import datetime

from Domain.Interfaces.IAuthor import IAuthor
from Domain.Interfaces.IClassification import IClassification
from Domain.Interfaces.ICopy import ICopy
from Domain.Interfaces.IEasyResponse import IEasyResponse
from Domain.Interfaces.IItem import IItem
from Domain.Interfaces.IPublisher import IPublisher
from Domain.Interfaces.ISerialTitle import ISerialTitle
from Infrastructure.Neo4j.Nodes.AuthorNode import AuthorNode
from Domain.Common.EasyResponseCommon import EasyResponseCommon
from Infrastructure.Neo4j.Nodes.ClassificationNode import ClassificationNode
from Infrastructure.Neo4j.Nodes.CopyNode import CopyNode
from Infrastructure.Neo4j.Nodes.ItemNode import ItemNode
from Infrastructure.Neo4j.Nodes.PublisherNode import PublisherNode
from Infrastructure.Neo4j.Nodes.SerialTitleNode import SerialTitleNode

EasyResponse:IEasyResponse = EasyResponseCommon()

bookController = Blueprint("bookController",__name__)

@bookController.route("/save",methods=["POST"])
def SaveBook():

    arrInput:list = request.get_json()

    arrPublisher:list =[]
    for item in arrInput["publishers"]:
        item["idPublisher"] = ''        
        Input:PublisherDataEntity = FromBody(item, PublisherDataEntity)
        arrPublisher.append(Input)
    
    arrAuthors:list =[]
    for item in arrInput["responsibles"]:
        item["idAuthor"] = ''        
        Input:AuthorDataEntity = FromBody(item, AuthorDataEntity)
        arrAuthors.append(Input)
    
    arrInput['classification']['idClassification'] = ''
    objclassification:ClassificationDataEntity = FromBody(arrInput['classification'], ClassificationDataEntity)

    arrInput['serialTitle']['idSerialTitle'] = ''
    objSerialTitle:SerialTitlesDataEntity = FromBody(arrInput['serialTitle'], SerialTitlesDataEntity)

    arrInput['item']['idItem'] = ''
    objItem:ItemDataEntity = FromBody(arrInput['item'], ItemDataEntity)
    
    arrAuthor:list =[]
    for item in arrInput["copies"]:
        item["idCopy"] = ''        
        Input:CopyDataEntity = FromBody(item, CopyDataEntity)
        arrAuthor.append(Input)

    return StatusCode(200,EasyResponse.EasySuccessRespond(objItem)) 
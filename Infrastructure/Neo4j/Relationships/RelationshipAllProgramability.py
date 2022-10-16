from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Enums.RelationShipEnum import RelationShipEnum
from Domain.Interfaces.IAllRelationship import IAllRelationship
from Domain.Interfaces.IContext import IContext
from Infrastructure.Neo4j.DbContext import DbContext


class RelationshipAllProgramability(IAllRelationship):

    __db: IContext = DbContext()

    def __init__(self):
        pass
    
    def MergeAllRelationships(self, objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:list, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity):
        
        NewRelation = self.__db.Relationship()

        idItem:int = int(objItem.idItem)

        for item in arrCopies:
            NewRelation.Merge(idItem, RelationShipEnum.ItemToCopy, int(item.idCopy))
        
        for item in arrAuthors:
            NewRelation.Merge(int(item.idAuthor), RelationShipEnum.ResponsibleToItem, idItem,("cRole",item.cRole))
        
        for item in arrPublisher:
            NewRelation.Merge(int(item.idPublisher), RelationShipEnum.publisherToItem, idItem)
        
        NewRelation.Merge(int(objClass.idClassification), RelationShipEnum.ClassificationToItem, idItem)

        if int(objSerial.idSerialTitle) != 0:
            NewRelation.Merge(int(objSerial.idSerialTitle), RelationShipEnum.SerialTitleToItem, idItem, ("cNumber",objSerial.cNumber))

        NewRelation.Select("TRUE AS idRelationship").FirstOrDefault()
        return





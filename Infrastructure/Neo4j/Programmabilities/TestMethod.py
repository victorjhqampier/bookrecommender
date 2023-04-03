from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Entities.Request.MergeBookResponseEntity import MergeBookResponseEntity
from Domain.Interfaces.IContext import IContext
from Infrastructure.Neo4j.DbContext import DbContext


class TestMethod():     

    def __init__(self):
        self.__db: IContext = DbContext()

    def MergeBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity) -> MergeBookResponseEntity:
             
        BuildRecomByJaccard = self.__db.Query()

        BuildRecomByJaccard.Match(            
            ).Node("Title","m").LeftRelationship("HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO").Node("t"
            ).RightRelationship("HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO").Node("Title","recom"
            ).Where().Id("m", 913
            ).With().Node("m").And().Node("recom").And().Count("t").As("intersection").And(
            ).OnArray("m","HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO","mt").As("s1").And(
            ).OnArray("recom","HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO","recomt").As("s2")
        
        return BuildRecomByJaccard.ToString()
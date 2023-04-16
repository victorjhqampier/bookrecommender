from Domain.Common.HelperCommon import HelperCommon
from Domain.Entities.Data.ClassificationDataEntity import ClassificationDataEntity
from Domain.Entities.Data.ItemDataEntity import ItemDataEntity
from Domain.Entities.Data.PublisherDataEntity import PublisherDataEntity
from Domain.Entities.Data.SerialTitlesDataEntity import SerialTitlesDataEntity
from Domain.Entities.Request.MergeBookResponseEntity import MergeBookResponseEntity
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IHelper import IHelper
from Infrastructure.Neo4j.DbContext import DbContext
from unicodedata import normalize
import re

class TestMethod():     

    def __init__(self):
        self.__db: IContext = DbContext()
        self.__helper: IHelper = HelperCommon()

    def MergeBook(self,objItem:ItemDataEntity, arrCopies:list,arrAuthors:list, arrPublisher:PublisherDataEntity, objClass:ClassificationDataEntity,objSerial:SerialTitlesDataEntity) -> MergeBookResponseEntity:
             
        BuildRecomByClassification = self.__db.Query()
        BuildRecomByClassification.SearchByIndex("quechua","titlesAndDescriptions"         
            ).Node("Title","doc"
            ).With(
                ).Node("doc"
                ).And().CountId("doc").As("coincidence"
            ).Match(
                ).Node("doc"
                ).LeftRelationship("HAS_RESPONSIBILITY","au"
                ).Node("Person","peo"
            ).With(
                ).Node("doc"
                ).And().Node("coincidence"
                ).And().SortObjectCollect("{cName:peo.cName, cSurname:peo.cSurname, cRole:au.cRole}","cRole").As("pe"
            ).Select("ID(doc) as idBook,doc.cTitle as cTitle,doc.cSubtitle as cSubtitle,doc.cTopics as cTopic,(doc.nReleased + ', '+doc.cEdition) as cRelease,doc.cImage as cImage,(pe.cName+' '+pe.cSurname) as cAuthor,pe.cRole as cRole, doc.nViews as nViews"                                                                                            
            ).OrderByDescending("coincidence"
            ).Limit(30)
        
        return self.__helper.GenerateIndex("desde entré https://google.com.pe Nándúü,545 los' goes más ál Álvaradö {:mamá:} así me gusta caxi")
        #return BuildRecomByClassification.ToList()
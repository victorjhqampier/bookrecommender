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
        
        return BuildRecomByClassification.ToList()
        # Words=["a","con","de","al","e","en", "ademas","tal","sus","el","entre","sido","asi","desde","ella","ello","del","es","estas","sin","esto","han","estos","esta","este","ha","pe","com","como","he","la","las","los","les","mas","mi","me","muy","no","o","para","por","que","se","si","son","su","tu","un","una","y","ya","yo","tus","tu","te","lo"]
        # cString = "La ñoña piñata, de José Cañada, está en la piñateria. La película 'Los niños del barrio' se proyectará en el teatro mañana a las 8:00 PM. El código secreto es 'GK#&%c4tY' y debe ingresarse en el formulario en línea. ¿Puedes adivinar la respuesta a 2+2 sin usar una calculadora?" 
        
        # # cString = normalize("NFD", cString.lower())
        # # cString = re.sub( r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",normalize( "NFD", cString.lower()), 0, re.I)
        # # arrTemp = [x for x in cString.split(" ") if x not in Words and len(x) > 2]
        # # cString = ''.join([char for char in " ".join(arrTemp) if char.isalnum()])
        # # return cString
        # return self.__helper.GenerateIdentifier(cString)
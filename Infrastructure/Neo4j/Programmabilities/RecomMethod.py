from Domain.Entities.Data.BookSimpleEntity import BookSimpleEntity
from Domain.Interfaces.IContext import IContext
from Domain.Interfaces.IRecomInfrastructure import IRecomInfrastructure
from Infrastructure.Neo4j.DbContext import DbContext

class RecomMethod(IRecomInfrastructure): 

    def __init__(self):
        self.__db: IContext = DbContext()

    def SearchBook(self,cKeyWord:str) -> list[BookSimpleEntity]:             
        BuildSearch = self.__db.Query()
        BuildSearch.SearchByIndex(cKeyWord,"titlesAndDescriptions"         
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
            ).Select("ID(doc) as idTitle,doc.cTitle as cTitle,doc.cSubtitle as cSubtitle,doc.cTopics as cTopic,(doc.nReleased + ' '+doc.cEdition) as cRelease,doc.cImage as cImage,(pe.cName+' '+pe.cSurname) as cAuthor,pe.cRole as cRole, doc.nViews as nViews"                                                                                            
            ).OrderByDescending("coincidence"
            ).Limit(30)
        
        return BuildSearch.ToList()
    
    def GetJaccardIndexRecom(self,idTitle:int) -> list[BookSimpleEntity]:       
        BuildRecomByJaccard = self.__db.Query()
        BuildRecomByJaccard.Match(            
            ).Node("Title","m"
                ).LeftRelationship("HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO"
            ).Node("t"
                ).RightRelationship("HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO"
            ).Node("Title","recom"
            ).Where(            
                ).Id("m", idTitle
            ).With(                
                ).Node("m"
                ).And().Node("recom"
                ).And().Count("t").As("intersection"
                ).And().OnSet("m","HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO","mt").As("neighbors_m"
                ).And().OnSet("recom","HAS_RESPONSIBILITY|ASSIGN_DEWEY|PUBLISHED|PART_TO","recomt").As("neighbors_recom"
            ).With(
                ).Node("recom"
                ).And().Node("intersection"
                ).And().FromRaw("neighbors_m + [x IN neighbors_recom WHERE NOT x IN neighbors_m]").As("union"
            ).With(            
                ).Node("recom"
                ).And().FromRaw("((1.0 * intersection) / SIZE(union))").As("jaccard"
                ).Where("jaccard > 0.16"
            ).Match(# View only         
                ).Node("recom").LeftRelationship("HAS_RESPONSIBILITY","res").Node("per"
            ).With(
                ).Node("recom"
                ).And().Node("jaccard"
                ).And().SortObjectCollect("{cName:per.cName, cSurname:per.cSurname, cRole:res.cRole}","cRole").As("author"
            ).Select("ID(recom) as idTitle,recom.cTitle as cTitle,recom.cSubtitle as cSubtitle,recom.cTopics as cTopic,(recom.nReleased + ' '+recom.cEdition) as cRelease,recom.cImage as cImage,(author.cName+' '+author.cSurname) as cAuthor,author.cRole as cRole, recom.nViews as nViews"
            ).OrderByDescending("jaccard,recom.nViews"
            ).Limit(10)
        
        return BuildRecomByJaccard.ToList()
    
    def GetCoResponsibilityRecom(self,idTitle:int) -> list[BookSimpleEntity]:
        BuildRecomByCoResponsibility = self.__db.Query()
        BuildRecomByCoResponsibility.Match(            
            ).Node("Title","m"
                ).LeftRelationship("HAS_RESPONSIBILITY"
            ).Node("person"
                ).RightRelationship("HAS_RESPONSIBILITY"
            ).Node("Title","other"
                ).And(            
            ).Node("other"
                ).LeftRelationship("HAS_RESPONSIBILITY"
            ).Node("co"
                ).RightRelationship("HAS_RESPONSIBILITY"
            ).Node("Title","recom"
            ).Where(   
                ).Id("m", idTitle).And("m <> recom"
            ).Match(# View only         
                ).Node("recom").LeftRelationship("HAS_RESPONSIBILITY","res").Node("per"
            ).With(
                ).Node("recom"
                ).And().SortObjectCollect("{cName:per.cName, cSurname:per.cSurname, cRole:res.cRole}","cRole").As("author"
            ).Select("ID(recom) as idTitle,recom.cTitle as cTitle,recom.cSubtitle as cSubtitle,recom.cTopics as cTopic,(recom.nReleased + ' '+recom.cEdition) as cRelease,recom.cImage as cImage,(author.cName+' '+author.cSurname) as cAuthor,author.cRole as cRole, recom.nViews as nViews"
            ).OrderByDescending("recom.nViews"
            ).Limit(10)
        
        return BuildRecomByCoResponsibility.ToList()
    
    def GetClassificationRecom(self,idTitle:int) -> list[BookSimpleEntity]:
        BuildRecomByClassification= self.__db.Query()
        BuildRecomByClassification.Match(            
            ).Node("Title","m"
                ).LeftRelationship("ASSIGN_DEWEY"
            ).Node("Classification","cl1"
            ).Where(   
                ).Id("m", idTitle
            ).Match(            
                ).Node("Classification","cl2"
                    ).RightRelationship("ASSIGN_DEWEY"
                ).Node("recom"
            ).Where("cl2.cCode").StartWith().Substring("cl1.cCode",2).And("m <> recom"
            ).Match(# View only         
                ).Node("recom").LeftRelationship("HAS_RESPONSIBILITY","res").Node("per"
            ).With(
                ).Node("recom"
                ).And().Node("cl2"
                ).And().SortObjectCollect("{cName:per.cName, cSurname:per.cSurname, cRole:res.cRole}","cRole").As("author"
            ).Select("ID(recom) as idTitle,recom.cTitle as cTitle,recom.cSubtitle as cSubtitle,recom.cTopics as cTopic,(recom.nReleased + ' '+recom.cEdition) as cRelease,recom.cImage as cImage,(author.cName+' '+author.cSurname) as cAuthor,author.cRole as cRole, recom.nViews as nViews"
            ).OrderByDescending("cl2.cCode,recom.nViews"
            ).Limit(10)
        
        return BuildRecomByClassification.ToList()
    
    def GetTrends(self):
        BuildForTrends= self.__db.Query()
        BuildForTrends.Match(            
            ).Node("Title","recom"                
            ).Where("recom.nViews <> 0 "
            ).Match(# View only         
                ).Node("recom").LeftRelationship("HAS_RESPONSIBILITY","res").Node("per"
            ).With(
                ).Node("recom"
                ).And().SortObjectCollect("{cName:per.cName, cSurname:per.cSurname, cRole:res.cRole}","cRole").As("author"
            ).Select("ID(recom) as idTitle,recom.cTitle as cTitle,recom.cSubtitle as cSubtitle,recom.cTopics as cTopic,(recom.nReleased + ' '+recom.cEdition) as cRelease,recom.cImage as cImage,(author.cName+' '+author.cSurname) as cAuthor,author.cRole as cRole, recom.nViews as nViews"
            ).OrderByDescending("recom.nViews"
            ).Limit(30)
        
        return BuildForTrends.ToList()

    def UpdateViews(self,idTitle:int):
        BuildUpdateViews = self.__db.Query()
        BuildUpdateViews.Match(            
            ).Node("Title","m"
            ).Where(            
                ).Id("m", idTitle
            ).UpdateField("m.nViews","(m.nViews + 1)"
            ).Select("true as lSuccess")
        return BuildUpdateViews.FirstOrDefault()
        
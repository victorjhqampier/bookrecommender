from enum import Enum
class RelationShipEnum(str, Enum):    
    ClassificationToItem = "DEWEY"    
    SerialTitleToItem ="SERIE"
    ResponsibleToItem = "RESPONSIBILITY"
    publisherToItem  = "RELEASE"
    ItemToCopy ="HAVE"
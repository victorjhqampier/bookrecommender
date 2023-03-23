from enum import Enum
class RelationShipEnum(str, Enum):    
    ClassificationToItem = "ASSIGN_DEWEY"    
    SerialTitleToItem ="PART_TO"
    ResponsibleToItem = "HAS_RESPONSIBILITY"
    publisherToItem  = "PUBLISHED"
    ItemToCopy ="HAS_COPY"
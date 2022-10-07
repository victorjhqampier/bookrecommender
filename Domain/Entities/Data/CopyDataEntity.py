from dataclasses import dataclass
from datetime import datetime

@dataclass
class CopyDataEntity:
    idCopy:str
    cCode:str
    cNotation:str
    cLibrary:str
    cLink:str
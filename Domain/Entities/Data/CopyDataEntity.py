from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class CopyDataEntity:
    idCopy:Optional[str]
    # cCode:Optional[str]
    cNotation:str
    cLibrary:str
    cLink:str
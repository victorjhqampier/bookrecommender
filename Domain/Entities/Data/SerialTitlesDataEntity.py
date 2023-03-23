from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class SerialTitlesDataEntity:
    idSerialTitle:Optional[str]
    cTitle:str
    cNumber:Optional[str]
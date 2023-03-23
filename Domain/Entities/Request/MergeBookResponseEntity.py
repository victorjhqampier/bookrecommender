from dataclasses import dataclass
from typing import Optional

@dataclass
class MergeBookResponseEntity:
    idTitle:str
    cTitle:Optional[str]
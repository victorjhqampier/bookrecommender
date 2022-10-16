from dataclasses import dataclass

@dataclass
class AuthDataEntity:       
    cToken:str
    nExpireIn:int
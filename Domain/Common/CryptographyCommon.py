import cryptocode
from Domain.Interfaces.ICryptography import ICryptography

class CryptographyCommon(ICryptography):
    def __init__(self):
        pass

    def CrearPassword(self):
        pass

    def ProbarPassword(self):
        pass
        
    def CifrarCadena(self,cCadena:str, cKey:str):
        return cryptocode.encrypt(cCadena,cKey)

    def DescifrarCadena(self, cCadena:str, cKey:str):
        return cryptocode.decrypt(cCadena,cKey)
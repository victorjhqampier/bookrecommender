import re
from unicodedata import normalize
import hashlib
from Domain.Interfaces.IHelper import IHelper
class HelperCommon(IHelper):
    __StopWords=["a", "ademas", "al", "algo", "asi", "com", "como", "con", "cuando", "de", "del", "desde", "donde", "e", "el", "ella", "ello", "embargo", "en", "entre", "era", "es", "esta", "estaba", "estabamos", "estaban", "estabas", "estado", "estamos", "estan", "estando", "estando", "estar", "estareis", "estaremos", "estaria", "estariamos", "estarian", "estarias", "estas", "este", "esten", "estes", "esto", "estos", "estoy", "estuve", "estuviera", "estuvieramos", "estuvieran", "estuvieras", "estuvieron", "estuviese", "estuviesemos", "estuviesen", "estuvieses", "estuvimos", "estuviste", "estuvo", "fue", "ha", "habia", "han", "hasta", "hay", "he", "la", "las", "les", "lo", "los", "mas", "me", "mi", "mientras", "mucho", "muy", "no", "nos", "nosotros", "nuevo", "o", "otra", "otras", "otro", "para", "parte", "pe", "pero", "por", "porque", "puede", "que", "quien", "se", "ser", "si", "sido", "sin", "sobre", "solo", "son", "su", "sus", "tal", "tambien", "te", "tiene", "todo", "todos", "tu", "tus", "un", "una", "usted", "vez", "y", "ya", "yo"]
    
    def __init__(self):
        pass   

    def GenerateIdentifier(self, cString:str)->str:
        cString = normalize("NFD", cString.lower())
        cString = ''.join([char for char in cString if char.isalnum() or char.isspace()])
        #cString = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", cString, 0, re.I)
        cString = ''.join([word for word in cString.split() if word not in self.__StopWords and len(word) > 1]).strip()
        arrBytes = cString.encode('utf-8')
        objHash = hashlib.sha256(arrBytes)
        return objHash.hexdigest()

    def GenerateIndex(self, cString:str)->str:
        cString = normalize("NFD", cString.lower())
        cString = ''.join(char for char in cString if char.isalnum() or char.isspace())
        arrWords = cString.split()
        arrWords = [word for word in arrWords if word not in self.__StopWords and len(word) > 1]
        return " ".join(sorted(arrWords)).strip()

    def FormateText(self, cString:str)->str:
        if(cString.strip() == ""):
            return ""
        return " ".join(cString.split()).strip()
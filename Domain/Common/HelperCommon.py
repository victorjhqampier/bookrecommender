import re
from unicodedata import normalize
from Domain.Interfaces.IHelper import IHelper
class HelperCommon(IHelper):
    __Words=["a","con","de","al","e","en", "ademas","tal","sus","el","entre","sido","asi","desde","ella","ello","del","es","estas","esto","han","estos","esta","este","ha","pe","com","como","he","la","las","los","les","mas","mi","me","muy","no","o","para","por","que","se","si","son","su","tu","un","una","y","ya","yo","tus","tu","te","lo"]
    
    def __init__(self):
        pass

    def GenerateIdentifier(self, cString:str):
        cString = cString.lower()
        cString = re.sub( r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",normalize( "NFD", cString), 0, re.I)
        temp = cString.split(" ")
        arrTemp = []
        for x in temp:
            if not (x in self.__Words) and len(x) > 2:
                arrTemp.append(x)
        cString = " ".join(arrTemp)        
        cString = ''.join(char for char in cString if char.isalnum())
        return str(hash(cString))
    
    def GenerateIndex(self, cString:str):
        cString = cString.lower()
        cString = re.sub( r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",normalize( "NFD", cString), 0, re.I)
        temp = cString.split(" ")
        arrTemp = []
        for x in temp:
            if not (x in self.__Words) and len(x) > 2:
                arrTemp.append(''.join(char for char in x if char.isalnum()))
        cString = " ".join(arrTemp)        
        return " ".join(cString.split())

    def FormateText(self, cString:str):
        if(cString == ""):
            return ""
        return " ".join(cString.split())
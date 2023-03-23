from Domain.Entities.Response import Response
from Domain.Entities.GlobalError import GlobalError
from Domain.Interfaces.IEasyResponse import IEasyResponse

class EasyResponseCommon(IEasyResponse):

    def EasyErrorRespond(self,cErrorCode:str, cErrorMessage:str, cMessage:str = None)->Response:        
        objErrors = GlobalError(
            code = cErrorCode,
            message = cErrorMessage
        )
        arrErrorMessage = [objErrors]
        return Response(
            success = 0,
            message = 'La petición no pudo completarse debido a un conflicto interno en nuestros servidores' if cMessage == None else cMessage,
            errors = arrErrorMessage
        )

    def EasyListErrorRespond(self,errorList:list, cMessage:str = None)->Response:
        return Response(
            success = 0,
            message = 'La petición no pudo completarse debido a que la solicitud no fue válida' if cMessage == None else cMessage,
            errors= errorList
        )

    def EasyEmptyRespond(self,cMessage:str = None)->Response:
        return Response(
            success = 1,
            message = 'La petición se completó exitosamente, pero su respuesta no tiene ningún contenido' if cMessage == None else cMessage            
        )

    def EasySuccessRespond(self,dataResponse, cMessage:str = None)->Response:
        return Response(
            success = 1,
            message = 'La petición se completó exitosamente' if cMessage == None else cMessage,
            data= dataResponse
        )
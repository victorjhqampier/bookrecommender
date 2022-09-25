from flask.json import jsonify
import jsons

def StatusCode(code:int, object):
    response = jsonify(jsons.dump(object))
    response.status_code = code
    return response
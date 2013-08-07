from bottle import request
from common.request_util import get_request_id

def get_param():
    request_iter=request.GET
    request_params={}
    request_identifier = 'guid'
    for key in request_iter:
        request_params[key]=request_iter.get(key)
    if request.json is not None:
        request_params.update(request.json)
    context_params = {}
    if request_identifier in request_params and request_params[request_identifier] is not None:
        context_params[request_identifier] = request_params.pop(request_identifier)
    else:
        context_params[request_identifier]=get_request_id()   
    return request_params,context_params

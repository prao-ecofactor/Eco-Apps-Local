import thread
from uuid import uuid5,NAMESPACE_DNS
import time
from bottle import request

def get_request_id():
    if request is not None:
        request_iter = request.GET
    request_id = request_iter.get('guid',None)
    if request_id is not None:
        return str(request_id)
    uniqueString =("%s%s" %(time.mktime(time.gmtime()),thread.get_ident()))
    request_id = str(uuid5(NAMESPACE_DNS, uniqueString))
    return request_id
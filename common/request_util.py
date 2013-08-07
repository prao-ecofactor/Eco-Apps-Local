import thread
from uuid import uuid5,NAMESPACE_DNS
import time

def get_request_id():
    uniqueString =("%s%s" %(time.mktime(time.gmtime()),thread.get_ident()))
    return str(uuid5(NAMESPACE_DNS, uniqueString))
# A view for the ReadThermostat API
from common.configuration import config
class Error:
    errorCode=10000
    def __init__(self, errorCode):
        self.errorCode = errorCode
    
    def render(self):
        retval = {}
        retval['errors'] = []
        exception={'msg':"Internal Server Error"}
        exception['msg'] = config.get("error_codes",str(self.errorCode))
        exception['code'] = self.errorCode
        retval['errors'].append(exception)
        return retval
              

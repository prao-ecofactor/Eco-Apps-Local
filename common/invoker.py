# This is our service invoker.  It takes in a request with a standard format, and then decides how to route it based on configuration.
# NOTE: "service" will mean "controller" when it's making internal calls.  However, a "service" may also reside on a different process, 
# or even cause an asynchronous HTTP call to be made.
# Even though remote calls may be asynchronous, the call to 'invoke' will block, with a per-service configured timeout
# In the event of a failed service call, a ServiceException will be raised with details of the failure

# method - a RESTful method of calling in.  One of GET, POST, PUT, or DELETE.  Please resist the temptation to add additional method types.
# service - the name of the service being called
# params - an optional set of parameters.  They'll be understood only by the service being called.  In order to prevent custom logic everywhere
#        for translating between invoked params and what needs to be passed via a webservice call in the future, params must be formatted as
#        a string that is acceptable in a URL.

import common.eflogging as logging
logger = logging.getLogger('invoker')
def invoke( method, service, request_params = None,context_params=None):
    # Parse out and validate the URI
    if method != 'GET' and method != 'POST' and method != 'PUT' and method != 'DELETE':
        raise Exception( "Only RESTful methods are permissible" )
    
#     if uriparams is not None :
#         raise Exception( "parameters must be passed in a format usable directly in a URL")
    
    # TODO: Check config for how to call the service        

    # Execute the call
        # For now, assume direct call
    try:
        return _invokeDirect( method, service,request_params,context_params)
    except Exception as error:
        logger.info('Invocation failed %s' % (error))
        logger.exception(error)
        raise ServiceException( error,"Internal Server Error",100000)

# The _invoke* methods are used to invoke a given service with a given invocation strategy.
# They should blindly pass along (i.e. not manipulate) any Exceptions that happen in the invocation of the method, or in the method itself.
# Typically, this means just not handling them.

# When the controller resides in the same application as us, we can directly invoke the appropriate method
def _invokeDirect( method, service,request_params,context_params):
    # Dynamically load the controller
    module = __import__("services.%s.controllers.%s" % ( service,service ), fromlist='*' )

    # Dynamically fetch the function, based on the method
    methodToCall = getattr( module, method )
    
    # Call it!
    results = methodToCall(request_params,context_params)
    return results

# A common, standardized exception class, so that errors being returned from a service can be done in a uniform manner
class ServiceException( Exception ):
    msg=None
    errorCode=None
    def __init__(self, error,msg,errorCode):
        self.inner_exception = error
        self.msg=msg
        self.errorCode=errorCode

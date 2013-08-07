from common import eflogging
from common.error_view import Error
from common.exception import ServiceException
from common.invoker import invoke

logger=eflogging.getLogger("onboarding")
#Add parameter validation here
def POST(request_params,context_params):
    logger.info("Start of user onboarding")
    location_params = {}
    location_params['locations']= request_params.pop('locations')
    user_params = request_params
    
    try:
        user_response = invoke('POST','user',user_params,context_params)
        location_params['user_id'] = user_response['user_id']
        location_response = invoke('PUT','location',location_params,context_params)
    except ServiceException as ex:
        logger.error("Onboarding failed for user %s %s" %(user_params,location_params))
        return Error(ex.errorCode)

    response={}
    response.update(location_response)
    response.update(user_response)
    logger.info("User onboarding succesful")
    
    return response

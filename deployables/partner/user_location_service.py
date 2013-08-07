from bottle import post,hook,request, Bottle,run,default_app
from common.invoker import invoke
from common.parameter_util import get_param
import logging
from common.request_util import get_request_id

logger = logging.getLogger("create_user_location")
app=default_app()

@app.post('/services/CMCSA/data/v1.0/user')
def create_user_location():
    request_params,context_params=get_param()
    context_params['partner_id']=8
    logger.info("Inside create_user_location")
    result = invoke("POST", "onboarding", request_params,context_params)
    return result

@hook('before_request')
def before_request():
    request.environ['guid']=get_request_id()
    logger.info('Before request to %s %s' % (request.method, request.path))
    # Need to move this to initializing request globals
  
@hook('after_request')
def after_request():
    logger.info('After  request to %s %s' % (request.method, request.path))

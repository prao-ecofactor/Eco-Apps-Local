from common.invoker import ServiceException
from services.region_timezone.models.region_timezone import YahooOAuthTimeZone 
from services.region_timezone.views.read_timezone import ReadYahooTimeZone  
from common.error_view import Error
import json
 
# The ReadYahooTimeZone API 
def GET(requestparams):
    # TODO: validate parameters
    yahooOAuthTimeZone = YahooOAuthTimeZone()
    
    try: 
        load_result = yahooOAuthTimeZone.loadData(requestparams['zip_code'])
    except ServiceException as e:
        error_view = Error(e.errorCode)
        return error_view.render()
    
    if load_result is False:
        raise Exception("invalid zip code given")
 
    try:
        yahooResponse = json.loads(yahooOAuthTimeZone.response)
        if yahooResponse['bossresponse']['responsecode'] != '200':
            raise ServiceException(Exception("Invalid yahoo OAuth response %s." % yahooResponse['bossresponse']['responsecode']), "ZipCode doesn't exist", 10001)
    except (ValueError, KeyError, TypeError):
        print "JSON format error" 
    
    yahoo_timezone_view = ReadYahooTimeZone(yahooResponse)
 
    return yahoo_timezone_view.render()


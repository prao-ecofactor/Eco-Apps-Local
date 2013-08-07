from bottle import get,put, request,hook
from common.invoker import invoke
# from validator.thermostat_validator import validate_update_thermostat
from common.error_view import Error
import logging
from logging import thread

logger = logging.getLogger("test_service")

@get('/ws/consumer/v1.0/thermostat/<thermostat_id:int>')
def readThermostat(thermostat_id=False):
    requestparams={'thermostat_id' :thermostat_id}
    contextparams={}
    if thermostat_id is False:
        raise Exception("thermostat_id cannot be empty")
    result = invoke( 'GET', 'thermostat', requestparams,contextparams)
    return result

@put('/ws/consumer/v1.0/thermostat/<thermostat_id:int>')
def updateThermostat(thermostat_id=None,guid=None):
    requestparams={'thermostat_id':thermostat_id}
    requestparams.update(request.json)
    contextparams={'guid' : requestparams.pop('guid', 0)}
    if request.json is None:
        return Error(10004).render()
#     result = validate_update_thermostat(requestparams)
#     if result is not None:
#         return result
    result =invoke( 'PUT', 'thermostat',requestparams,contextparams)
    return result




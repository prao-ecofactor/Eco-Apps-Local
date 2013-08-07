from common.error_view import Error
from common.invoker import ServiceException
from services.thermostat.models.thermostat import Thermostat
from services.thermostat.views.read_thermostat import ReadThermostat
import logging

logger = logging.getLogger("Thermostat Controller")

# The ReadThermostat API
def GET(requestparams,contextparams):
    # TODO: validate parameters
    thermostat = Thermostat()
    logger.info("Calling update thermostat Model")
    load_result = thermostat.loadData(requestparams['thermostat_id'])
 
    if load_result is False:
        raise Exception("invalid thermostat id given, or other DB problem")
 
    thermostat_view = ReadThermostat(thermostat)
 
    return thermostat_view.render()

#Update thermostat API
def PUT(requestparams,contextparams):
    thermostat = Thermostat()
    try:
        logger.info("Calling update thermostat Model")
        update_result = thermostat.updateThermostatData(requestparams['thermostat_id'],requestparams['name'])
    except ServiceException as e:
        error_view = Error(e.errorCode)
        return error_view.render()
    if(update_result) is False:
        raise Exception("Thermsotat data could not be updated")
# need to format the success response to send 200 OK success
    return None
    
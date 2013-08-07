#Begin of server global configuration and imports
#Please do not add any service imports above this.

from common.configuration import config
from common import eflogging
logger = eflogging.getLogger("rest_service_startup")

#End of Server global configuration imports

#Please add the imports to new rest controller services in this section
#
#   Start of Rest Service Controller import section
#
import deployables.test_harness.test_service
#
#   End of Rest Service Controller import section
#
from bottle import run, Bottle, default_app
run(host=config.get("webserver", "hostname"), port=config.get("webserver", "port"), server="cherrypy", debug=config.get("webserver", "debug"),options={"numthreads":30})

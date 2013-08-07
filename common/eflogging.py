from bottle import request
import logging
import thread
from logging import config
from common.configuration import config as ef_config

class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.
     
    """
 
    def filter(self, record):
        if request is not None and 'guid' in request.environ and request.environ['guid'] is not None:
            record.id = request.environ['guid']
        else:
            record.id = thread.get_ident()
        return True
    
env = ef_config.get('log_env','env')
path = ef_config.get('conf_path','path')
logging.config.fileConfig('%s/default.conf' %(path))
if env == 'dev':
    logging.config.fileConfig('%s/default.conf' %(path))
else:
    logging.config.fileConfig('%s/environment.conf' %(path))

def getLogger(name="apps"):
    if name != "apps" and not name.startswith("apps."):
        name = ("apps.%s" %(name))
    logger = logging.getLogger(name)
    f = ContextFilter()
    logger.addFilter(f)
    logger.info('Inside getLogger')
    return logger

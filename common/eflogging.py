from logging import config
from bottle import request
import logging
import thread
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
    
# app = config.get('loggers','keys')
# level = config.get('logger_root','level')
# handlers = split(config.get('logger_root','handlers'),',')
# handler_list=[]
# #  configuring only the root logger for now
# logger = logging.getLogger()
# logger.setLevel(level)
# for handler in handlers:
#     handler_class = config.get("handler_%s" %(handler.strip()),"class")
#     handler_args = config.get("handler_%s" %(handler.strip()),"args")
#     handler_formatter = config.get("handler_%s" %(handler.strip()), "formatter")
#     format_log = config.get("formatter_%s" %(handler_formatter) , "format")
#     module = __import__("logging.handlers",fromlist='*')
#     class_ = getattr(module, handler_class)
#     handler_entry = class_(*eval(handler_args))
#     format_log = Formatter(format_log)
#     handler_entry.setFormatter(format_log)
#     logger.addHandler(handler_entry)
# 
# logger.info('Logger configuration loaded')
from logging import Formatter
Formatter("test")
env = ef_config.get('log_env','env')
logging.config.fileConfig('conf/default.conf')
if env == 'dev':
    logging.config.fileConfig('conf/default.conf')
else:
    logging.config.fileConfig('conf/environment.conf')

def getLogger(name):
    logger = logging.getLogger(name)
    f = ContextFilter()
    logger.addFilter(f)
    logger.info('Inside getLogger')
    return logger

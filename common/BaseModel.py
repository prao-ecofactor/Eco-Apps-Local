from common.connection_manager import get_connection

class BaseModel(object):
    dbconnection = None
    require_dbconnection=False
    
    def __init__(self,require_dbconnection):
        self.require_dbconnection=require_dbconnection
        self.dbconnection = get_connection()
        
# This method is automatically called when the instance of the class is not longer in use
# This method should not be called explicitly
    def __del__(self):
        self.dbconnection.close()
        
        
# Model needs to find out whether it needs a read or write connection. Loaded from config file.
    
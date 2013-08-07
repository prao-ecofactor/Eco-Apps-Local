from common.db import fetchData, updateData
from common.BaseModel import BaseModel
from common.invoker import ServiceException

# The canonical representation of a physical thermostat, and the home for all thermostat-related methods.
class Thermostat(BaseModel):
    thermostat_id = None
    alt_thermostat_id = None
    thermostat_name = None
    thermostat_model_id = None
    thermostat_model_info = None
    thermostat_model_hvac_info = None
    
    def __init__(self):
        BaseModel.__init__(self,True)
        
    def loadData(self, thermostat_id):
        self.thermostat_id = thermostat_id
        
        # Construct query and params
        sql = (
"""
                SELECT et.thermostat_name, et.thermostat_model_id
                FROM ef_thermostat AS et
                WHERE
                et.thermostat_id = %s
                LIMIT 1
"""     )

        params = ( self.thermostat_id, )

        # Fetch data
        rows = fetchData(self.dbconnection ,sql, params )
        if rows is None or len(rows) == 0:
            return False

        # Populate self
        row = rows[0]
        self.thermostat_name = row[0]
        self.thermostat_model_id = row[1]

        self.loadModelInfo()
        self.loadHVACInfo()

        return True

    def loadModelInfo(self):
        # Construct query and params
        sql = (
"""
                SELECT etm.model_name, etm.temperature_min, etm.temperature_max
                FROM ef_thermostat_model AS etm
                WHERE
                etm.thermostat_model_id = %s
                LIMIT 1
"""     )
        
        params = ( self.thermostat_model_id, )

        # Fetch data
        rows = fetchData( self.dbconnection,sql, params )
        if rows is None or len(rows) == 0:
            return False

        # Populate self
        row = rows[0]
        self.thermostat_model_info = {}
        self.thermostat_model_info['model_name'] = row[0]
        self.thermostat_model_info['temperature_min'] = float(row[1])
        self.thermostat_model_info['temperature_max'] = float(row[2])

    def loadHVACInfo(self):
        # Default is to have both HEAT and COOL present if nothing exists in the DB
        self.thermostat_model_hvac_info = [ 'HEAT', 'COOL' ]
        
        # Construct query and params
        sql = (
"""
                SELECT eths.hvac_stage_type
                FROM ef_thermostat_hvac_stage AS eths
                WHERE
                eths.thermostat_id = %s AND
                hvac_stage = 1
"""     )
        
        params = ( self.thermostat_id ,)

        # Fetch data
        rows = fetchData(self.dbconnection ,sql, params )
        if rows is None or len(rows) == 0:
            return False

        # It's ok if there's no data here; just use the default
        if rows == None or len(rows) == 0:
            return True

        # Populate self
        self.thermostat_model_hvac_info = []
        for row in rows:
            self.thermostat_model_hvac_info.append( row[0] )
        
        return True
    
    def updateThermostatData(self,thermostat_id,thermostat_name):
        self.thermostat_id =  thermostat_id
        self.thermostat_name = thermostat_name
        
        sql = (
               
"""               Update ef_thermostat et
                  Set et.thermostat_name = %s
                  Where 
                  et.thermostat_id = %s
                  
"""

               )
        
        sql1 = (
               
"""               Select count(*) from ef_thermostat et
                  Where 
                  et.thermostat_id = %s
"""

               )
        params1 = ( self.thermostat_id, )
        count = fetchData(self.dbconnection,sql1, params1)
        #Service Exception should be cleaned up may be to not take exception as an argument
        if count[0][0] == 0:
            raise ServiceException(Exception("Thermostat Doesn't Exist"),"Thermostat doesn't exist",10001)
        params = (self.thermostat_name, self.thermostat_id)
        success = updateData(self.dbconnection,sql,params)
        self.dbconnection.commit()
        return success

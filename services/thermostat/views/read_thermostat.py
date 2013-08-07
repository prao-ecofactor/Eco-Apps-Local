# A view for the ReadThermostat API
class ReadThermostat:
    thermostat = None
    def __init__(self, thermostat):
        self.thermostat = thermostat
    
    def render(self):
        retval = {}
        retval['name'] = self.thermostat.thermostat_name
        
        retval['model'] = {}
        if self.thermostat.thermostat_model_info is not None:
            retval['model']['name'] = self.thermostat.thermostat_model_info['model_name']
            retval['model']['minTemperature'] = self.thermostat.thermostat_model_info['temperature_min']
            retval['model']['maxTemperature'] = self.thermostat.thermostat_model_info['temperature_max']

        retval['hvacControl'] = ()
        if self.thermostat.thermostat_model_hvac_info is not None:
            retval['hvacControl'] = self.thermostat.thermostat_model_hvac_info
        
        return retval

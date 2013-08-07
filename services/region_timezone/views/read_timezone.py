# A view for the ReadYahooTimeZone API
class ReadYahooTimeZone:
    yahooAddress = None
    def __init__(self, yahooResponse):
        self.yahooAddress = yahooResponse['bossresponse']['placefinder']
    
    def render(self):
        retval = {}
        results = self.yahooAddress['results'][0]
        
        for key, value in results.iteritems():
            print key, value
            if(key == 'timezone'):
                retval['timezone'] = value 
                break
        
        return retval

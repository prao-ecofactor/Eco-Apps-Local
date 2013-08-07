from common.configuration import config
from common.BaseModel import BaseModel
import oauth.oauth as oauth 
import urllib

#Yahoo!'s OAuth Authorization : Using OAuth with BOSS API
class YahooOAuthTimeZone(BaseModel):
    zip_code = None
    timezone = None
    response = None
   
    def __init__(self):
        BaseModel.__init__(self,True)
        
    def loadData(self, zip_code,):
        self.zip_code = zip_code
        OAUTH_CONSUMER_KEY = config.get("yahoo_boss", "yahoo_consumer_key")
        OAUTH_CONSUMER_SECRET = config.get("yahoo_boss", "yahoo_consumer_secret")
        URL = config.get("yahoo_boss", "yahoo_boss_service_url")
        APP_ID = config.get("yahoo_boss", "yahoo_boss_app_id")

        # Construct parameters
        data = {'appId': APP_ID, 
                'postal': self.zip_code, 
                'flags': 'TJ', 
                'gflags': 'Q'} 
 
        #Create oAuth Consumer 
        consumer = oauth.OAuthConsumer(OAUTH_CONSUMER_KEY, OAUTH_CONSUMER_SECRET)
        
        #OAuth_signature_method=HMAC-SHA1 Ð (specific algorithm used for BOSS API OAuth calls).
        signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()
        
        #Set/SIGN the OAuthRequest   
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token=None, http_method='GET', http_url=URL, parameters=data)
        oauth_request.sign_request(signature_method_hmac_sha1, consumer, "")
        complete_url = oauth_request.to_url()
        
        #Response
        result = urllib.urlopen(complete_url)
        self.response = result.read();
 
        print self.response
        return True
    

class ServiceException( Exception ):
    msg=None
    errorCode=None
    def __init__(self,msg,errorCode):
        self.msg=msg
        self.errorCode=errorCode
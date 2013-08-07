# This is a wrapper around the MySQLdb functionality, so that logic related to the mechanics of 
# querying can be separated from the models that ask for the data. 

# Connection pooling can happen here, as can standardized logging messages for failure modes

import logging

# A thin wrapper around cursor.execute().  See http://www.python.org/dev/peps/pep-0249/ for more details on this method
logger = logging.getLogger('db')
def fetchData(connection,sql, params=None):
    cursor = connection.cursor()
    cursor.execute(sql, params)
    data = cursor.fetchall()
    return data

def updateData(connection,sql,params=None):
    "used to update data to database"
    if connection is None:
        raise Exception("A connection to database is needed for updating the database")
    logger.debug("Updating data to database")
    cursor=connection.cursor()
    cursor.execute(sql, params)
    return True
      
        
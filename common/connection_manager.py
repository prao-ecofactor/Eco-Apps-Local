from common.configuration import config
import mysql.connector as dbconnector
import eflogging

logger = eflogging.getLogger('ConnectionManager')

ef_host = config.get("database_master", "host")
ef_user = config.get("database_master", "user")
ef_password = config.get("database_master", "password")
ef_database = config.get("database_master", "database")
ef_port=config.get("database_master","port")

ef_host_ro = config.get("database_readonly", "host")
ef_user_ro = config.get("database_readonly", "user")
ef_password_ro = config.get("database_readonly", "password")
ef_database_ro = config.get("database_readonly", "database")
ef_port_ro = config.get("database_readonly","port")

def get_connection():
    try:
        connection = dbconnector.connect(user=ef_user_ro, password=ef_password_ro,
                               host=ef_host_ro,port=ef_port_ro,
                              database=ef_database_ro)
    except Exception as e:
        logger.error("Cannot get a database connection %s" %(e))
        raise Exception("Cannot get a database conneciton")
    return connection

def get_connection_ro():
    try:
        connection = dbconnector.connect(user=ef_user, password=ef_password,
                               host=ef_host,port=ef_port,
                              database=ef_database)
    except Exception as e:
        logger.error("Cannot get a database connection %s" %(e))
        raise Exception("Cannot get a database connection")
    return connection



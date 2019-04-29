import mysql.connector
import configparser

class AppDB:

    __instance = None
    db = None
    config = configparser.ConfigParser()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AppDB.__instance == None:
            AppDB()
        return AppDB.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if AppDB.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AppDB.__instance = self
        self.config.read('config.ini')
        self.db = mysql.connector.connect(
            host=self.config.get('MYSQL', 'host'),
            port=self.config.get('MYSQL', 'port'),
            user=self.config.get('MYSQL', 'user'),
            passwd=self.config.get('MYSQL', 'password'),
            database=self.config.get('MYSQL', 'database'),
            auth_plugin='mysql_native_password'
        )

    def getDatabase(self):
        return self.db

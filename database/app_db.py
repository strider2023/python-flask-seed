import mysql.connector

class AppDB:

    __instance = None
    mydb = None

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
        self.mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='upasthiti',
            passwd='upasthiti321',
            database='upasthiti-backend',
            auth_plugin='mysql_native_password'
        )

    def getDatabase(self):
        return self.mydb

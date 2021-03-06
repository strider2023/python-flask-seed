from database.app_db import AppDB

class UserQueries:
    'All queries for User Table'
    db = None
    dbcursor = None

    def __init__(self):
        self.db = AppDB.getInstance()
        self.dbcursor = self.db.getDatabase().cursor()

    def getUsers(self):
        self.dbcursor.execute("SELECT * FROM `upasthiti-backend`.user WHERE status = 0")
        myresult = self.dbcursor.fetchall()
        return myresult

    def getUser(self, id):
        self.dbcursor.execute("SELECT * FROM `upasthiti-backend`.user WHERE id=" + id)
        myresult = self.dbcursor.fetchall()
        return myresult
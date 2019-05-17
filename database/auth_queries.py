from database.app_db import AppDB

class AuthQueries:
    'All queries for Authentication'
    db = None
    dbcursor = None

    def __init__(self):
        self.db = AppDB.getInstance()
        self.dbcursor = self.db.getDatabase().cursor()

    def authenticateUser(self, email, password):
        self.dbcursor.execute("SELECT * FROM `upasthiti-backend`.user WHERE email='" + email + "' AND password='" + password + "' AND status=0")
        myresult = self.dbcursor.fetchall()
        return myresult
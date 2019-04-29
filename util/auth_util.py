import jwt
import configparser

class AuthUtil:

    config = configparser.ConfigParser()

    def __init__(self):
        self.key = self.config.get('JWT', 'key')

    def createToken(self, input):
        return jwt.encode(input, self.key, algorithm='HS256')

    def getDecodedToke(self, input):
        return jwt.decode(input, self.key, algorithms=['HS256'])
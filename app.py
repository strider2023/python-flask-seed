from flask import Flask
from util.swagger_util import api

from services.authentication_services import ns as auth_namespace
from services.user_services import ns as user_namespace
from services.health_check_services import ns as health_check_namespace

app = Flask(__name__)
api.init_app(app)

api.add_namespace(health_check_namespace)
api.add_namespace(auth_namespace)
api.add_namespace(user_namespace)

if __name__ == "__main__":
    app.run()
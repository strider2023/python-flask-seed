from flask_restplus import Resource
from util.swagger_util import api

ns = api.namespace('health_check', description='Check for service running status')


@ns.route("/")
class HealthCheck(Resource):

    def get(self):
        return {
            "status": "Server Running"
        }

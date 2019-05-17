from flask_restplus import Resource, marshal
from util.swagger_util import api
from util.auth_util import AuthUtil
from database.user_queries import UserQueries
from models.user_models import user_model as userModel

ns = api.namespace('user', description='User account services')

db = UserQueries()
authUtil = AuthUtil()

@ns.route("/<int:id>")
class User(Resource):

    @ns.marshal_with(userModel)
    @ns.doc(security='apikey')
    @ns.doc(responses={200: 'OK', 400: 'Invalid Argument', 403: 'Not Authorized', 500: 'Mapping Key Error'})
    def get(self, id):
        try:
            result = db.getUser(id)
            response = {
                'firstname': result[0][4],
                'lastname': result[0][6],
                'email': result[0][1],
                'phone': result[0][2],
                'token': authUtil.createToken({'id': result[0][0]})
            }
            return marshal(response, userModel)
        except KeyError as e:
            ns.abort(500, e.__doc__, status="Please check your request body.", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Invalid argument.", statusCode="400")


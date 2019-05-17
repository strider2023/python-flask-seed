from flask import request
import hashlib
from flask_restplus import Resource, marshal
from util.swagger_util import api
from database.auth_queries import AuthQueries
from models.login_model import login_model as loginModel
from models.user_models import user_model as userModel
from util.auth_util import AuthUtil

ns = api.namespace('auth', description='Authentication services')

db = AuthQueries()
authUtil = AuthUtil()

@ns.route("/login")
class UserLogin(Resource):

    @ns.expect(loginModel)
    @ns.marshal_with(userModel)
    @ns.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def post(self):
        try:
            result = db.authenticateUser(request.json['username'], hashlib.md5(request.json['password'].encode("utf")).hexdigest())
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
            ns.abort(400, e.__doc__, status="Please provide username and password.", statusCode="400")

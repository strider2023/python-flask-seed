from flask_restplus import fields, Resource
from util.swagger_util import api

ns = api.namespace('auth', description='Authentication services')

login_model = api.model('Login Model', {
    'username': fields.String,
    'password': fields.String,
})

@ns.route("/login")
class UserLogin(Resource):

    @ns.expect(login_model)
    @ns.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def post(self):
        try:
            api.abort(400)
            return {
                "status": "Server Running"
            }
        except KeyError as e:
            ns.abort(500, e.__doc__, status="Could not save information", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Could not save information", statusCode="400")

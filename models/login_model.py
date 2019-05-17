from flask_restplus import fields
from util.swagger_util import api

login_model = api.model('Login Model', {
    'username': fields.String(required=True, description='User email', help="Username cannot be blank."),
    'password': fields.String(required=True, description='User password', help="Password cannot be blank.")
})

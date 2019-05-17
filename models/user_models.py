from flask_restplus import fields
from util.swagger_util import api

user_model = api.model('User Model', {
    'firstname': fields.String(required=True, description='User first name', help="Username cannot be blank."),
    'lastname': fields.String(required=True, description='User last name', help="Password cannot be blank."),
    'email': fields.String(required=True, description='User email', help="Password cannot be blank."),
    'phone': fields.String(required=True, description='User phone', help="Password cannot be blank."),
    'token': fields.String(required=True, description='Header token', help="Token cannot be blank."),
})

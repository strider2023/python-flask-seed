from flask_restplus import fields
from util.swagger_util import api

user_model = api.model('User Data Model', {
    'firstname': fields.String(required=True, description='User first name'),
    'lastname': fields.String(required=True, description='User last name'),
    'email': fields.String(required=True, description='User email'),
    'phone': fields.String(required=True, description='User phone')
})
from werkzeug.datastructures import FileStorage
from flask_restplus import fields
from util.swagger_util import api

user_model = api.model('User Data Model', {
    'firstname': fields.String(required=True, description='User first name'),
    'lastname': fields.String(required=True, description='User last name'),
    'email': fields.String(required=True, description='User email'),
    'phone': fields.String(required=True, description='User phone')
})

upload_image_model = api.parser()
upload_image_model.add_argument('image_name', location='form', type='string', required=True)
upload_image_model.add_argument('file', location='files', type=FileStorage, required=True)
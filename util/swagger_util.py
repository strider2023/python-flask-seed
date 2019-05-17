from flask_restplus import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api = Api(version="1.0",
          title="Python Seed Application",
          description="Python seed application with Flask, Swagger, JWT and MySQL",
          authorizations=authorizations)

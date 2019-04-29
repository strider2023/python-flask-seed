from flask import Flask
from services.user_services import users_api

app = Flask(__name__)
app.register_blueprint(users_api)

@app.route("/health_check")
def health():
    return "All Good!"

if __name__ == "__main__":
    app.run()
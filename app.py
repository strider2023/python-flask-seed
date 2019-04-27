from flask import Flask
from services.employee_services import employees_api

app = Flask(__name__)
app.register_blueprint(employees_api)

@app.route("/health_check")
def health():
    return "All Good!"

if __name__ == "__main__":
    app.run()
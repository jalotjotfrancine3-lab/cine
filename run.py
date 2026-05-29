from flask import Flask
from routes.build_routes import build

app = Flask(__name__)

app.register_blueprint(build)

if __name__ == "__main__":
    app.run(debug=True)
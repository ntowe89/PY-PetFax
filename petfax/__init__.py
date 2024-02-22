from flask import Flask
from . import pets
from . import facts

#factory
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        print("This is my console")
        return "This is my home page"

    app.register_blueprint(pets.bp)

    app.register_blueprint(facts.bp)

    return app
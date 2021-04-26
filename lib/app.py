from flask import Flask
from lib.interface.chain import chain
from lib.interface.mineration import mineration
from lib.interface.validation import validation

app = Flask(__name__)

app.register_blueprint(chain)
app.register_blueprint(mineration)
app.register_blueprint(validation)
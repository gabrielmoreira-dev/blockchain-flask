from flask import Flask
from lib.api.chain import chain
from lib.api.mineration import mineration
from lib.api.node import node
from lib.api.transaction import transaction
from lib.api.validation import validation

app = Flask(__name__)

app.register_blueprint(chain)
app.register_blueprint(mineration)
app.register_blueprint(node)
app.register_blueprint(transaction)
app.register_blueprint(validation)
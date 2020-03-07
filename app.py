from flask import Flask, request

from flask_restful import Resource, Api
from function import Fun
from function1 import funky

app = Flask(__name__)
api = Api(app)

api.add_resource(Fun, '/entry')
api.add_resource(funky,'/exit')

app.run(port=5000, debug=True)
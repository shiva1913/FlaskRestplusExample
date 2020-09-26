from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
ns_conf = api.namespace('FRP_Example', description='Flask Restplus example testing apis')


from resources.ExampleOne import *
from resources import ExampleTwo

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from app import *

@ns_conf.route('/ExampleOne')
class ExampleOne(Resource):
    def get(self):
        return {'hello': 'from example one'}
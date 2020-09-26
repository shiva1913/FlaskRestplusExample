from app import *

@ns_conf.route('/ExampleTwo')
class ExampleTwo(Resource):
    def get(self):
        return {'hello': 'from example Two'}
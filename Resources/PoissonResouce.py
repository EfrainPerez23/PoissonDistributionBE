from flask_restful import Resource, reqparse
from Util.BodyParser import BodyParser
from Distribution.Poisson.Poisson import Poisson



class PoissonResource(Resource):

    def post(self):
        data = BodyParser.bodyParser([
            {
                'key': 'lambda',
                '_type': str,
                '_required': True,
                '_help': 'lambda cannot be blank!'
            },
            {
                'key': 'size',
                '_type': int,
                '_required': True,
                '_help': 'size cannot be blank!'
            },
        ])
        poissonObj = Poisson()
        return {'poissonValues': poissonObj.inversePoisson(data['size'], float(data['lambda'])) }

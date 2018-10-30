from flask_restful import Resource, reqparse
from Util.BodyParser import BodyParser
from Distribution.Poisson.Poisson import Poisson



class PoissonResource(Resource):

    def post(self):
        data = BodyParser.bodyParser([
            {
                'key': 'miu',
                '_type': int,
                '_required': True,
                '_help': 'miu cannot be blank!'
            },
            {
                'key': 'size',
                '_type': int,
                '_required': True,
                '_help': 'size cannot be blank!'
            },
        ])
        poissonObj = Poisson()
        poissonValues = poissonObj.calculate(data['size'], data['miu'])
        accumulateValues = poissonObj.accumulate(poissonValues, data['size'])
        return {'poissonValues': poissonObj.poissonValues(data['size'], data['miu'], accumulateValues)}
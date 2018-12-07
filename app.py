from flask import Flask, jsonify
from flask_restful import Api

# Resources
from Resources.PoissonResouce import PoissonResource
app = Flask(__name__)


# Load config File
app.secret_key = 'numeros-aleatorios'

# Init Rest API endpoints
api = Api(app)
api.add_resource(PoissonResource, '/poisson')

# Main function
if __name__ == '__main__':
    app.run()

from flask import request, app, Blueprint
from flask_restful import Resource, Api
from model.predict import PredictionModel

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api/v1")

class Model(Resource):

    def get(self):
        """
        Uses the model to predict and output the results in json.
        :return:
        """

        query = request.get_json()
        model = PredictionModel()
        results = 0
        try:
            results = model.predict(query)
        except Exception as e:
            results = str(e)
            pass

        response = {"response": results}
        return response


api.add_resource(Model, "/model")

from flask import request, app, Blueprint, Response, jsonify
from flask_restful import Resource, Api
import json
from middleware.restaurant import validate_restaurant_id, validate_restaurant_name, validate_restaurant_postcode
from model.restaurant import RestaurantModel

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api/v1")

class RestaurantId(Resource):

    def get(self, id):
        """
        Uses the restaurant to get a restaurant
        :return:
        """

        if not validate_restaurant_id(id):
            results = "Error"
            message = json.dumps(results)
            resp = Response(message, status=400, mimetype='application/json')
            return resp

        restaurant = request.get_json()
        res = RestaurantModel()
        results = res.get_restaurant(id)
        message = json.dumps(results)
        resp = Response(message, status=results['statusCode'], mimetype='application/json')
        return resp

class RestaurantName(Resource):

    def get(self, name):
        """
        Uses the restaurant to get a restaurant
        :return:
        """

        if not validate_restaurant_name(name):
            results = "Error"
            message = json.dumps(results)
            resp = Response(message, status=400, mimetype='application/json')
            return resp

        restaurant = request.get_json()
        res = RestaurantModel()
        results = res.get_restaurant(name)
        message = json.dumps(results)
        resp = Response(message, status=results['statusCode'], mimetype='application/json')
        return resp

class RestaurantPostcode(Resource):

    def get(self, postcode):
        """
        Uses the restaurant to get a restaurant
        :return:
        """

        if not validate_restaurant_postcode(postcode):
            results = "Error"
            message = json.dumps(results)
            resp = Response(message, status=400, mimetype='application/json')
            return resp

        restaurant = request.get_json()
        res = RestaurantModel()
        results = res.get_restaurant(postcode)
        message = json.dumps(results)
        resp = Response(message, status=results['statusCode'], mimetype='application/json')
        return resp      

class Restaurant(Resource):

    def post(self):
        """
        Uses the restaurant to get a restaurant
        :return:
        """

        '''if validate_restaurant(request.get_json()) == 0:
            results = "Error"
            message = json.dumps(results)
            resp = Response(message, status=400, mimetype='application/json')
            return resp'''

        restaurant = request.get_json()
        res = RestaurantModel()
        results = res.create_restaurant(restaurant)
        message = json.dumps(results)
        resp = Response(message, status=results['statusCode'], mimetype='application/json')
        return resp

class Post(Resource):

    def post(self):

        return ''


api.add_resource(RestaurantId, "/restaurant/:id")
api.add_resource(RestaurantName, "/restaurant/:name")
api.add_resource(RestaurantPostcode, "/restaurant/:postcode")
api.add_resource(Restaurant, "/restaurant")
api.add_resource(Post, "/post")
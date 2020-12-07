
from flask import request, app, Blueprint, Response, jsonify
from flask_restful import Resource, Api
import json
from middleware.restaurant import validate_restaurant_id, validate_restaurant_name, validate_restaurant_postcode
from model.restaurant import RestaurantModel

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix="/api/v1")

class RestaurantById(Resource):

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
        results = res.get_restaurant_by_name(id)
        message = json.dumps(results)
        resp = Response(message, status=200, mimetype='application/json')
        return resp

class RestaurantsByNameAPI(Resource):

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
        results = res.get_restaurant_by_name(name)
        response = json.dumps(results)
        resp = Response(response, status=200, mimetype='application/json')
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
        resp = Response(message, status=200, mimetype='application/json')
        return resp

class Post(Resource):

    def post(self):

        return ''


api.add_resource(RestaurantById, "/restaurant/<int:id>", endpoint='restuarnt_by_id')
api.add_resource(RestaurantsByNameAPI, "/restaurants/<name>", endpoint='restaurants_by_name')
api.add_resource(Restaurant, "/restaurant")
api.add_resource(Post, "/post")
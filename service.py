# -*- coding: utf-8 -*-
import json
import access
import status
import logging

def handler(event, context):
    # Handler function
    if 'httpMethod' in event:
        method = event["httpMethod"]
        if "GET" in method:
            print("Get Request")
            return getRestaurant(event)
        elif "POST" in method:
            print("Post Request")
            return createRestaurant(event)

def getRestaurant(event):
    if 'queryStringParameters' in event and 'restaurant' in event["queryStringParameters"]:
        # Check we have parameters
        request = event["queryStringParameters"]["restaurant"]
        try:
            db = access.Access_Db()
            db.getRestaurant(request)
            return status.success()
        except ValueError:
            print("Request was not fully provided")
            return status.failure_parameters()   
    else:
        return status.failure_parameters()


def createRestaurant(event):
    if 'queryStringParameters' in event and 'restaurant' in event["queryStringParameters"]:
        # Check we have parameters
        message = event["queryStringParameters"]["restaurant"]
        #try:
        db = access.Access_Db()
        print(message)
        return db.createRestaurant(message)
        #except ValueError:
         #   print("Restaurant was not provided")
          #  return status.failure_parameters()   
    else:
        return status.failure_parameters()


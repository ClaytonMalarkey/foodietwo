
from functools import wraps

from flask import jsonify, make_response, request

from dbhelpers import run_statement

def client_token_required(func):
    def client_wrapper(*args, **kwargs):
    
        token = request.headers.get("token")
        print("token", token)
        # if (token == None or token == ""):
        #     return make_response(jsonify("Please provide a token"), 403)
    
        # result = run_statement('CALL validate_restaurant_token(?)', [token])
    
        # if (len(result) == 0):
        #     return make_response(jsonify("invalid token, please login"), 403)
        
        response = func(*args, **kwargs) 
        return response
    client_wrapper.__name__ = func.__name__
    return client_wrapper
 

from flask import Flask, jsonify, request, make_response
from dbhelpers import run_statement
from middlewares.auth import client_token_required

app = Flask(__name__)

@app.get("/test")
def get_cars():
 try:
  return make_response(jsonify("running"), 200)

 except:
  return make_response(jsonify("Error"), 400)

 
@app.post("/api/client")
def create_client():
 try:
  
  # This is how you get values from body
  email = request.json.get('email')
  first_name  = request.json.get('first_name')
  last_name  = request.json.get('last_name')
  image_url  = request.json.get('image_url')
  username  = request.json.get('username')
  password  = request.json.get('password')

  cursor = cnx.cursor(buffered=True)
  result = run_statement('CALL create_client(?,?,?,?,?,?)', [email, password, first_name, last_name, image_url, username ])

  return make_response(jsonify(result), 200)
 except:
  return make_response(jsonify("Error"), 400)

@app.delete("/api/client")
def delete_client():
 try:
    id = request.json.get('id');
    result = run_statement('CALL delete_client(?)'[id])
    return make_response(jsonify(result), 200)
 except:
    return make_response(jsonify("error"), 400)
 
@app.get("/api/client")
def get_client():
 try:
    id = request.json.get('id');
    result = run_statement('CALL get_client(?)'[id])
    return make_response(jsonify(result), 200)
 except:
    return make_response(jsonify("error"), 400)

@app.patch("/api/client")
@client_token_required
def update_client():
 try:
    id = request.json.get('id');
    print(id)
    email = request.json.get('email')
    first_name  = request.json.get('first_name')
    last_name  = request.json.get('last_name')
    image_url  = request.json.get('image_url')
    username  = request.json.get('username')
    password  = request.json.get('password')
    print(username + password + image_url +first_name + last_name)
    result = run_statement('CALL upate_client(?)'[id])
    return make_response(jsonify(result), 200)
 except:
    return make_response(jsonify("error"), 400)
 
@app.get("/api/client-login")
@client_token_required
def get_client_login():
   try:
      id = request.json.get('id')
      token = request.json.get('token')
      result = run_statement('CALL insert_session(?)'[id])
      return make_response(jsonify(result), 200)
   except:
      return make_response(jsonify("error"), 400)
   
@app.delete("/api/client-login")
@client_token_required
def delete_client_session():
   try:
      token = request.json.get('token')
      result = run_statement('CALL delete_session(?)'[id])
      return make_response(jsonify(result), 200)
   except:
      return make_response(jsonify("error"), 400)


@app.post("/api/restaurant")
def create_restaurant():
 try:
  
  # This is how you get values from body
   name = request.json.get('name')
   email  = request.json.get('email')
   password  = request.json.get('password')
   is_Verified = request.json.get('is_Verified')
   verification_token = request.json.get('verifcation_token')
   image_url = request.json.get('image_url')
   banner_url = request.json.get('banner_url')

   result = run_statement('CALL create_restaurant(?,?,?,?,?,?,?)', [name, email, password, is_Verified, verification_token, image_url, banner_url])

   return make_response(jsonify(result), 200)
 except:
   return make_response(jsonify("Error"), 400)


app.run(debug=True)

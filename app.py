from flask import Flask, jsonify, request, make_response
from dbhelpers import run_statement

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

  result = run_statement('CALL create_client(?,?,?,?,?,?)', [email, password, first_name, last_name, image_url, username ])

  return make_response(jsonify(result), 200)
 except:
  return make_response(jsonify("Error"), 400)

@app.delete("/api/client")
def delete_client():
 try:
    id = request.json.get('id');
    result - run_statement('CALL delete_client(?)'[id])
    return make_response(jsonify(result), 200)
 except:
    return make_response(jsonify("error"), 400)
 
@app.get("/api/client")
def get_client():
 try:
    id = request.json.get('id');
    result - run_statement('CALL get_client(?)'[id])
    return make_response(jsonify(result), 200)
 except:
    return make_response(jsonify("error"), 400)

@app.patch("/api/client")
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




app.run(debug=True)

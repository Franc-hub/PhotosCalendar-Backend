from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongo'

mongo = PyMongo(app)

@app.route("/",methods=['GET'])
def test():
    return {"Message":"ok"}

@app.error_handler(404)
def not_found(error = None):
    return jsonify(
        {"message" : "resource not found" + request.url,
         "status":   404 }) 

@app.route("/users",methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    if username and email and password  is not None:
        hash_password = generate_password_hash(password)
        id = mongo.db.users.insert({
                 'username': username,'email':email, 'password':hash_password
        })
   
        return jsonify (id = str(id), username = username, password=password, email  =email) ,201
        
    else:
        {"message":"You didn't complete all the data"}


if __name__ == "__main__":
    app.run(debug=True)
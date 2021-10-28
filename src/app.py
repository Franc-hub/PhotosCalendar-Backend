from flask import Flask,request,jsonify,Response
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash
from bson import json_util,ObjectId



app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongo'

mongo = PyMongo(app)

@app.route("/",methods=['GET'])
def test():
    return {"Message":"ok"}

@app.errorhandler(404)
def not_found(error = None):
    res =  jsonify(
        {"message" : "Resource Not found" + request.url ,
         "status":   404 }
         )
    

    return res, 404 

# CRUD USER


@app.route("/users",methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    if username and email and password  is not None and mongo.db.users.find_one(username != username and email != email):

        hash_password = generate_password_hash(password)
        id = mongo.db.users.insert({
                 'username': username,'email':email, 'password':hash_password
        })
    
        return jsonify (id = str(id), username = username, password=password, email  =email) ,201
    
    else:
        return not_found()

@app.route("/users",methods=['GET'])
def get_all_users():

    users = mongo.db.users.find()
    res = json_util.dumps(users)
    return Response(res,mimetype='application/json'), 200

@app.route("/users/<id>",methods=['GET'])
def get_one_user(id):
    user = mongo.db.users.find_one({'_id':ObjectId(id)})
    res = json_util.dumps(user)
    return Response(res,mimetype='application/json'), 200

@app.route("/users/<id>",methods=['DELETE'])
def delete_one_user(id):
    if id == True:
        mongo.db.users.delete_one({'_id':ObjectId(id)})
        res = jsonify({"message": "User " + id+ "was Delated sucessfully"}),202
        return res

    else:
        return not_found()


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongo'

mongo = PyMongo(app)

@app.route("/",methods=['GET'])
def test():
    return {"Message":"emilia"}



@app.route("/users",methods=['POST'])
def create_user():
    print(request.json)

    return{"message":"Found"}


if __name__ == "__main__":
    app.run(debug=True)
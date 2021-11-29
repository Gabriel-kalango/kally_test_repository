import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity

from resources.user import registeruser
from resources.item import Item,Itemlist
from resources.store import Store,Storelist
app=Flask(__name__)
DATABASE_URL="postgres://gbcjspxtyhnytb:e463bc9c77ae037cb0ea6c6e4113f8d218b30bdf523e580f840709ed8c3e27d0@ec2-34-192-41-115.compute-1.amazonaws.com:5432/deodntnq4be4bt"
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("sqlite:///data.db",'DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key="kally"
api=Api(app)
jwt=JWT(app,authenticate,identity)


api.add_resource(registeruser,"/register")
api.add_resource(Item,"/item/<string:name>")
api.add_resource(Itemlist,"/items")
api.add_resource(Store,"/store/<string:name>")
api.add_resource(Storelist,"/stores")

if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)

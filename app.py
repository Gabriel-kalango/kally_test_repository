from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from flask_jwt import JWT
from resources.user import registeruser
from resources.item import Item,Itemlist
from resources.store import Store,Storelist
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
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

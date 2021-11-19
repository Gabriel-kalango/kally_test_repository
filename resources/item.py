from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import Item_model

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="This field can't be left blank")
    parser.add_argument("store_id",
        type=int,
        required=True,
        help="an item must have a store id")

    @jwt_required()   
    def get(self,name):
        item =Item_model.find_by_name(name)
        if item:
            return item.json()
        return {"message":"item not found"},404
    


    def post(self,name):
        if Item_model.find_by_name(name):
            return {"message":f"item with the name {name}, already exist"},400

        data=Item.parser.parse_args()

        item=Item_model(name,**data)
        try:
            item.save_to_db()
        except:
            return {"message":"an error occured while posting this item"},500

        return item.json(),201




    def delete(self,name):
        item=Item_model.find_by_name(name)
        if name:
            item.delete_from_db()
        return {"message":"item has been deleted"}


    def put(self,name):
        data=Item.parser.parse_args()
        item=Item_model.find_by_name(name)
        if item is None:
            item=Item_model(name,**data)
        else:
            item.price=data["price"]

        item.save_to_db()
        return item.json()

class Itemlist(Resource):
    def get(self):
        return {"items":[item.json() for item in Item_model.query.all()]}

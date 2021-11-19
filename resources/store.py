from flask_restful import Resource
from models.store import Store_model

class Store(Resource):
    def get(name):
        store=Store_model.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message":f"store with the name {name} , doesnt exist"}

    def post(name):
        if Store_model.find_by_name(name):
            return {"message ":"store exists already"},400
        store=Store_model(name)
        

        try:
            store.save_to_db()
                
        except:
            return{"message":"store was not created"},500
        return store.json()


    def delete(name):
        store=Store_model.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message":"store has been deleted"},200



class Storelist(Resource):
    def get():
        return {"store":[store.json() for store in Store_model.query.all()]} 
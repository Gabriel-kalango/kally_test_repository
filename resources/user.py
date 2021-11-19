
from flask_restful import Resource,reqparse
from models.user import UserModel
class registeruser(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username",
    type=str,
    required=True,
    help="this field must be filled ")

    parser.add_argument("password",
    type=str,
    required=True,
    help="this field must be filled ")
    


    def post(self):
        data= registeruser.parser.parse_args()
        if UserModel.find_byusername(data["username"]):
            return {"message":"username already exist"},400
        user=UserModel(**data)
        user.savetodb()
        return {"message":"user has been succesfully created"},201
import sqlite3
from  flask_restful   import Resource,reqparse
from models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help="This field can not be blank!"
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help="This field can not be blank!"
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exsits."}  
        
        connection = sqlite3.connect("data.db")
        cursor =connection.cursor()

        query = "INSERT INTO users VALUES(NULL,?,?)"
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.commit()

        return {"message":"User successfully created."}, 201

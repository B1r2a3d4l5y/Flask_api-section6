import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt   import jwt_required
from models.item import ItemModel




class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument ('price',
       type = float,
       required = True,
       help ='This field can not be blank!'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

   

    def post(self, name):
        if ItemModel.find_by_name(name): error {
	"resource": "/c:/Users/User/Desktop/section 6/code/resources/item.py",
	"owner": "_generated_diagnostic_collection_name_#1",
	"code": {
		"value": "reportUndefinedVariable",
		"target": {
			"$mid": 1,
			"external": "https://github.com/microsoft/pylance-release/blob/main/DIAGNOSTIC_SEVERITY_RULES.md#diagnostic-severity-rules",
			"path": "/microsoft/pylance-release/blob/main/DIAGNOSTIC_SEVERITY_RULES.md",
			"scheme": "https",
			"authority": "github.com",
			"fragment": "diagnostic-severity-rules"
		}
	},
	"severity": 4,
	"message": "\"ItemModel\" is not defined",
	"source": "Pylance",
	"startLineNumber": 24,
	"startColumn": 12,
	"endLineNumber": 24,
	"endColumn": 21
}
    
            return {"message": "An item with name '{}' already exits".format(name)}, 400

        data = Item.parser.parse_args()

        item =  ItemModel = (name, data['price'])

        try:
            item.insert()
        except:
            return {"message":"An error has occured inserting the item" }, 500
        return item.json(), 201

    
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM  items WHERE name = ?"
        cursor.execute(query,(name,))

        connection.commit()
        connection.close()
        return {"message": "Item deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name,data['price'])
        if item is None:
            try:

           
                 updated_item.insert()
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:

                updated_item.update()
            except:
                return {"message": "An error occurred inserting the item."},500 
        return updated_item.json()
   

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        items = []
        result = cursor.execute(query)
        for row in result:
            items.append({'name': row[0], 'price':row[1]})


        connection.close()
        return {'items': items}


   

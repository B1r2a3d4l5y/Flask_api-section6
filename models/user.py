mport sqlite3

class UserModel:

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connecton = sqlite3.connect('data.db')
        cursor = connecton.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connecton.close()
    
    @classmethod
    def find_by_id(cls, _id):
        connecton = sqlite3.connect('data.db')
        cursor = connecton.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connecton.close()
        return user

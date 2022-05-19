from db import Db


class UserModel():
    def query(self, username, password):
        queries = []
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        queries.append({"sql": sql, "bind": [username, password]})
        db = Db.get_instance()
        res = db.transactional(queries)

        if res:
            return True
        else:
            return False

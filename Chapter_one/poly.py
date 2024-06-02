class SQLightDatabase:
    def connect(self):
        print(f'Connecting to SQLightDatabase')

    def get_users(self):
        print(f'get users with SQL')


class MongoDatabase:
    def connect(self):
        print(f'Connecting to MongoDatabase')

    def get_users(self):
        print(f'get users with no SQL')


class PostgreDatabase:
    def connect(self):
        print(f'Connecting to PostgreDatabase')

    def get_users(self):
        print(f'get users with SQL')


class Server:
    def get_users(self, db):
        # db = SQLightDatabase()
        db.connect()
        users = db.get_users()
        return users


def get_from_config():
    print(f'read config')
    return PostgreDatabase()


if __name__ == '__main__':
    server = Server()
    server.get_users(get_from_config())

from sqlalchemy import create_engine

class SQLConnector:
    def __init__(self, db_type, username, password, host, port, database):
        self.db_type = db_type
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None

    def connect(self):
        if self.db_type == 'mysql':
            self.engine = create_engine(f'mysql+mysqlconnector://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}')
        elif self.db_type == 'postgresql':
            self.engine = create_engine(f'postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}')
        elif self.db_type == 'sqlite':
            self.engine = create_engine(f'sqlite:///{self.database}')
        else:
            raise ValueError("Unsupported database type")
        return self.engine.connect()

    def execute_query(self, query):
        with self.engine.connect() as connection:
            result = connection.execute(query)
            return result.fetchall()

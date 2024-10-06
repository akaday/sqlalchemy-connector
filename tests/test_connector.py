import unittest
from sql_connector.connector import SQLConnector

class TestSQLConnector(unittest.TestCase):
    def test_mysql_connection(self):
        connector = SQLConnector('mysql', 'username', 'password', 'localhost', '3306', 'test_db')
        connection = connector.connect()
        self.assertIsNotNone(connection)

    def test_postgresql_connection(self):
        connector = SQLConnector('postgresql', 'username', 'password', 'localhost', '5432', 'test_db')
        connection = connector.connect()
        self.assertIsNotNone(connection)

    def test_sqlite_connection(self):
        connector = SQLConnector('sqlite', '', '', '', '', 'test_db.sqlite')
        connection = connector.connect()
        self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main()

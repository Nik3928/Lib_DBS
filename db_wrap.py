import psycopg as pg


class Connection:
    def __init__(self, host: str, user: str, password: str, db_name: str, port: int):
        """Initialize database connection"""
        self.conn = pg.connect(f"host={host} port={port} dbname={db_name} user={user} password={password}")
        self.cursor = self.conn.cursor()

    def __new__(cls, host: str, user: str, password: str, db_name: str, port: int):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance

    def query_c(self, string: str) -> list:
        """ Query with commit """
        self.cursor.execute(string)
        res = self.cursor.fetchall()
        self.conn.commit()
        return res

    def query(self, string: str) -> list:
        """ Query without commit """
        self.cursor.execute(string)
        res = self.cursor.fetchall()
        return res

    def commit(self):
        """ Commit changes to DB """
        self.conn.commit()

    def close(self):
        """ Close connection """
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def __del__(self):
        self.close()

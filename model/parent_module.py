import pymysql
import os

class SQL():

    conn = None
    invalid_conn = False

    def __init__(self):
        print("Creation")
        self.conn = None
        self.invalid_conn = False
        try:
            self.rds_host = os.environ['RDS']
            self.name = os.environ['NAME']
            self.password = os.environ['PASSWORD']
            self.db_name = os.environ['DB']
            self.port = os.environ['PORT_NUMBER']
        except:
            print("Environment variables not set")

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                #print("Connecting to db")
                self.conn = pymysql.connect(
                    host=self.rds_host,
                    user=self.name,
                    passwd=self.password,
                    port=int(self.port),
                    db=self.db_name,
                    connect_timeout=5
                )
        except pymysql.MySQLError as e:
            self.invalid_conn = True

    def check_connection(self):
        try:
            self.open_connection()
            if self.conn is None:
                return True
        except:
            return False
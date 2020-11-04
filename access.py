import json
import logging
import uuid
import pymysql.cursors
import status
import os
import hashlib


class Access_Db():


    def __init__(self):
        print("Creation")
        status_type   = "latest"
        self.conn = None
        try:
            self.rds_host = os.environ['RDS']
            print(self.rds_host)
            self.name = os.environ['NAME']
            self.password = os.environ['PASSWORD']
            self.db_name = os.environ['DB']
            self.port = os.environ['PORT_NUMBER']
        except:
            print("Environment variables not set")


    def generateID(self):
        print("Generating id")
        random_data = os.urandom(128)
        id = hashlib.md5(random_data).hexdigest()[:16]
        return id

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                print("Connecting to db")
                self.conn = pymysql.connect(
                    host=self.rds_host,
                    user=self.name,
                    passwd=self.password,
                    port=int(self.port),
                    db=self.db_name,
                    connect_timeout=5
                )
        except pymysql.MySQLError as e:
            print("Error: ", e)

    def createRestaurant(self, restaurant):
        print("Creating record in db")
        if restaurant == None:
            return status.failure_db()
        
        try:
            print("Accessing db")
            self.open_connection()
            if self.conn is None:
                print("Db is none")
                return status.failure_db()
            cursor = self.conn.cursor()
            # Create a new record
            sql = "INSERT INTO `restaurant` (`id`, `name`, `postcode`, `cuisine`) VALUES (%s, %s, %s, %s)"
            insert_tuple = (self.generateID(), restaurant['name'], restaurant['postcode'], restaurant['cuisine'])
            cursor.execute(sql, insert_tuple)

            sql = "SELECT * FROM restaurant"
            cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

        except pymysql.MySQLError as e:
            print("Error: ",e)
        else:
            self.conn.close()
            return status.success()


    def getURestaurant(self, status_request):
        print("Creating query for getting restaurant record")

    
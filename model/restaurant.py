from status.message import failure_db
import pymysql
from model.parent_module import SQL

class RestaurantModel(SQL):

    def __init__(self):
        self.error = ""
        
    def create_restaurant(self, restaurant):
        try:
            cursor = self.conn.cursor()
            # Create a new record
            if not self.check_connection():
                return failure_db()

            sql = "INSERT INTO `Restaurants` (`RestaurantID`, `RestaurantName`, `Cuisine`, `Postcode`) VALUES (%s, %s, %s, %s)"
            insert_tuple = (restaurant.restaurantId, restaurant.name, restaurant.cuisine, restaurant.postcode)
            cursor.execute(sql, insert_tuple)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()

        except pymysql.MySQLError as e:
            self.error = e
        else:
            self.conn.close()

    def get_restaurant(self, restaurant):
        try:
            # Create a new record
            if not self.check_connection():
                return failure_db(), True
            cursor = self.conn.cursor()

            cursor.execute("SELECT * FROM Restaurants WHERE RestaurantId=%s", restaurant.name)
            row = cursor.fetchone()
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.conn.commit()

            cursor.close()
            self.conn.close()
            message = success()
            message['body'] = row
            return message, False

        except pymysql.MySQLError as e:
            self.error = e
            return failure_db(), True
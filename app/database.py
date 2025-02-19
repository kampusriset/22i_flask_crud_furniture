import pymysql

class Database:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',  # Ganti dengan username MySQL Anda
                password='',  # Ganti dengan password MySQL Anda
                database='instyle_furniture',
                cursorclass=pymysql.cursors.DictCursor  # Agar hasil query berbentuk dictionary
            )
            self.cursor = self.connection.cursor()
            print("Database connection successful!")
        except pymysql.Error as err:
            print(f"Error: {err}")

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")
from werkzeug.security import generate_password_hash
from database import Database
import mysql.connector

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def create_user(username, password):
        db = Database()
        try:
            password_hash = generate_password_hash(password)
            db.cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                             (username, password_hash))
            db.connection.commit()
            print(f"User {username} created successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            db.close()
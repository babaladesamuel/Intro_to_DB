import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (use your own credentials)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'  # Replace with your actual MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()




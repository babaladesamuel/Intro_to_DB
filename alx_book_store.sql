import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'  # Replace with your actual password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
    print("Error: Failed to connect or create the database.")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

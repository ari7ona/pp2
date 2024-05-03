import psycopg2
import csv

# Function to connect to the PostgreSQL database
def connect():
    try:
        conn = psycopg2.connect(
            dbname="pp2",
            user="pp2",
            password="Hjk12345",
            host="localhost",
            port="54321"
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e)
        return None

# Function to insert data from CSV file
def insert_from_csv(conn, file_path):
    try:
        cur = conn.cursor()
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                cur.execute(
                    "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    row
                )
            conn.commit()
        print("Data inserted from CSV successfully")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data from CSV")
        print(e)

# Function to insert data from console
def insert_from_console(conn):
    try:
        cur = conn.cursor()
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        cur.execute(
            "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (first_name, last_name, phone_number)
        )
        conn.commit()
        print("Data inserted from console successfully")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data from console")
        print(e)

# Function to update data in the table
def update_data(conn, user_id, field, new_value):
    try:
        cur = conn.cursor()
        cur.execute(
            f"UPDATE PhoneBook SET {field} = %s WHERE id = %s",
            (new_value, user_id)
        )
        conn.commit()
        print("Data updated successfully")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error updating data")
        print(e)

# Function to query data from the table
def query_data(conn, condition=None):
    try:
        cur = conn.cursor()
        if condition:
            cur.execute(
                f"SELECT * FROM PhoneBook WHERE {condition}"
            )
        else:
            cur.execute(
                "SELECT * FROM PhoneBook"
            )
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error querying data")
        print(e)

# Function to delete data from the table
def delete_data(conn, condition):
    try:
        cur = conn.cursor()
        cur.execute(
            f"DELETE FROM PhoneBook WHERE {condition}"
        )
        conn.commit()
        print("Data deleted successfully")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error deleting data")
        print(e)

# Main function
def main():
    conn = connect()
    if conn:
        # Insert data from CSV file
        insert_from_csv(conn, 'upload.csv')

        # Insert data from console
        insert_from_console(conn)

        # Update data
        update_data(conn, user_id=1, field='first_name', new_value='Jane')

        # Query data
        query_data(conn, condition="first_name = 'John'")

        # Delete data
        delete_data(conn, condition="first_name = 'John'")

        conn.close()

if __name__ == "__main__":
    main()

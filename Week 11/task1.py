import psycopg2

# Establish connection to the database
conn = psycopg2.connect(
    dbname="pp2",
    user="pp2",
    password="Hjk12345",
    host="localhost",
    port="54321"
    )

# Function to search phonebook based on a pattern
def search_phonebook(pattern):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PhoneBook WHERE first_name LIKE %s OR last_name LIKE %s OR phone_number LIKE %s", ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
    rows = cursor.fetchall()
    return rows

# Procedure to insert or update a single user
def insert_or_update_user(name, surname, phone_number):
    cursor = conn.cursor()
    cursor.execute("""
        DO $$
        BEGIN
            IF EXISTS (SELECT * FROM PhoneBook WHERE first_name = %s AND last_name = %s) THEN
                UPDATE PhoneBook SET phone_number = %s WHERE first_name = %s AND last_name = %s;
            ELSE
                INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s);
            END IF;
        END $$;
        """, (name, surname, phone_number, name, surname, name, surname, phone_number))
    conn.commit()

# Procedure to insert many new users and check correctness of phone numbers
def insert_many_users(user_data):
    cursor = conn.cursor()
    incorrect_data = []

    for data in user_data:
        name, phone_number = data
        if not phone_number.isdigit() or len(phone_number) != 10:
            incorrect_data.append((name, phone_number))
        else:
            cursor.execute("INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, '', %s)", (name, phone_number))
    
    conn.commit()
    return incorrect_data

# Example usage
pattern = "John"
result = search_phonebook(pattern)
print("Search Results:")
for row in result:
    print(row)

insert_or_update_user("Alice", "Smith", "1234567890")

user_data = [("Bob", "1234567890"), ("Charlie", "1234567890"), ("David", "1234567890")]
incorrect_data = insert_many_users(user_data)
print("\nIncorrect Data:")
for data in incorrect_data:
    print(data)

# Close connection
conn.close()

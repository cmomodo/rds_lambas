import pymysql

# Database connection parameters
host = <host>
username = <username>
password = <password>
database_name = <database_name>

def handler():
    connection = None
    try:
        # Establish connection to the database
        connection = pymysql.connect(host=host, user=username,
                                     password=password, database=database_name)

        with connection.cursor() as cursor:
            # Prepare the data to be inserted (Example data)
            restaurant_data = [
                ('KFC', '783 Oak Street', 'New York', 'NY', '80001', '555-555-9087', 'contactkfc@training.com')
            ]

            # SQL query for inserting data into the customers table
            insert_query = """
            INSERT INTO restaurants (name, address, city, state, postal_code, phone_number, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            # Execute the insert query for each row of data
            for customer in restaurant_data:
                cursor.execute(insert_query, customer)

            # Commit the changes
            connection.commit()

            print(f"{len(restaurant_data)} restaurant data inserted successfully.")

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

# Call the handler function
handler()

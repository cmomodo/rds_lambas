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
            customer_data = [
                (3, 'Mike', 'Dean', 'mikedean@gmail.com', '555-555-1235', '12 Maple St', 'New York', 'NY', '10001'),
                (4, 'John', 'Doe', 'johndoe@gmail.com', '555-555-6789', '34 Oak St', 'Boston', 'MA', '02118')
            ]

            # SQL query for inserting data into the customers table
            insert_query = """
            INSERT INTO customers (customer_id, first_name, last_name, email, phone_number, address, city, state, postal_code)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Execute the insert query for each row of data
            for customer in customer_data:
                cursor.execute(insert_query, customer)

            # Commit the changes
            connection.commit()

            print(f"{len(customer_data)} customers inserted successfully.")

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

# Call the handler function
handler()

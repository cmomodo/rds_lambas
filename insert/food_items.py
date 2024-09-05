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
            orders_data = [
                (3,3, 'pending', 13.99)
            ]

            # SQL query for inserting data into the customers table
            insert_query = """
            INSERT INTO orders (customer_id, restaurant_id, order_status, total_price)
            VALUES (%s, %s, %s, %s)
            """

            # Execute the insert query for each row of data
            for customer in orders_data:
                cursor.execute(insert_query, customer)

            # Commit the changes
            connection.commit()

            print(f"{len(orders_data)} Order data inserted successfully.")

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

# Call the handler function
handler()

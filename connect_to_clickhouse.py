# Import necessary module
import clickhouse_driver

# Define the connection string (replace with your actual details)
connection_string = 'clickhouse://sricharan22:Sricharan@2210@localhost:9000/clickhousedb'

def main():
    try:
        # Connect to ClickHouse
        connection = clickhouse_driver.connect(connection_string)
        print("Connected to ClickHouse!")

        # Create cursor object to execute queries
        cursor = connection.cursor()

        # Example query: Selecting data from a table
        query = 'SELECT * FROM your_table LIMIT 10'
        cursor.execute(query)

        # Fetch and print results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")

# Execute the main function
if __name__ == "__main__":
    main()

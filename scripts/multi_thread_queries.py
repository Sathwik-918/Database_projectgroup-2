import threading
import mysql.connector

# Database connection parameters
DB_CONFIG = {
    'host': 'YOUR_DB_HOST',
    'user': 'YOUR_DB_USER',
    'password': 'YOUR_DB_PASSWORD',
    'database': 'project_db'
}
       
def execute_query(query):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print(f"Query executed: {query}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Queries
insert_query = "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES ('Los Angeles', '2023-01-04', 22.5, 5.0, 40.0);"
select_query = "SELECT * FROM ClimateData WHERE temperature > 20.0;"
update_query = "UPDATE ClimateData SET humidity = 50.0 WHERE location = 'New York';"

# Threads for concurrent execution
threads = [
    threading.Thread(target=execute_query, args=(insert_query,)),
    threading.Thread(target=execute_query, args=(select_query,)),
    threading.Thread(target=execute_query, args=(update_query,))
]

# Start and join threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

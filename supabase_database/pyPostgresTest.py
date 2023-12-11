import psycopg2
from dotenv import load_dotenv
import os
import random
import datetime

load_dotenv()

connection = psycopg2.connect(database = os.getenv("DATABASE_DATABASE"),
                        user = os.getenv("DATABASE_USER"),
                        host = os.getenv("DATABASE_URL"),
                        password = os.getenv("DATABASE_PASSWORD"),
                        port = os.getenv("DATABASE_PORT"))

def table_exists():
    """
    Check if a table exists in the PostgreSQL database.

    :param table_name: Name of the table to check.
    :param connection: PostgreSQL database connection.
    :return: True if the table exists, False otherwise.
    """

    with connection.cursor() as cursor:
        cursor.execute("""SELECT EXISTS (
                    SELECT 1 FROM information_schema.tables
                    WHERE table_name = %s);
                    """, ('grafana_table',))
        exists = cursor.fetchone()[0]
    return exists

def create_table():
    # Execute a command: create test_table table
    cursor.execute("""CREATE TABLE grafana_table(
                test_id SERIAL PRIMARY KEY,
                test_time TIMESTAMP(0),
                test_name VARCHAR (50) UNIQUE NOT NULL,
                test_outcome BOOLEAN);
                """)
    # Make the changes to the database persistent
    connection.commit()
    print("'grafana_table' and schema created")

def fill_data_into_table():
    for i in range (256):
        # Generate time - unix epoch
        time = str(datetime.datetime.fromtimestamp(1701857824 + (i * 86400)))
        name = 'test_case' + str(i)
        outcome = str(random.getrandbits(1))
        # print ('("INSERT INTO test_table(test_time, test_name, test_outcome) VALUES("' + time + '", '" + name + "', "' + outcome + '")");')
        cursor.execute("INSERT INTO grafana_table(test_time, test_name, test_outcome) VALUES('" + time + "', '" + name + "', '" + outcome + "');")
    # Make the changes to the database persistent
    connection.commit()

def select_all_from_table():
    cursor.execute('SELECT * FROM grafana_table;')
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(row)

# Open a cursor to perform database operations
cursor = connection.cursor()
if not table_exists():
    print("not found 'grafana_table', attempt to create it")
    create_table()
else:
    print("'grafana_table' already present")
# fill_data_into_table()
select_all_from_table()

# Close cursor and communication with the database
cursor.close()
connection.close()

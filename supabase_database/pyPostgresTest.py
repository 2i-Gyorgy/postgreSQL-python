import psycopg2
from dotenv import load_dotenv
import os
import random
import datetime

load_dotenv()

conn = psycopg2.connect(database = os.getenv("DATABASE_DATABASE"),
                        user = os.getenv("DATABASE_USER"),
                        host = os.getenv("DATABASE_URL"),
                        password = os.getenv("DATABASE_PASSWORD"),
                        port = os.getenv("DATABASE_PORT"))

def create_table():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: create test_table table
    cur.execute("""CREATE TABLE grafana_table(
                test_id SERIAL PRIMARY KEY,
                test_time TIMESTAMP(0),
                test_name VARCHAR (50) UNIQUE NOT NULL,
                test_outcome BOOLEAN);
                """)
    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()

def fill_data_into_table():
    cur = conn.cursor()
    for i in range (256):
        # Generate time - unix epoch
        time = str(datetime.datetime.fromtimestamp(1701857824 + (i * 86400)))
        name = 'test_case' + str(i)
        outcome = str(random.getrandbits(1))
        # print ('("INSERT INTO test_table(test_time, test_name, test_outcome) VALUES("' + time + '", '" + name + "', "' + outcome + '")");')
        cur.execute("INSERT INTO grafana_table(test_time, test_name, test_outcome) VALUES('" + time + "', '" + name + "', '" + outcome + "')");
    conn.commit()
    cur.close()
    conn.close()

def select_all_from_table():
    cur = conn.cursor()
    cur.execute('SELECT * FROM test_table;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)


# create_table()
# fill_data_into_table()
# select_all_from_table()
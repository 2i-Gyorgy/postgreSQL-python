import psycopg2

conn = psycopg2.connect(database = "admin",
                        user = "admin",
                        host= '127.0.0.1',
                        password = "example",
                        port = 5432)

def create_table():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: create test_table table
    cur.execute("""CREATE TABLE test_table(
                test_id SERIAL PRIMARY KEY,
                test_name VARCHAR (50) UNIQUE NOT NULL,
                test_more_property VARCHAR (100) NOT NULL);
                """)
    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()

def fill_data_into_table():
    cur = conn.cursor()
    cur.execute("INSERT INTO test_table(test_name, test_more_property) VALUES('a','bc')");
    cur.execute("INSERT INTO test_table(test_name, test_more_property) VALUES('b','cd')");
    cur.execute("INSERT INTO test_table(test_name, test_more_property) VALUES('c','de')");
    cur.execute("INSERT INTO test_table(test_name, test_more_property) VALUES('d','ef')");
    cur.execute("INSERT INTO test_table(test_name, test_more_property) VALUES('e','fg')");
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
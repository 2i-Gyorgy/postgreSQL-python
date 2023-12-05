In this project I experiment working with PostgreSQL and Python.

There are two folders:

1. dockerised_database
   Use this for a local database in a docker container.

to get the database up and running:
docker-compose up

2. supabase_database
   Use this for a remote PostgreSQL database on Supabase

   Ask from me, or add your own Supabase URL and password to the .env file

all the python code is from: https://www.datacamp.com/tutorial/tutorial-postgresql-python
requirements for pyPostgresTest.py
pip install psycopg2
pip install python-dotenv

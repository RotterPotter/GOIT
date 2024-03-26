from faker import Faker
import psycopg2 as psy


fake = Faker()


def insert_data(cursor, table_name:str, datatype:str, column:str, quantity:int):
    for _ in quantity:
        if datatype == 'name':
            query = f'insert into {table_name} ({column}) values ({fake.name()})'
            cur.execute(query)
        else:
            return 

if __name__ == '__main__':
    conn = psy.connect(
        host="localhost",
        port="8978",
        database="mydb",
        user="root",
        password="nevermind"
    )
    cur = conn.cursor()
    # insert_data(cur, 'students', 'name', 'name', 30)
    cur.execute("SELECT * FROM my_data")
    conn.close()

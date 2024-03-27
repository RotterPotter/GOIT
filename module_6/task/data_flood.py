from faker import Faker
import psycopg2 as psy
from random import randint

fake = Faker()
subjects = ['math', 'chemistry', 'physics', 'informatica']
def insert_data(cursor, table_name:str, datatype:str, column:str, quantity:int):
    if datatype == 'name':
        for i in range(quantity):
            query = f"INSERT INTO {table_name} (id, {column}) VALUES ({i}, '{fake.name()}')"
            cur.execute(query)
    elif datatype == 'group':
        cursor.execute('SELECT * FROM students')
        students_records = cursor.fetchall()
        for row in students_records:
            query = f'INSERT INTO {table_name} (student_id, {column}) values ({row[0]}, {randint(1, quantity)})'
            cursor.execute(query)
    elif datatype == 'subject':
        cursor.execute('SELECT * FROM teachers')
        teachers_records = cursor.fetchall()
        for i in range(quantity):
            cursor.execute(f"INSERT INTO {table_name} (id, name, teachers_id) values ({i}, '{subjects[i]}', {teachers_records[randint(0, len(teachers_records) - 1)][0]})")
    elif datatype == 'score':
        cursor.execute('select * from students')
        students_records = cursor.fetchall()
        students_id = list()
        for row in students_records:
            students_id.append(row[0])

        cursor.execute('select * from subjects')
        subjects_records = cursor.fetchall()
        subjects_id = list()
        for row in subjects_records:
            subjects_id.append(row[0])

        for student_id in students_id:
            for subject_id in subjects_id:
                query = f'insert into {table_name} (student_id, subject_id, score) values ({student_id}, {subject_id}, {randint(0, 12)})'
                cursor.execute(query)

    else:
        return 

if __name__ == '__main__':
    conn = psy.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="nevermind"
    )
    cur = conn.cursor()
    insert_data(cur, 'students', 'name', 'name', 51)
    insert_data(cur, 'groups', 'group', 'number_of_group', 3)
    insert_data(cur, 'teachers', 'name', 'name', 4)
    insert_data(cur, 'subjects', 'subject', '', 4)
    insert_data(cur, 'scores', 'score', '', 0)
    conn.commit()
    conn.close()

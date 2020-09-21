import psycopg2

connection = psycopg2.connect(user = "postgres",
                                  password = "shororo123",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "test")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table4;')

cursor.execute('''
    CREATE TABLE table4 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')
SQL='INSERT INTO table4 (id, completed) VALUES (%(id)s,%(completed)s);'
data = {
    'id':2,
    'completed':False
}
cursor.execute(SQL, data)
cursor.execute('SELECT * FROM table2;')
result = cursor.fetchall()
print(result)

connection.commit()

connection.close()
cursor.close()
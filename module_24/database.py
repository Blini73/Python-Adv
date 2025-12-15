import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute(
    '''
        create table if not exists employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT not null,
            position text not null,
            departament text not null,
            salary REAL 
            )
    '''
)

connection.commit()

cursor.execute('''

insert into employees (name, position, departament, salary) values (?, ?, ?, ?)     
''',('John Doe', 'Software Developer', 'IT', 70000.00))

connection.commit()

cursor.execute('select * from employees')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
    uptade employees set salary = ? where id = ?
''', (80000.0, 1))

connection.commit()

cursor.execute('select * from employees')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
    uptade employees set salary = ? where id = ?
''', (1,))

connection.commit()
cursor.execute('select * from employees')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
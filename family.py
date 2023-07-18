import sqlite3

conn = sqlite3.connect('mydb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Family')
cur.execute('''
    CREATE TABLE Family(id INTEGER PRIMARY KEY,
    first_name TEXT, middle_name TEXT, last_name TEXT,
     age INTEGER, occupation TEXT, sec_school TEXT,
     university TEXT)
''')

data = [
    (1, 'Kingsley', 'Mmaduabuchi', 'Udoako', 30, 'Software Engineer', 'St. Gregorys college', 'UNN'),
    (2, 'Onyinye', 'Prisca', 'Udoako', 29, 'Teacher', 'Kalac loyola secondary school', 'Unizik'),
    (3, 'Chukwuma', 'David', 'Udoako', 27, 'Business Man', 'Patjoe high school', 'Unizik'),
    (4, 'Chiamaka', 'Theresa', 'Udoako', 25, 'Student', 'Patjoe high school', 'Oko ploytechnic'),
    (5, 'Chinonso', 'Juliana', 'Udoako', 24, 'Marketer', 'Patjoe high school', 'Oko ploytechnic'),
    (6, 'Chibuzor', 'Christian', 'Udoako', 20, 'Student', 'Kalac loyola secondary school', 'Kaduna Seminary School')
]

cur.executemany('INSERT INTO Family(id, first_name, middle_name, last_name, age, occupation, sec_school, university) VALUES(?,?,?,?,?,?,?,?)', data)

conn.commit()
conn.close()
# import sqlite3
# conn = sqlite3.connect('db1')
# print(conn)
# if conn:
# 	print('Connected')
# else:
	# print('Not connect')
# conn.execute('''
# 		Create table student(
# 			st_id int primary key not null,
# 			st_name varchar(50),
# 			st_class varchar(10),
# 			st_email varchar(30)
# 		)
# 	''')
# conn.close()

# ins='''
# 			insert into student(st_id,st_name,st_class,st_email) values (2,'monty','11th','ramak@gmail.com')
# 	'''
# conn.execute(ins)
# conn.commit()

# data='select * from student'
# x=conn.execute(data)
# for i in x:
# 	print(i)

# import sqlite3
# conn=sqlite3.connect('student.db')
# if True:
# 	print('connect to db')
# else:
# 	print('not connected')

# cur=conn.cursor()
# cur.execute('''
# 		CREATE TABLE student(
# 			rollno INTEGER PRIMARY KEY NOT NULL,
# 			name TEXT,
# 			attendance REAL,
# 			phy INTEGER,
# 			chem INTEGER,
# 			math INTEGER,
# 			bio INTEGER,
# 			gk INTEGER
# 			)
# 		''')

# student_data=[
# 	(1,'bunty',94.89,99,56,78,12,34),
# 	(2,'munty',93.85,49,76,73,62,14)
# ]

# cur.executemany('INSERT INTO student VALUES(?,?,?,?,?,?,?,?)',student_data)
# conn.commit()
# cur.execute('SELECT * FROM student where phy=99')
# rows=cur.fetchall()

# print(rows)


import mysql.connector


server='localhost'
port=3306
database='studentmanagement'
username='root'
password='@Obama123'

conn=mysql.connector.connect(
    host=server,
    port=port,
    database=database,
    user=username,
    password=password
)

#Update Sinh viên có Code=’sv09′ thành tên mới “Hoàng Lão Tà”
cursor = conn.cursor()
sql="update student set name='Hoàng Lão Tà' where Code='sv09'"
cursor.execute(sql)

conn.commit()
print(cursor.rowcount," record(s) affected")

#Update tên Sinh viên có Code=’sv09′ thành tên mới “Hoàng Lão Tà” bằng "SQL Injection"
cursor = conn.cursor()
sql="update student set name=%s where Code=%s"
val=('Hoàng Lão Tà','sv09')

cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount," record(s) affected")
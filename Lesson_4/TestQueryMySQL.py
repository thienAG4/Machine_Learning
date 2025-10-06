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

# Sử dụng conn cho CRUD
cursor=conn.cursor()
sql="select * from student"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format("ID","Code","Name","Age"))

for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    print(align.format(id,code,name,age))

cursor.close()

print("\t","*"*10)
#Truy vấn sinh viên có age (22;26)
cursor=conn.cursor()
sql="Select * from student where Age>=20 and age<=32"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]

    print(align.format(id,code,name,age))

cursor.close()

print("\t","*"*10)
#Truy vấn toàn bộ sinh viên v sắp xếp tăng dần
cursor = conn.cursor()
sql="SELECT * FROM student " \
    "order by Age desc"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\t","*"*10)
#Truy vấn các Sinh viên có độ tuổi từ 22 tới 26 và sắp xếp theo tuổi giảm dần
cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where Age>=22 and Age<=26 " \
    "order by Age desc "
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\t","*"*10)
#Truy vấn chi tiết thông tin Sinh viên khi biết Id
cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where ID=1 "

cursor.execute(sql)

dataset=cursor.fetchone()
if dataset!=None:
    id,code,name,age,avatar,intro=dataset
    print("Id=",id)
    print("code=",code)
    print("name=",name)
    print("age=",age)

cursor.close()

print("\t","*"*10)
#Truy vấn dạng phân trang Student (Paging)
cursor = conn.cursor()
sql="SELECT * FROM student LIMIT 3 OFFSET 0"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()


print("\t","*"*10)
#Truy vấn dạng phân trang Student (Paging) Phần 2
cursor = conn.cursor()
sql="SELECT * FROM student LIMIT 3 OFFSET 3"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()


print("\t","*"*10)
#Truy vấn dạng phân trang Student (Paging) Phần 3 - Truy vấn N dòng, mỗi lần 3 dòng cho đến hết N dòng
cursor=conn.cursor()
sql="Select count(*) from student"
cursor.execute(sql)
dataset=cursor.fetchone()
rowcount=dataset[0]

limit =3
step=3
for offset in range(0,rowcount,step):
    sql = f"SELECT * FROM student LIMIT {limit} OFFSET {offset}"
    cursor.execute(sql)

    dataset = cursor.fetchall()
    align = '{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code', 'Name', 'Age'))
    for item in dataset:
        id = item[0]
        code = item[1]
        name = item[2]
        age = item[3]
        avatar = item[4]
        intro = item[5]
        print(align.format(id, code, name, age))

cursor.close()






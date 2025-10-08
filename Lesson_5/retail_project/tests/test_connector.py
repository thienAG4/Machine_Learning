import mysql.connector
import traceback
try:
    server='localhost'
    port=3306
    database='k23416_retail'
    username='root'
    password='@Obama123'

    conn=mysql.connector.connect(
        host=server,
        port=port,
        database=database,
        user=username,
        password=password
    )
except: 
    traceback.print_exc()
print("---Đã kết nối thành công---")


print("---Thao tác CRUD---")


#Câu 1: Đăng nhập cho Customer
def login_customer(email,pwd):
    cursor=conn.cursor()
    sql="select * from customer "\
        "where Email='"+email +"' and Password='"+pwd+"'"   #Cách 1: Truyền đối số
    
    print(sql)

    cursor.execute(sql)

    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login Failed!")
    cursor.close()
login_customer(email="daodao@gmail.com", pwd="123")



def login_customer1(email,pwd):
    cursor=conn.cursor()
    sql="select * from employee "\
        r"where Email= %s and Password=%s"
    val=(email,pwd)
    cursor.execute(sql,val)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login Failed!")
    cursor.close()

login_customer1(email="kimunun@yahoo.com", pwd="123")
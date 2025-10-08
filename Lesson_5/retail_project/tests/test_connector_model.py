import mysql.connector
import traceback
from Lesson_5.retail_project.models.customer import Customer

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



#Câu 1: Đăng nhập cho Customer
def login_customer(email,pwd):
    cursor=conn.cursor()
    sql="select * from customer "\
        "where Email='"+email +"' and Password='"+pwd+"'"   #Cách 1: Truyền đối số
    
    cust=None

    cursor.execute(sql)

    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
        cust=Customer()
        # cust.ID, cust.Name, cust.Phone,cust.Email,cust.Password, cust.IsDeleted=dataset
    else:
        print("Login Failed!")
    cursor.close()
    return cust
cust=login_customer(email="daodao@gmail.com", pwd="123")
if cust==None:
    print("Login Failed!")
else:
    print("Login successful!")
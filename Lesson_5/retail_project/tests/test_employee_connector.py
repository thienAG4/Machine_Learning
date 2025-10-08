from Lesson_5.retail_project.connectors.employee_connector import EmployeeConnector


ec=EmployeeConnector()
ec.connect()
em=ec.login("putin@hotmail.com","123")
if em==None:
    print("Login Fail!")
else:
    print("Login sucessful!")
    print(em)
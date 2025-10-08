class Employee:
    def __init__(self, ID=None,EmployeeCode=None,Name=None, Phone=None, Email=None, Password=None,IsDelete=None):
        self.ID=ID
        self.EmployeeCode=EmployeeCode
        self.Name=Name
        self.Phone=Phone
        self.Email=Email
        self.Password=Password
        self.IsDelete=IsDelete
    def __str__(self):
        print("ID=",self.ID)
        print("EmployeeCode=",self.ID)
        print("Name=",self.ID)
        print("Phone=",self.ID)
        print("Email=",self.ID)
        print("Password=",self.ID)
        print("IsDelete=",self.ID)
        
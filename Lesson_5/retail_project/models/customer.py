class Customer:
    def __init__(self, ID=None,EmployeeCode=None,Name=None, Phone=None, Email=None, Password=None,IsDelete=None):
        self.ID=ID
        self.EmployeeCode=EmployeeCode
        self.Name=Name
        self.Phone=Phone
        self.Email=Email
        self.Password=Password
        self.IsDelete=IsDelete
    def __str__(self):
        print(self.ID,self.Name,self.Password,self.Email)
        info="{}\t{}\t{}\t"
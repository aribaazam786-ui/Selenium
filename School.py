class school:
    def Fees(self):
        print("Fees submission")

    def Accounts(self):
        print("Fees display")

class teacher(school):
    def English(self):
        print("English Class Teacher")

    def French(self):
        print("French Class Teacher")

class student(teacher):
    def st1(self):
        print("Student Class Student")

obj = student()
obj.Fees()
obj.Accounts()
obj.English()
obj.French()
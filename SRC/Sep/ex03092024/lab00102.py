# Web autometion -- selenium
# page -- you are going automate



class VWOLoginpage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg
    def login_confirm(self):
        if self.email == "ujwal@gmail.com" and self.password == "pass123":
            print("login Sucssesful")
        else:
            print("ceck usser name or password")

email = input("Enter the email \n")
password = input("Enter the password \n")

vwo_obj = VWOLoginpage(email,password)
vwo_obj.login_confirm()
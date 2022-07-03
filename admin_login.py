class LoginAdmin:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        
    def check_username_password(self):
        if self.username == 'AP4002Group4@gmail.com' and self.password == 'alikousha_ap4002_group4':
            return 'You have successfully logged in'
        else:
            return 'Wrong username or Password, Please Try again'
        
# a = LoginAdmin('AP4002Group4@gmail.com', 'alikousha_ap4002_group4')
# b = LoginAdmin('AP4002Group4@', 'alikousha_ap4002_group4')

# print(a.check_username_password())
# print(b.check_username_password())
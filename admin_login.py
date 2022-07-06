class LoginAdmin:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        
    def check_username_password(self):
        if self.username == 'mahdihosseinizade2000@gmail.com' and self.password == 'mahdi2000':
            return 'You have successfully logged in'
        else:
            return 'Wrong username or Password, Please Try again'

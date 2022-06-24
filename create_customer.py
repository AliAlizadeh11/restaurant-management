import re

class CreateCustomer:
    def __init__(self, name, family_name, phone_number, email, national_code, password, repeat_password):
        self.name = name
        self.family_name = family_name
        self.phone_number = phone_number
        self.email = email
        self.national_code = national_code
        self.password = password
        self.repeat_password = repeat_password

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        validate_name = '^[a-zA-Z]+$'
        
        if not re.match(validate_name, value):
            raise ValueError("Name must be without any numbers or punctuation.")
        
        self._name = value
        
        
    @property
    def family_name(self):
        return self._familyname

    @family_name.setter
    def family_name(self, value):
        validate_family_name = '^[a-zA-Z]+$'
        
        if not re.match(validate_family_name, value):
            raise ValueError("LastName must be without any numbers or punctuation.")
        
        self._family_name = value
        

    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        valid_phone_number1 = re.compile(r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')
        valid_phone_number2 = re.compile(r'9(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')
        valid_phone_number3 = re.compile(r'(\+98)?9\d{9}')
        valid_phone_number4 = re.compile(r'00989(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')
        
        if not re.fullmatch(valid_phone_number1,value) and not re.fullmatch(valid_phone_number2,value) and not re.fullmatch(valid_phone_number3,value) and not re.fullmatch(valid_phone_number4,value):
            raise ValueError("It's not a valid phone number")
        
        self._phone_number = value
            
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        validate_email = '^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
        
        if not re.match(validate_email, value):
            raise ValueError("It's not an email address.")
        
        self._email = value
    
    @property
    def national_code(self):
        return self._national_code
    
    @national_code.setter
    def national_code(self, value):
        validate_national_code = '^[0-9]{10}$'
        
        if not re.match(validate_national_code, value):
            raise ValueError("It's not a valid national code.")
        
        self._national_code = value
        
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        validate_password = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
        
        if not re.match(validate_password, value):
            raise ValueError("It's not a validate password")
        
        self._password = value
    
    @property
    def repeat_password(self):
        return self._repeat_password
    
    @repeat_password.setter
    def repeat_password(self, value):
        validate_repeat_password = self.password
        
        if not validate_repeat_password == value:
            raise ValueError("It's not a validate repeat password")
        
        self._repeat_password = value

import calendar
from datetime import date, datetime

class BookingFood:
    def __init__(self):
        pass
    
    
    def choose_date_and_check_valid_date(self):
        
        today_date = date.today().strftime('%Y-%m-%d').replace(',', '-')
        
        user_choose_day = input()
        user_choose_month = input()
        user_choose_year = input()
        user_date = user_choose_year + '-' + user_choose_month + '-' + user_choose_day
        
        
        user_date1 = datetime.strptime(user_date, '%Y-%m-%d')
        today_date1 = datetime.strptime(today_date, '%Y-%m-%d')
        result = (user_date1 - today_date1).days 
        
        if result < 0:
            print('This day is not available in the calendar')
            return False
        else:
            return True
        
        

    def choose_food(self):
        food_menu = list()
        customer_list = list()

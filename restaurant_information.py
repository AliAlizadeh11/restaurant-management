from PIL import Image


class RestaurantInformation:
    def __init__(self, name, family_name, restaurant_area, restaurant_type, restaurant_address):
        self.name = name
        self.family_name = family_name
        self.restaurant_area = restaurant_area
        self.restaurant_type = restaurant_type
        self.restaurant_address = restaurant_address
        
    
    def name(self):
        return self.name
    
    def family_name(self):
        return self.family_name
    
    def restaurant_area(self):
        return self.restaurant_area
    
    def restaurant_type(self):
        return self.restaurant_type
    
    def restaurant_menu(self):
        img = Image.open("menu.jpg")
        return img.show()
    
    def restaurant_address(self):
        return self.restaurant_address

a = RestaurantInformation('alikoosha', 'alizadehlahooti', '1', 'fastfood & traditional', 'tehran')

print(a.name)
print(a.family_name)
print(a.restaurant_area)
print(a.restaurant_type)
print(a.restaurant_menu)
print(a.restaurant_address)
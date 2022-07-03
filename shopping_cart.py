class ShoppingCart():
    def __init__(self):
        self.total = 0
        self.items = dict()
        self.product_price = {'spicy Lobster': 19,
                'Baked Escargot': 16,
                'Shrimp Cocktail': 16,
                'Seared Ahi Tuna':17,
                'Filet Mignon 8 ounce': 36,
                'Rib Eye Steak, 18 ounce': 39,
                'Porterhouse for two': 40,
                'Filet Mignon 12 ounce': 40,
                'French Onion Soup': 5,
                'Lobster Bisque': 8,
                'Caprese Salad': 8.5,
                'Spinach Salad': 9.5,
                'Coca': 2,
                'Tea': 2.5,
                'Coffee':3.5,
                'Orange Juice':4
                }
        
        
    def add_item(self,item_name,quantity,price):
        self.total += price*quantity
        self.items.update({item_name:quantity})
        
        return self.total,self.items
    
    
    def remove_item(self,item_name,quantity,price):
        if item_name in self.items:
            if quantity < self.items[item_name] and quantity > 0:
                self.items[item_name] -= quantity
                self.total -= price*quantity
                
            elif quantity >= self.items[item_name]:
                self.total -= price*self.items[item_name]
                del self.items[item_name]
                
            return self.items,self.total
        
        
    def checkout(self,cash_paid):
            if cash_paid >= self.total:
                return cash_paid - self.total
            else:
                return "Cash paid not enough"
            
class Shop(ShoppingCart):

    def __init__(self):
        self.quantity = 100
        
    def remove_item(self):
        if self.quantity > 0:
            self.quantity = self.quantity - 1
        return self.quantity
        
        
# Object = ShoppingCart()
# Object.add_item("Carrots",2,2.00)
# Object.add_item("Parrots",3,2.00)
# print(Object.add_item("Marrots",4,2.00))
# print(Object.remove_item("Carrots",2,2.00))
# print(Object.checkout(200))
# Object = Shop()
# print(Object.remove_item())
class Car:
    def __init__(self,model, brand , color ,price , counter):
        self.model = model
        self.brand = brand
        self.color = color
        self._price = price
        self.counter = counter

    def info(self):
        return f'model: {self.model}, color: {self.color}, price: {self._price}'

    def tchinge_price(self,price):
        self.price = self.price - self.price * price

    def reset_counter(self):
        self.counter = 0
    def set_price(self,price):
        self._price = price

    def get_price(self):
        return self._price +'$'

class Mobile(Car):
    def __init__(self,model,color ,price):
        self.model = model
        self.color = color
        self._price = price


car_1 = Car(model= 'toy' , brand= 'KH', color= 'red',price= 1000 , counter= 800)
print(car_1.info())
car_1.reset_counter()
car_1.set_price(100)
print(car_1.info())

print('--------------------------')

mobile_1 = Mobile(model= 'iphon14' , color= 'orange',price= 1000)
print(mobile_1.info())

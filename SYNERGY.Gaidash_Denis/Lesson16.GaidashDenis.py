class Kassa:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def top_up(self, X):
        self.amount += X
        print(f"Касса пополнена на {X} рублей. Текущий баланс: {self.amount} рублей.")

    def count_1000(self):
        thousands = self.amount // 1000
        return thousands

    def take_away(self, X):
        if X > self.amount:
            raise ValueError("Недостаточно денег в кассе.")
        self.amount -= X
        print(f"Снято {X} рублей. Текущий баланс: {self.amount} рублей.")

kassa = Kassa(2500)  

kassa.top_up(1500)    
print(f"Целых тысяч в кассе: {kassa.count_1000()}")  

kassa.take_away(1000)  
print(f"Целых тысяч в кассе: {kassa.count_1000()}") 

try:
    kassa.take_away(4000)  
except ValueError as err:
    print(err)

# Задание 1:
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



# Задание 2:
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s
        print(f"Черепашка переместилась вверх на {self.s} клеток. Текущая позиция: ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.s
        print(f"Черепашка переместилась вниз на {self.s} клеток. Текущая позиция: ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.s
        print(f"Черепашка переместилась влево на {self.s} клеток. Текущая позиция: ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.s
        print(f"Черепашка переместилась вправо на {self.s} клеток. Текущая позиция: ({self.x}, {self.y})")

    def evolve(self):
        self.s += 1
        print(f"Черепашка эволюционировала. Текущая скорость: {self.s} клеток за ход.")

    def degrade(self):
        if self.s > 1:
            self.s -= 1
            print(f"Черепашка деградировала. Текущая скорость: {self.s} клеток за ход.")
        else:
            raise ValueError("Скорость не может быть меньше или равна 0.")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves_x = dx // self.s + (1 if dx % self.s != 0 else 0)
        moves_y = dy // self.s + (1 if dy % self.s != 0 else 0)
        return moves_x + moves_y



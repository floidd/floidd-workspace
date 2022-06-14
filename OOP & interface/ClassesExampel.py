class Human:
    default_name = 'Ivan'
    default_age = 33

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 0
        self._house = None

    def info(self):
        print(f'Name: {self.name}\nAge: {self.age}\nMoney: {self._money}\nHouse: {self._house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}\nDefault age: {Human.default_age}')

    def make_deal(self, house, price):
        self._money -= price
        self._house = house

    def earn_money(self, wages):
        self._money += wages

    def buy_house(self, house, sale):
        price = house.final_price(sale)
        if self._money >= price:
            self.make_deal(house, price)
        else:
            print('На счете недостаточно средств')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        if sale == 0:
            return self._price
        else:
            return self._price * (sale/100)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


if __name__ == '__main__':
    pass

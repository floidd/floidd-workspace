from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def acceleration(self):
        pass

    @abstractmethod
    def type(self):
        pass


class LadaKalina(Car):
    def acceleration(self):
        print('Acceleration time to 100 km / h — from 11 to 14.2 seconds.')

    def type(self):
        print('Body type - universal')


class BMWm5(Car):
    def acceleration(self):
        print('Acceleration time to 100 km / h — from 3 to 3.4 seconds.')

    def type(self):
        print('Body type - sedan')


class BugattiVeyron(Car):
    def acceleration(self):
        print('Acceleration time to 100 km / h — from 2.3 to 2.5 seconds.')

    def type(self):
        print('Body type - coupe')


Car1 = LadaKalina()
Car2 = BMWm5()
Car3 = BugattiVeyron()

Car1.type()
Car1.acceleration()

Car2.type()
Car2.acceleration()

Car3.type()
Car3.acceleration()
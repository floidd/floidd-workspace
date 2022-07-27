from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, mail):
        self.verify_fio(fio)
        self.__fio = fio.split()
        self.old = old
        self.mail = mail

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 99:
            raise TypeError("Возраст должен быть целым числом, а также находиться в диапазоне [14:99]")

    @classmethod
    def verify_mail(cls, mail):
        if type(mail) != str:
            raise TypeError("Емайл должен быть строкой")
        if mail.find("@") == -1 or mail.find('.') == -1:
            raise TypeError("Емайл должен в формате xxхххх@xxx.xx")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.old
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def mail(self):
        return self.mail
    @mail.setter
    def mail(self, mail):
        self.verify_mail(mail)
        self.__mail = mail




p = Person('Иванов Иван Ивынович', 33, 'Ivanoff@mail.ru')
print(p.__dict__)
p.old = 15
p.mail = 'ivanIvanov@yandex.ru'
print(p.__dict__)
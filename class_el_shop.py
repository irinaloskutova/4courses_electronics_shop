import csv

class Item:
    discount_coefficient = 0.85
    all = []

    def __init__(self, name="", price=0.0, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise (Exception("Длина наименования товара превышает 10 символов"))

    def calculate_total_price(self):
        """Подсчитывает стоимость всего конкретного товара и возвращает его"""
        return self.price * self.quantity

    def apply_discount(self):
        """Подсчитывает стоимость с учетом коэффициента"""
        self.price = self.price * Item.discount_coefficient
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        """Загружает данные из csv файла и преобразует их в список словарей"""
        with open('items.csv', 'r', encoding='UTF-8', newline='') as f:
            reader = csv.DictReader(f)
            for line in reader:
                cls.all.append(line)
            return cls.all

    @staticmethod
    def is_whole(digit):
        """Проверяет целое ли число. Допустимо с 0 после точки (напр.10.0)"""
        is_int = float(digit).is_integer()
        return is_int

    def __repr__(self) -> str:
        return f"Имя: {self.name}, цена: {self.price}"

    def __str__(self) -> str:
        return f"{self.name}"


class Phone(Item):
    def __init__(self, name="", price=0.0, quantity=0, number_of_sim=0):
        super().__init__(name, price, quantity)
        if number_of_sim > 0 and isinstance(number_of_sim, int):
            self.__number_of_sim = number_of_sim
        else:
            raise AttributeError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        # self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self) -> str:
        return f"({self.name}, {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise (Exception("C объектами других классов запрещено сложение."))

class Mixin():
    def __init__(self, *args, **kwargs):
        language = "EN"
        super().__init__(*args, **kwargs)
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self.__language
        elif self.__language == "RU":
            self.__language = "EN"
            return self.__language

class KeyBoard(Mixin, Item):
    def __init__(self, *args):
        super().__init__(*args)

# phone1 = Phone("Iphone", 100000, 10, 1)
# print(phone1.number_of_sim )
# phone1.number_of_sim = 5
# print(phone1.number_of_sim)
kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb)
# Dark Project KD87A

print(kb.language)
# EN

kb.change_lang()
print(kb.language)
# RU

kb.language = 'CH'
print(kb.language)
# AttributeError: property 'language' of 'KeyBoard' object has no setter



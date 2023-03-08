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

item = Item('Телефон', 10000, 5)

# item.name = 'Смартфон'
print(item)
# Смартфон

# item.name = 'СуперСмартфон'
# print(item.name)
# Exception: Длина наименования товара превышает 10 символов.

Item.instantiate_from_csv()  # создание объектов из данных файла
print(len(Item.all))  # в файле 5 записей с данными по товарам
# 5
# item1 = Item.all[0]
# print(item1["name"])  #По-другому не знаю как вывести наименование "Смартфон", подскажите как?????#
# Смартфон
# print(Item.is_whole(5))
# print(Item.is_whole(5.0))
# print(Item.is_whole(5.5))
# True
# True
# False

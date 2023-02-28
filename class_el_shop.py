import csv


class Item:
    discount_coefficient = 0.85
    all = []

    def __init__(self, name="", price=0.0, quantity=0):
        self.name_length(name)

        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    @classmethod
    def name_length(cls, name):  #не могу добиться чтоб этот метод работал
        if len(str(name)) > 10:
            raise Exception("Длина наименования товара превышает 10 символов")
        else:
            cls.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.name_length(self.name)
        self.__name = name

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


item = Item('Телефон', 10000, 5)
item.name = 'Смартфон'
print(item.name)
# Смартфон

item.name = 'СуперСмартфон'
print(item.name)
# Exception: Длина наименования товара превышает 10 символов.


Item.instantiate_from_csv()  # создание объектов из данных файла
print(len(Item.all))  # в файле 5 записей с данными по товарам
# 5
item1 = Item.all[0]
print(item1["name"])  #По-другому не знаю как вывести наименование "Смартфон", подскажите как?????#
# Смартфон
print(Item.is_whole(5))
print(Item.is_whole(5.0))
print(Item.is_whole(5.5))
# True
# True
# False


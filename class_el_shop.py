class Item:
    discount_coefficient = 0.85
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.discount_coefficient


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
# 200000 # общая стоимость смартфонов
# 100000 # общая стоимость ноутбуков

Item.discount_coefficient = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)
# 8000.0 # к цене смартфона применена скидка
# 20000 # к цене ноутбука скидка не была применена

print(Item.all)

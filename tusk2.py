class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

    def add(self, p):
        self.products.append(p)

p = Product("Телефон", 10000)
c = Cart()
c.add(p)
print(p.name, p.price)

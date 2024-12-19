from pprint import pprint

class Product:

    def __init__(self, name:str, weight:int, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def  __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self, __file_name):
        file = open(__file_name, 'r')
        pprint(file.read())
        return file.close()

    def add(self, *products, __file_name):
        self.products = products
        file = open(__file_name, 'w')
        

        pass


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
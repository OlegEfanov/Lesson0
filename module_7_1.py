from unicodedata import category


class Product:

    def __init__(self, name:str, weight:int, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def  __str__(self):
        return f'{self.name},",",{self.weight},",",{self.category}'

class Shop:
    __file_name = 'products.txt'

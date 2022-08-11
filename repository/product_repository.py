from repository.irepository import IRepository


class ProductRepository(IRepository):

    def __int__(self):
        self.products = list()

    def add(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

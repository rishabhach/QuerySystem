from service.iservice import IService
from repository.product_repository import ProductRepository
from constant.constants import Constants


class ProductService(IService):

    def __init__(self):
        self.product_repository = ProductRepository()

    def query(self, query):
        total_count = 0
        group_by_results = dict()

        for product in self.product_repository.get_products():
            satisfy_condition = True
            if query.filters:
                for field, value in query.filters.items():
                    if product.get(field) != value:
                        satisfy_condition = False
                        break
            total_count += satisfy_condition
            if satisfy_condition and query.group_by:
                count = group_by_results.get(product.get(query.group_by, ''), 0)
                count += 1
                group_by_results[product.get(query.group_by, '')] = count

        return total_count, group_by_results

    def add(self, product):
        self.product_repository.add(product)

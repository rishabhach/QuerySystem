from model.base_model import BaseModel


class Product(BaseModel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

p = Product(**{"a":1})
print (p)

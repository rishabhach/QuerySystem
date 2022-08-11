from model.base_model import BaseModel
from constant.operator import Operator
from constant.constants import Constants


class Query(BaseModel):
    filters = dict()
    operator = Operator.AND

    def __init__(self, filters, operator=Operator.AND, **kwargs):
        self.filters = filters
        self.operator = operator
        self.group_by = kwargs.get(Constants.GROUP_BY.value, '')
        super(Query, self).__init__(**kwargs)

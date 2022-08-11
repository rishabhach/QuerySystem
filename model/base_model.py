class BaseModel(dict):
    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)

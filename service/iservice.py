from abc import ABCMeta, abstractmethod


class IService:
    __metaclass__ = ABCMeta
    """
    Service Layer interface    
    """
    @abstractmethod
    def query(self, query):
        pass

    @abstractmethod
    def add(self, item):
        pass

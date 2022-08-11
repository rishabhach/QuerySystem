from abc import ABCMeta, abstractmethod


class IRepository:
    __metaclass__ = ABCMeta
    """
    Storage Layer interface    
    """
    @abstractmethod
    def add(self, model):
        pass

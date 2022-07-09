from abc import ABCMeta, abstractmethod

class IObserver(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'update') and
            callable(subclass.update) or
            NotImplemented
        )

    @abstractmethod
    def update(self, updated_data:dict) -> None:
        raise NotImplementedError

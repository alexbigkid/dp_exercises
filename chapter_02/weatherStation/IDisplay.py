from abc import ABCMeta, abstractmethod

class IDisplay(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'display') and
            callable(subclass.display) or
            NotImplemented
        )

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError

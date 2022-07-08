from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'fly') and
            callable(subclass.fly) or
            NotImplemented
        )

    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print('fly, fly away')


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print('cannot fly')


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print('I am flying with a rocket!')

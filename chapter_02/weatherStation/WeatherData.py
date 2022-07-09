from enum import Enum
from typing import List

from IPublisher import IPublisher
from IObserver import IObserver

class WeatherInfo(Enum):
    TEMPERATURE     = 'temperature'
    HUMIDITY        = 'humidity'
    PRESSURE        = 'pressure'


class WeatherData(IPublisher):
    _observers: List[IObserver]

    def __init__(self) -> None:
        self._observers = []
        super().__init__()


    def substribe(self, observer: IObserver) -> None:
        self._observers.append(observer)


    def unsubscribe(self, observer:IObserver) -> None:
        print(f'---- Unsubscribing: {observer.__class__.__name__}')
        self._observers.remove(observer)


    def notify(self, data:dict) -> None:
        for observer in self._observers:
            observer.update(data)


    def set_measurements(self, temperature:float=None, humidity:float=None, pressure:float=None) -> None:
        updated_measurements:dict = {}
        if temperature is not None:
            updated_measurements[WeatherInfo.TEMPERATURE] = temperature
        if humidity is not None:
            updated_measurements[WeatherInfo.HUMIDITY] = humidity
        if pressure is not None:
            updated_measurements[WeatherInfo.PRESSURE] = pressure
        self.notify(updated_measurements)
        print('')

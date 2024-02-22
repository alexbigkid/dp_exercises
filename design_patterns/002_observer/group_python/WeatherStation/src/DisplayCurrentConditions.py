from IObserver import IObserver
from IDisplay import IDisplay
from IPublisher import IPublisher
from WeatherData import WeatherData,WeatherInfo


class DisplayCurrentConditions(IObserver, IDisplay):
    _weather_data:WeatherData = None
    _temperature:float = None
    _humidity:float = None


    def __init__(self, weather_data:WeatherData) -> None:
        pass

    def update(self, updated_data: dict) -> None:
        pass

    def display(self) -> None:
        pass

if __name__ == '__main__':
    raise Exception(f'This module should not be executed directly. Only for imports')

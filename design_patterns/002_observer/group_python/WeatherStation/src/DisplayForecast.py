from IObserver import IObserver
from IDisplay import IDisplay
from IPublisher import IPublisher
from WeatherData import WeatherInfo



class DisplayForecast(IObserver, IDisplay):
    _weather_data:IPublisher = None
    _current_pressure:float = 29.92
    _last_pressure:float = None

    def __init__(self, weather_data: IPublisher) -> None:
        pass

    def update(self, updated_data: dict) -> None:
        pass

    def display(self) -> None:
        pass

if __name__ == '__main__':
    raise Exception(f'This module should not be executed directly. Only for imports')

from IObserver import IObserver
from IDisplay import IDisplay
from IPublisher import IPublisher
from WeatherData import WeatherInfo


class DisplayStatistic(IObserver, IDisplay):
    _weather_data:IPublisher
    _max_temp:float = 0.0
    _min_temp:float = 200.0
    _temp_sum:float = 0.0
    _num_readings:int = 0


    def __init__(self, weather_data:IPublisher) -> None:
        pass

    def update(self, updated_data: dict) -> None:
        pass

    def display(self) -> None:
        print(f'Avg/Max/Min temperature = {self._temp_sum/self._num_readings}/{self._max_temp}/{self._min_temp}')


if __name__ == '__main__':
    raise Exception(f'This module should not be executed directly. Only for imports')

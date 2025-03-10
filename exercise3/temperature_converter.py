# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    return round( celsius*9/5 + 32, 2)

    # TODO: Implement this function
    pass


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    return round( (fahrentheit- 32) × 5/9, 2)
    # TODO: Implement this function
    pass


def celsius_to_kelvin(celsius: Temperature) -> float:
    return round ( celsius+ 273.15, 2)
    # TODO: Implement this function
    pass


def kelvin_to_celsius(kelvin: Temperature) -> float:
    s= round( kelvin - 273.15, 2)
    if s> 0:
        return s
    else:
        print( "temperature is below absolute 0")
    # TODO: Implement this function
    pass

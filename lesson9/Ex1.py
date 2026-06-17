def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    return c + 273.15


def my_function(x):
    print(celsius_to_fahrenheit(x))
    print(fahrenheit_to_celsius(x))
    print(celsius_to_kelvin(x))


if __name__ == "__main__":
    my_function(25)
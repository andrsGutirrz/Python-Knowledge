"""
Decorator file for Platzi Ventas
Author: Andres Gutierrez Arcia
june 2019
"""


PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('What is your password?')

        if (password == PASSWORD):
            return func()
        else:
            print('Password incorrect!')

    return wrapper


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


@password_required
def needs_password():
    print('Password required')


@upper
def say_my_name(name):
    return f'Hello {name}'


if __name__ == "__main__":
    #needs_password()
    print(say_my_name('Andres'))
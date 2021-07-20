# def

def say_hello(name: str) -> str:
    hi = f"Hi, {name}"
    return hi


# lambda
say_hello_lambda = lambda name: f"Hi, {name}"

if __name__ == '__main__':
    print(say_hello("Andres"))
    print(say_hello_lambda("Melissa"))

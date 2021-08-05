# def
# typing
def say_hello(name: str) -> str:
    hi = f"Hi, {name}"
    def hi_():
        pass
    return hi


# lambda
say_hello_lambda = lambda name: f"Hi, {name}"

if __name__ == '__main__':
    print(say_hello("Andres"))
    print(say_hello_lambda("Melissa"))
    simple_lambda = lambda x: "Hola Starters"
    print(simple_lambda("a"))
    double_lambda = lambda x: lambda y: x+y
    print(double_lambda(1)(2))

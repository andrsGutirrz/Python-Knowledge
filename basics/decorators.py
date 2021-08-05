def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'



if __name__ == '__main__':
    cache = []
    # db = [1,2,3,4]  -> emulates db
    # search el 3
    if 3 in cache:
        # 3 in cache
        pass
    else:
        filter(lambda i: i==3, db)
        cache.append(3)


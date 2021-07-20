# list
my_list = [1, 2, 3, 4, 5]
# tuples
# set
# generator

def my_generator():
    max_n = 5
    count = 0
    while count <= max_n:
        count = count + 1
        yield count

# dictionary

# map
# filter
list(filter(lambda i: i>3, my_list))

if __name__ == '__main__':
    print(list(filter(lambda i: i>3, my_list)))
    print([i for i in my_list if i>3])
    gen = my_generator()
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
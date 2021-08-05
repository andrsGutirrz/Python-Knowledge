# list
my_list = [1, 2, 3, 4, 5,]
# tuples
my_tuple = (1,2, "", True, [])
# set
my_set = {1, 2, 3}

# generator
def my_generator():
    max_n = 5
    count = 0
    while count <= max_n:
        count = count + 1
        yield count

# dictionary
d = {
    "1": "a",
    "2": "b"
}

# map
map(lambda i: i+1, my_list)
# filter
list(filter(lambda i: i>3, my_list))

if __name__ == '__main__':
    print(list(filter(lambda i: i>3, my_list)))
    # print([i for i in my_list if i>3])
    # gen = my_generator()
    # print(gen.__next__())
    # print(gen.__next__())
    # print(gen.__next__())
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
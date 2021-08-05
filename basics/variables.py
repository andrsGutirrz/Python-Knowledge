# snake_case
# camelCase

if __name__ == '__main__': # main() en Java o Cpp
    my_str = "Andres"
    my_int = 1
    my_float = 1.1
    my_bool = True # False
    my_sum = my_int + my_float

    my_values = [my_str, my_int, my_float, my_bool, my_sum]

    print(my_str, my_int, my_float, my_bool, my_sum, sep=", ")
    print(*my_values, sep=", ")
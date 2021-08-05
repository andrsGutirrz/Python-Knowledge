""" How to handle files """
"""
MODES: 
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
"""


# Read
def read_file(filename: str):
    with open(filename, "r") as file:
        # file.methods()
        # print(file.readline(5))
        print(file.read())


# write
def write_file(filename: str): # log
    with open(filename, "a") as file:
        file.write("hello world\n")

def search_in_list(keyword, collection: list):
    pass

if __name__ == '__main__':
    filename: str = "my_file.txt"
    for i in range(10):
        write_file(filename)
    read_file(filename)

    # buscar en lista, algun parametro
    search_in_list("andres", ["Juan", "Claudia", "Flor", 1, 2, True, False])


from dataclasses import dataclass

# for i in range(5):
#     print(i)
#
# i = 1
# while i < 10:
#     print(i)
#     if i == 2:
#         break  # continue
#     i += 1
# else:
#     print("While finishes")


@dataclass
class Person:
    id: int
    name: str
    age: int

LIST_PERSON = [
    Person(id=1, name="Melissa", age=23),
    Person(id=2, name="Andres", age=25),
    Person(id=3, name="Erick", age=35),
]

if __name__ == '__main__':
    # [<variable> FOR <variable> IN <collection>]
    names = [i.name for i in LIST_PERSON]
    names_2: list = []
    for i in LIST_PERSON:
        names_2.append(i.name)
    v = names if names is not None else []
    print(names)
    print(names_2)

    d = {
        'a', 1,
        'b', 2,
        'c', 3,
        'd', 4,
        'e', 5,
        'f', 6,
    }

    list = [{'name':i.name} for i in LIST_PERSON]


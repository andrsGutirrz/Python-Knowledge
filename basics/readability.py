import json
from typing import List


def read_json(filename: str) -> dict:
    with open(filename, mode='r') as f:
        text = f.read()

    return json.loads(text)


def get_laptop_sugar_1(payload: dict) -> List:
    return list(filter(lambda l:
                       list(filter(lambda ll: ll.get("size") == 16, l.get("memory", [])))
                       and
                       list(filter(lambda ll: ll.get("make", "").upper() == "RYZEN", l.get("processor", [])))
                       ,
                       payload.get("items", [])))


def get_laptop_sugar_2(payload: dict) -> List:
    return [i for i in payload.get("items", []) if
            {"size": 16} in i.get("memory", []) and [j for j in i.get("processor", []) if
                                                     j.get("make", "").upper() == "RYZEN"]]


def get_laptop_not_sugar(payload: dict) -> List:
    response = []
    items = payload.get("items")
    if items:
        for item in items:
            memories = item.get("memory")
            processors = item.get("processor")
            for memory in memories:
                if memory.get("size") == 16:
                    for processor in processors:
                        if (processor.get("make", "").upper() == "RYZEN") and item not in response:
                            response.append(item)

    return response


if __name__ == '__main__':
    payload = read_json("laptops.json")
    sugar_1 = get_laptop_sugar_1(payload)
    sugar_2 = get_laptop_sugar_2(payload)
    not_sugar = get_laptop_not_sugar(payload)
    assert sugar_2 == sugar_1, "sugars are equals"
    assert sugar_1 == not_sugar, "sugars and not sugar are equals"

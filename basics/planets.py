import argparse
from datetime import datetime
from enum import Enum
from typing import List, Optional


class Planets(Enum): # Can be done using a dict
    MERCURY = 3.7
    VENUS = 8.87
    EARTH = 9.8
    MOON = 1.6
    MARS = 3.7
    JUPITER = 24.79
    SATURN = 10.44


def list_planets() -> List[Planets]:
    return [
        Planets.MERCURY,
        Planets.VENUS,
        Planets.EARTH,
        Planets.MOON,
        Planets.MARS,
        Planets.JUPITER,
        Planets.SATURN,
    ]


def parse_params(args=None):
    parser = argparse.ArgumentParser(description='Your weight on Others Worlds')
    parser.add_argument('--weight', '-w', type=float, required=True, help='Weight')
    parser.add_argument('--title', '-t', type=float, required=True, help='Weight')
    parser.add_argument('--planet', '-p', type=str, required=True, help='planet'
                        , choices=[p.name for p in list_planets()])
    if not args:
        return parser.parse_args()
    else:
        return parser.parse_args(args)


def raw_planet_to_enum_planet(raw_planet: str) -> Optional[Planets]:
    filtered = list(filter(lambda p: p.name.lower() == raw_planet.lower(), list_planets()))
    if filtered:
        return filtered[0]
    return None


def calculate_weight(weight: float, planet: Planets) -> float:
    return (weight / Planets.EARTH.value) * planet.value


def generate_txt_report(weight: float, planet: Planets, final_weight: float):
    current_timestamp = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    with open("report.txt", mode='a') as report:
        line = f"{current_timestamp}. Your weight: {weight} in {planet.name} with gravity {planet.value} is {final_weight}.\n"
        print(line)
        report.write(line)
    return "report.txt"


if __name__ == '__main__':
    # parsed_params = parse_params(args=['-w', '70', '-p', 'MOON'])
    parsed_params = parse_params()
    planet = parsed_params.planet
    weight = parsed_params.weight
    planet = raw_planet_to_enum_planet(raw_planet=planet)
    new_weight = calculate_weight(weight=weight, planet=planet)
    generate_txt_report(weight=weight, planet=planet, final_weight=new_weight)

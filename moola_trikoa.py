from angle_dms import AngleDMS
from planet import Planet
from planet_placement import PlanetPlacement
from zodiac import Zodiac
from typing import Union
from typing import List

class MoolatrikonaCondition:
    def __init__(self, planet:Planet, zodiac:Zodiac, lower_angle:Union[AngleDMS,int], upper_angle:Union[AngleDMS,int]):
        if type(lower_angle)==int:
            lower_angle=AngleDMS.from_decimal_degrees(lower_angle)
        if type(upper_angle)==int:
            upper_angle=AngleDMS.from_decimal_degrees(upper_angle)

        self.planet:Planet=planet
        self.zodiac=zodiac
        self.lower_angle:AngleDMS=lower_angle
        self.upper_angle:AngleDMS=upper_angle

    def is_valid(self, planet_placement:PlanetPlacement):
        # return planet_placement.position.zodiac== \
        #     self.zodiac \
        #             and \
        #         planet_placement.position.degree>=self.lower_angle \
        #             and \
        #         planet_placement.position.degree<=self.upper_angle
        if planet_placement.planet==self.planet and \
            planet_placement.position.zodiac==self.zodiac and \
            self.lower_angle <= planet_placement.position.degree and \
                self.upper_angle >= planet_placement.position.degree :
            return True

class MoolaTrikona:
    all_mool_trikon_coditions:List[MoolatrikonaCondition]=[
        MoolatrikonaCondition(Planet.Sun, Zodiac.Leo,0, 20),
        MoolatrikonaCondition(Planet.Moon, Zodiac.Taurus,4, 30),
        MoolatrikonaCondition(Planet.Venus, Zodiac.Libra,0, 15),
        MoolatrikonaCondition(Planet.Mars, Zodiac.Aries,0, 12),
        MoolatrikonaCondition(Planet.Mercury, Zodiac.Virgo,16, 20),
        MoolatrikonaCondition(Planet.Jupiter, Zodiac.Sagittarius,0, 10),
        MoolatrikonaCondition(Planet.Saturn, Zodiac.Aquarius,0, 20),
        ]

    def __init__(self):
        pass

    def is_in_moolatrikona(self,planet_placement:PlanetPlacement):
        for cond in MoolaTrikona.all_mool_trikon_coditions:
            if cond.is_valid(planet_placement):
                return True

        return False
from zodiac import Zodiac
from angle_dms import AngleDMS
from position import Position
from planet_placement import PlanetPlacement
from planet import Planet
from typing import List, Optional
from typing import Union

class MooltrikonaCondition:
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
        return planet_placement.position.zodiac== \
            self.zodiac \
                    and \
                planet_placement.position.degree>=self.lower_angle \
                    and \
                planet_placement.position.degree<=self.upper_angle 


class MoolTrikoa:
    all_mool_trikon_coditions=[
        MooltrikonaCondition(Planet.Sun, Zodiac.Leo,0, 20),
        MooltrikonaCondition(Planet.Moon, Zodiac.Taurus,4, 30),
        MooltrikonaCondition(Planet.Venus, Zodiac.Libra,0, 15),
        MooltrikonaCondition(Planet.Mars, Zodiac.Aries,0, 12),
        MooltrikonaCondition(Planet.Mercury, Zodiac.Virgo,16, 20),
        MooltrikonaCondition(Planet.Jupiter, Zodiac.Sagittarius,0, 10),
        MooltrikonaCondition(Planet.Saturn, Zodiac.Aquarius,0, 20),
        ]

    def __init__(self):
        pass

    def is_in_moolatrikona(self,planet_placement:PlanetPlacement):


        for cond in MoolTrikoa.all_mool_trikon_coditions:
            if planet_placement.planet==cond.planet and \
                planet_placement.position.zodiac==cond.zodiac and \
                cond.lower_angle <= planet_placement.position.degree and \
                    cond.upper_angle >= planet_placement.position.degree :
                return True
        return False


class Kundli:
    def __init__(self, planet_placements:List[PlanetPlacement]):
        self.planet_placements=planet_placements
        assert self.is_all_planets_present()
        print("Init done")

    def is_all_planets_present(self):
        planet_present={planet:False for planet in Planet}
        for planet_placement in self.planet_placements:
            planet_present[planet_placement.planet]=True
        return all(planet_present.values())

    def get_moolatrikona_planets(self):
        mt=MoolTrikoa()
        entire_list=[]
        for planet_placement in self.planet_placements:
            if mt.is_in_moolatrikona(planet_placement):
                entire_list.append(planet_placement)
        return entire_list

if __name__ == '__main__':
    priy_planets=[
    # PlanetPlacement(Planet.Asc, Position(Zodiac.Aries,AngleDMS(22, 33, 2))),
    PlanetPlacement(Planet.Sun, Position(Zodiac.Cancer,AngleDMS(1, 15, 31))),
    PlanetPlacement(Planet.Moon, Position(Zodiac.Taurus,AngleDMS(19, 9, 10))),
    PlanetPlacement(Planet.Mars, Position(Zodiac.Virgo,AngleDMS(27, 21, 27))),
    PlanetPlacement(Planet.Mercury, Position(Zodiac.Gemini,AngleDMS(22, 28, 26))),
    PlanetPlacement(Planet.Jupiter, Position(Zodiac.Libra,AngleDMS(7, 25, 37))),
    PlanetPlacement(Planet.Venus, Position(Zodiac.Gemini,AngleDMS(2, 55, 58))),
    PlanetPlacement(Planet.Saturn, Position(Zodiac.Virgo,AngleDMS(22, 36, 14))),
    PlanetPlacement(Planet.Rahu, Position(Zodiac.Gemini,AngleDMS(19, 5, 56))),
    PlanetPlacement(Planet.Ketu, Position(Zodiac.Sagittarius,AngleDMS(19, 5, 56))),
    # PlanetPlacement(Planet.Uranus, Position(Zodiac.Scorpion,AngleDMS(7, 12, 42))),
    # PlanetPlacement(Planet.Neptune, Position(Zodiac.Sagittarius,AngleDMS(1, 15, 5))),
    # PlanetPlacement(Planet.Pluto, Position(Zodiac.Libra,AngleDMS(0, 32, 45)))
    ]

    kun=Kundli(priy_planets)
    print(kun.get_moolatrikona_planets())

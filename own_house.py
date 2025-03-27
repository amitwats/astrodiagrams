from angle_dms import AngleDMS
from planet import Planet
from planet_placement import PlanetPlacement
from zodiac import Zodiac


from typing import List


class OwnHouseCondition:
    def __init__(self, planet:Planet,zodiac:Zodiac,degree_start:AngleDMS, degree_end:AngleDMS):
        self.planet=planet
        self.zodiac=zodiac
        self.degree_start=degree_start
        self.degree_end= degree_end

    def is_condition_met(self, planet_placement:PlanetPlacement):
        planet_match=self.planet==planet_placement.planet
        zodiac_match=self.zodiac==planet_placement.position.zodiac
        degree_match=self.degree_start<=planet_placement.position.degree<=self.degree_end
        return all([planet_match, zodiac_match,degree_match])


class OwnHouse:
    all_own_house_conditions:List[OwnHouseCondition]=[
        # ExaltedPlanetCondition(Pl)
        OwnHouseCondition(Planet.Sun, Zodiac.Leo ,AngleDMS(20,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Moon, Zodiac.Cancer,AngleDMS(0,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Venus, Zodiac.Taurus ,AngleDMS(15,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Venus, Zodiac.Libra,AngleDMS(0,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Mars, Zodiac.Aries ,AngleDMS(12,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Mars, Zodiac.Scorpio,AngleDMS(0,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Mercury, Zodiac.Virgo,AngleDMS(20,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Mercury, Zodiac.Gemini,AngleDMS(0,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Jupiter, Zodiac.Sagittarius ,AngleDMS(10,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Jupiter, Zodiac.Pisces,AngleDMS(0,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Saturn, Zodiac.Aquarius ,AngleDMS(15,0,0), AngleDMS(30,0,0)),
        OwnHouseCondition(Planet.Saturn, Zodiac.Capricon,AngleDMS(0,0,0), AngleDMS(30,0,0)),
    ]


    def is_own_house(planet_placement:PlanetPlacement):
        for cond in OwnHouse.all_own_house_conditions:
            if cond.is_condition_met(planet_placement):
                return True
        return False
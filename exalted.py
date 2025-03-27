from angle_dms import AngleDMS
from planet import Planet
from planet_placement import PlanetPlacement
from zodiac import Zodiac


from typing import List


class ExaltedDebilitatedPlanetCondition:
    def __init__(self, planet:Planet,zodiac:Zodiac,degree_start:AngleDMS, degree_end:AngleDMS, degree_peak:AngleDMS):
        self.planet:Planet=planet
        self.zodiac:Zodiac=zodiac
        self.degree_start:AngleDMS  = degree_start
        self.degree_end:AngleDMS  = degree_end
        self.degree_peak:AngleDMS  = degree_peak

    def is_condition_met(self, planet_placement:PlanetPlacement):
        planet_match=self.planet==planet_placement.planet
        zodiac_match=self.zodiac==planet_placement.position.zodiac
        degree_match=self.degree_start<=planet_placement.position.degree<=self.degree_end
        return all([planet_match, zodiac_match,degree_match])


class Exalted:
    all_exalted_conditions:List[ExaltedDebilitatedPlanetCondition]=[
        # ExaltedPlanetCondition(Pl)
        ExaltedDebilitatedPlanetCondition(Planet.Sun, Zodiac.Aries,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(10,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Moon, Zodiac.Taurus,AngleDMS(0,0,0), AngleDMS(3,0,0), AngleDMS(3,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Venus, Zodiac.Pisces,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(27,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Mars, Zodiac.Capricon,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(28,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Mercury, Zodiac.Virgo,AngleDMS(0,0,0), AngleDMS(15,0,0), AngleDMS(15,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Jupiter, Zodiac.Cancer,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(5,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Saturn, Zodiac.Libra,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(20,0,0)),
    ]


    def is_exalted(planet_placement:PlanetPlacement):
        for cond in Exalted.all_exalted_conditions:
            if cond.is_condition_met(planet_placement):
                return True
        return False



class Debilitated:
    all_debilitated_conditions:List[ExaltedDebilitatedPlanetCondition]=[
        # ExaltedPlanetCondition(Pl)
        ExaltedDebilitatedPlanetCondition(Planet.Sun, Zodiac.Libra,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(10,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Moon, Zodiac.Scorpio,AngleDMS(0,0,0), AngleDMS(3,0,0), AngleDMS(3,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Venus, Zodiac.Virgo,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(27,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Mars, Zodiac.Cancer,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(28,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Mercury, Zodiac.Pisces,AngleDMS(0,0,0), AngleDMS(15,0,0), AngleDMS(15,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Jupiter, Zodiac.Capricon,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(5,0,0)),
        ExaltedDebilitatedPlanetCondition(Planet.Saturn, Zodiac.Aries,AngleDMS(0,0,0), AngleDMS(30,0,0), AngleDMS(20,0,0)),
    ]


    def is_debilitated(planet_placement:PlanetPlacement):
        for cond in Debilitated.all_debilitated_conditions:
            if cond.is_condition_met(planet_placement):
                return True
        return False
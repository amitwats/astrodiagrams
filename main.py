from kundli import Kundli
from zodiac import Zodiac
from angle_dms import AngleDMS
from position import Position
from planet_placement import PlanetPlacement
from planet import Planet


if __name__ == '__main__':
    priyanka_planets=[
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


    amit_planets=[
    # PlanetPlacement(Planet.Asc, Position(Zodiac.Aries,AngleDMS(22, 33, 2))),
    PlanetPlacement(Planet.Sun, Position(Zodiac.Virgo,AngleDMS(16, 35, 57))),
    PlanetPlacement(Planet.Moon, Position(Zodiac.Leo,AngleDMS(29, 55, 35))),
    PlanetPlacement(Planet.Mars, Position(Zodiac.Gemini,AngleDMS(2, 16, 45))),
    PlanetPlacement(Planet.Mercury, Position(Zodiac.Virgo,AngleDMS(27, 56, 21))),
    PlanetPlacement(Planet.Jupiter, Position(Zodiac.Pisces,AngleDMS(27, 25, 16))),
    PlanetPlacement(Planet.Venus, Position(Zodiac.Leo,AngleDMS(6, 20, 52))),
    PlanetPlacement(Planet.Saturn, Position(Zodiac.Cancer,AngleDMS(7, 52, 37))),
    PlanetPlacement(Planet.Rahu, Position(Zodiac.Scorpio,AngleDMS(0, 27, 35))),
    PlanetPlacement(Planet.Ketu, Position(Zodiac.Taurus,AngleDMS(0, 27, 35))),
    # PlanetPlacement(Planet.Uranus, Position(Zodiac.Scorpion,AngleDMS(7, 12, 42))),
    # PlanetPlacement(Planet.Neptune, Position(Zodiac.Sagittarius,AngleDMS(1, 15, 5))),
    # PlanetPlacement(Planet.Pluto, Position(Zodiac.Libra,AngleDMS(0, 32, 45)))
    ]

    kun=Kundli(amit_planets)
    # kun=Kundli(priyanka_planets)
    print(kun.get_moolatrikona_planets())
    print(kun.get_exalted_planets())
    print(kun.get_debilitated_planets())
    print(kun.get_own_house_planets())
    

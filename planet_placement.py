from position import Position
from planet import Planet

class PlanetPlacement:
    def __init__(self, planet:Planet, position:Position):
        self.planet:Planet=planet
        self.position:Position=position

    def __str__(self):
        return f"Planet: {self.planet.name}, Zodiac: {self.position.zodiac.name}, Position:{self.position.degree}"
    
    def __repr__(self):
        return f"Planet: {self.planet.name}, Zodiac: {self.position.zodiac.name}, Position:{self.position.degree}"
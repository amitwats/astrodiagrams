from exalted import Exalted, Debilitated
from moola_trikoa import MoolaTrikona
from own_house import OwnHouse
from planet import Planet
from planet_placement import PlanetPlacement


from typing import List


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
        mt=MoolaTrikona()
        entire_list=[]
        for planet_placement in self.planet_placements:
            if mt.is_in_moolatrikona(planet_placement):
                entire_list.append(planet_placement)
        return entire_list


    def get_exalted_planets(self):
        # mt:Exalted=Exalted()
        entire_list=[]
        for planet_placement in self.planet_placements:
            if Exalted.is_exalted(planet_placement):
                entire_list.append(planet_placement)
        return entire_list

    def get_debilitated_planets(self):
        entire_list=[]
        for planet_placement in self.planet_placements:
            if Debilitated.is_debilitated(planet_placement):
                entire_list.append(planet_placement)
        return entire_list

    def get_own_house_planets(self):
        entire_list=[]
        for planet_placement in self.planet_placements:
            if OwnHouse.is_own_house(planet_placement):
                entire_list.append(planet_placement)
        return entire_list

    
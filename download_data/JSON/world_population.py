import json
from countries import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

# Getting data from json file
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Get population of 2010 each country and 2 letter code and storing key as code(2letter) value populatoin as value in list 
cc_group_1 , cc_group_2, cc_group_3 = {}, {}, {}

for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))

        # Get country code from pygal.maps.world.COUNTRIES if country not found return None
        code = get_country_code(country_name)
        
        # If code is found  Run this branch
        if code:
            # Keeping populaton less than 1 crore  in first dict
            if population < 10000000:
                cc_group_1[code] = population

            # Keeping populaton less than 100 crore  in second dict
            elif population < 100000000:
                 cc_group_2[code] = population
            
            # Keeping populaton more than than 100 crore  in third dict
            else:
                cc_group_3[code] = population

        # If code returns None run this else
        else:
            pass

# Object of WorldMap
wm_style = RS('#336699', base_style = LCS)
wm = World( style= wm_style)
wm.title = "Populaton of the world"

# Add countries of population
wm.add("Under 1crore", cc_group_1)
wm.add("Under 10crore", cc_group_2)
wm.add("Over 10crore", cc_group_3)

# Rendering to image
wm.render_to_file("worldmap.svg")
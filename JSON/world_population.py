import json;
from country_codes import get_country_code;
import pygal_maps_world.maps as MP;
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS;

filename = "population_data.json";
with open(filename) as f:
    pop_data = json.load(f);#Transform the data into a list;
cc_populations = {};
for pop_dict in pop_data:
    if(pop_dict["Year"] == "2010"):
        country = pop_dict["Country Name"];
        population = int(float(pop_dict["Value"]));#Some data are floats;
        code = get_country_code(country);
        if(code):
            cc_populations[code] = population;
        else:
            print("ERROR - " + country);


cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {};
for cc, pops in cc_populations.items():
    if(pops < 10000000):
        cc_pops_1[cc] = pops;
    elif(pops < 1000000000):
        cc_pops_2[cc] = pops;
    else:
        cc_pops_3[cc] = pops;

wm_style = RS("#336699", base_style = LCS);
#wm_style = LightColorizedStyle;
#wm_style = RotateStyle("#330000");#RGB
wm = MP.World(style = wm_style);

wm.title = "World Population in 2010, by Country";
wm.add("0 - 10m", cc_pops_1);
wm.add("10m - 1bn", cc_pops_2);
wm.add(">1bn", cc_pops_3);

#Darker color for larger number and vice versa;

wm.render_to_file("world_population.svg");

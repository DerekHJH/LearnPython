import pygal_maps_world.maps as MP;

wm = MP.World();
wm.title = "North, Central, and Sounth America";
wm.add("North America", ["ca", "mx", "us"]);
#Each new add will change a different color;
wm.add("Central America", ["bz", "cr", "gt", "hn", "ni", "pa", "sv"]);
wm.add("South America", ["ar", "bo", "br", "cl", "co", "ec", "gf", "gy", "pe", "py", "sr", "uy", "ve"]);
wm.render_to_file("americas.svg");

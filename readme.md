Fetch highways in Pierce County Washington that have the abbreviation "Kp" and generate
a JOSM change file to expand that abbreviation to "Key Peninsula".

The highways are fetched from Overpass API using this script:

	[out:xml];
	area(3601153347)->.searchArea;
	(
	way["highway"]["name"~"Kp"](area.searchArea);
	>;
	);
	out meta;
import math, sys
from numpy import linalg as LA
from numpy import array as ar

earthRadius = 637100000

def convert_points(lat,lon):
	lat = lat * math.pi / 180.
	lon = lon * math.pi / 180.
	x = earthRadius * math.cos(lat) * math.cos(lon)
	y = earthRadius * math.cos(lat) * math.sin(lon)

	return (x,y)

def get_distance(p1,p2):
	# lat1 = float(sys.argv[1])
	# lon1 = float(sys.argv[2])
	# lat2 = float(sys.argv[3])
	# lon2 = float(sys.argv[4])

	a = ar(convert_points(float(p1[0]),float(p1[1])))
	b = ar(convert_points(float(p2[0]),float(p2[1])))
	# print a-b

	dist = LA.norm(a-b)

	return dist
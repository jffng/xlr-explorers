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

lat1 = float(sys.argv[1])
lon1 = float(sys.argv[2])
lat2 = float(sys.argv[3])
lon2 = float(sys.argv[4])

a = ar(convert_points(lat1,lon1))
b = ar(convert_points(lat2,lon2))

print a-b

dist = LA.norm(a-b)

print dist
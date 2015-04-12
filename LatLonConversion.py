import math, sys
from numpy import linalg as LA
from numpy import array as ar
import utm

def utm_convert_points(lat,lon):
	value = utm.from_latlon(lat, lon)
	return (value[0], value[1])

def utm_convert_lat_lon(x,y):
	# 18 = zone number, T = zone letter
	value = utm.to_latlon(x,y,18,'T')
	return value

def get_distance(p1,p2):

	a = ar(utm_convert_points(float(p1[0]),float(p1[1])))
	b = ar(utm_convert_points(float(p2[0]),float(p2[1])))

	dist = LA.norm(a-b)

	return dist
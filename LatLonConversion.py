import math, sys
from numpy import linalg as LA
from numpy import array as ar
import utm

earthRadius = 637100000

def convert_points(lat,lon):
	lat = lat * math.pi / 180.
	lon = lon * math.pi / 180.
	x = earthRadius * math.cos(lat) * math.cos(lon)
	y = earthRadius * math.cos(lat) * math.sin(lon)

	# print 'x ' , x
	# print 'y ' , y

	return (x,y)

# def pyproj_convert_points(lat,lon):
# 	gmaps = Proj('+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs')
# 	wgs84 = Proj(init='epsg:4326')
# 	lon, lat = transform(gmaps, wgs84, lon, lat, radians=True)
# 	#p1 = Proj("+proj=robin +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs")
# 	#p1 = Proj(init="epsg:4326+units=m")
# 	x,y = p1(lat,lon)
# 	return (x,y)

def utm_convert_points(lat,lon):
	value = utm.from_latlon(lat, lon)
	return (value[0], value[1])

def utm_convert_lat_lon(x,y):
	# 18 = zone number, T = zone letter
	value = utm.to_latlon(x,y,18,'T')
	return value

# def pyproj_convert_lat_long(x,y):
# 	#p1 = Proj("+proj=robin +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs")
# 	p1 = Proj("epsg:4326 +units=m")
# 	lat,lon = p1(x,y,inverse=True)
# 	return (lat,lon)

def get_distance(p1,p2):
	# lat1 = float(sys.argv[1])
	# lon1 = float(sys.argv[2])
	# lat2 = float(sys.argv[3])
	# lon2 = float(sys.argv[4])

	a = ar(utm_convert_points(float(p1[0]),float(p1[1])))
	b = ar(utm_convert_points(float(p2[0]),float(p2[1])))
	# print a-b

	dist = LA.norm(a-b)
	#print 'back to lat lon' , utm_convert_lat_lon(a[0], a[1])

	return dist

	# x = earthRadius * math.cos(lat * math.pi / 180) * math.cos(lon * math.pi / 180)
	# x/earthRadius = math.cos(lat * math.pi / 180) * math.cos(lon * math.pi / 180)
	# x/earthRadius = inverse_cos(lat) * pi/180 * inverse_cos(lon) * pi/180
	# x/earthRadius = inverse_cos(lat) * 2pi/180 * inverse_cos(lon)
	# (x/earthRadius)/(2pi/180) = inverse_cos(lat) * inverse_cos(lon)


	# y = earthRadius * math.cos(lat * math.pi / 180.) * math.sin(lon * math.pi / 180.)
	# y/earthRadius = math.cos(lat * math.pi / 180.) * math.sin(lon * math.pi / 180.)
	# y/earthRadius = inverse_cos(lat) * pi/180 * inverse_sin(lon) * pi/180
	# y/earthRadius = inverse_cos(lat) * 2pi/180 * inverse_sin(lon)
	# (y/earthRadius)/(2pi/180) = inverse_cos(lat) * inverse_sin(lat)
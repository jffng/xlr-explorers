import xlr, serial
import json
import math
import operator
import argparse
import LatLonConversion
import numpy

three_d = False

# switch from sys arguments to argument parser
# command line input ex: python trigV2.py -radio1 1 2 3 -radio2 4 5 6 -radio3 6 7 8 --three_d

parser = argparse.ArgumentParser()

parser.add_argument("-radio1", nargs='+')
parser.add_argument("-radio2", nargs='+')
parser.add_argument("-radio3", nargs='+')
# to set as 2D, trig2V.py --two_d
# to set as 3D, trig2V.py --three_d
# you can also not specify 3D or 2D, and it will default to 2D
parser.add_argument("--two_d", dest = 'three_d', action = 'store_false')
parser.add_argument("--three_d", dest = 'three_d', action = 'store_true')
parser.set_defaults(three_d=False)

args = parser.parse_args()
three_d = args.three_d


# returns the cross product of two vectors in 2D or 3D
def cross(a, b, three_d):
    if three_d:
        c = [a[1]*b[2] - a[2]*b[1],
             a[2]*b[0] - a[0]*b[2],
             a[0]*b[1] - a[1]*b[0]]

        return c
    else:
        c = a[0]*b[1] - a[1]*b[0]
        return c
    

# we are radio1, we are trying to trianglualte location of radio4

ser = serial.Serial('/dev/cu.usbserial', timeout=.5)

# reset radio2, radio3, and radio4 to ensure all arguments are what we are expecting
reset = 're'
remote_at = xlr.RemoteAT(reset, "radio2")
remote_at.update()
#print remote_at.send(ser,50)

remote_at = xlr.RemoteAT(reset, "radio3")
remote_at.update()
#print remote_at.send(ser,50)

remote_at = xlr.RemoteAT(reset, "radio4")
remote_at.update()
#print remote_at.send(ser,50)

# abs coordinates for radio1, radio2, and radio3
p1 = tuple(args.radio1)
p2 = tuple(args.radio2)
p3 = tuple(args.radio3)

# set data rates to 4

data_rate = 'br4'
remote_at = xlr.RemoteAT(data_rate, "radio2")
remote_at.update()
remote_at.send(ser,50)

remote_at = xlr.RemoteAT(data_rate, "radio3")
remote_at.update()
remote_at.send(ser,50)

remote_at = xlr.RemoteAT(data_rate, "radio4")
remote_at.update()
remote_at.send(ser,50)

at_command = xlr.ATCommand(data_rate)
at_command.update()
at_command.send(ser,50)

# distance between 1 + 2
range12 = LatLonConversion.get_distance(p1,p2)

# distance betwen 1 + 3
range13 = LatLonConversion.get_distance(p1,p3)
	
# distance betwen 2 + 3
range23 = LatLonConversion.get_distance(p2,p3)

def distance(p0, p1):
    if three_d:
        return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2 + (p0[2] - p1[2])**2)
    else:
        return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

sum_range14 = 0
sum_range24 = 0
sum_range34 = 0
total_range14 = 0
total_range24 = 0
total_range34 = 0
#distances to target
for i in range(20):
    # 1 + 4
    rg = xlr.Distance("radio4")
    rg.update()
    #range14 = float(rg.send(ser, 50)[1])
    try:
        curr_range = float(rg.send(ser, 50)[1])
        sum_range14 += curr_range
        total_range14 += 1
    except ValueError:
        continue
    #2+4
    rg = xlr.RemoteDistance("radio2", "radio4")
    rg.update()
    #range24 = float(rg.send(ser, 50)[1])
    try:
        curr_range = float(rg.send(ser, 50)[1])
        sum_range24 += curr_range
        total_range24 += 1
    except ValueError:
        continue
    #3+4
    rg = xlr.RemoteDistance("radio4", "radio3")
    rg.update()
    #range34 = float(rg.send(ser, 50)[1])
    try:
        curr_range = float(rg.send(ser, 50)[1])
        sum_range34 += curr_range
        total_range34 += 1
    except ValueError:
        continue

range14 = (sum_range14 / total_range14) / 100
range24 = (sum_range24 / total_range24) / 100
range34 = (sum_range34 / total_range34) / 100


# radio 3
i = (math.pow(range13,2)+math.pow(range12,2)-math.pow(range23,2))/(2*range12)
j = math.sqrt(math.pow(range13,2)-math.pow(i,2))

# radio 4
x = (math.pow(range14,2) - math.pow(range24,2) + math.pow(range12,2))/(2*range12)
y = (math.pow(range14,2)-math.pow(range34,2)+math.pow(range13,2)-(2*i*x))/(2*j)
# z = math.sqrt(abs(math.pow(range14,2) - math.pow(x,2) - math.pow(y,2)))

# relative coordinate positions
radio1 = 0,0
radio2 = range12,0
radio3 = i,j
# radio4 = x,y,z
radio4 = x,y

# get absolute value of 4th radio

# ex is a unit vector in the direction from p1 towards p2
# ex = num_ex/den_ex

p1 = LatLonConversion.utm_convert_points(float(p1[0]),float(p1[1]))
p2 = LatLonConversion.utm_convert_points(float(p2[0]),float(p2[1]))
p3 = LatLonConversion.utm_convert_points(float(p3[0]),float(p3[1]))
num_ex =  tuple(map(operator.sub,p2,p1)) 
den_ex =  distance(p2,p1)
ex = tuple([round((i/den_ex),4) for i in num_ex])


d = tuple(map(operator.sub,p3,p1))
smx = sum(map(operator.mul, ex, d))

# ey is a unit vector in the y direction

q = tuple([i*smx for i in ex])
num_ey = tuple(map(operator.sub,d,q))

den_ey = distance(d,q)
ey = tuple([i/den_ey for i in num_ey])

# ez is the cross product of ex and ey
np = numpy
# ez = tuple(np.cross(ex,ey))

#P4 = p1 + xex + yey +- zez
# xex
j = tuple([num*x for num in ex])
# yez
k = tuple([num*y for num in ey])
# zez and -zez
# l = tuple([num*z for num in ez])
# l2 = tuple([num*-z for num in ez])
# xex + yey
m = tuple(map(operator.add,j,k)) 
# xex + yey + zez and xex + yey - zez
# n = tuple(map(operator.add,m,l)) 
# n2 = tuple(map(operator.add,m,l2)) 
# p1 + xex + yey + zez and p1 + xex + yey - zez
# p1 + xex + yey
p4 = tuple(map(operator.add,m,p1)) 
# p4 = tuple(map(operator.add,n,p1)) 
# p4_2 = tuple(map(operator.add,n2,p1)) 
#print "P4: ", p4 
# print p4_2

p4_coords = LatLonConversion.utm_convert_lat_lon(p4[0],p4[1])

p4_dict = {"point": [p4_coords[0], p4_coords[1]]}
print json.dumps(p4_dict)



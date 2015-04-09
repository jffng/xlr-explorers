import xlr, serial
import math
import operator
import argparse
import LatLonConversion
import numpy

# TO DO - should work for 2D and 3D vectors
def cross(a, b):
    # c = [a[1]*b[2] - a[2]*b[1],
    #      a[2]*b[0] - a[0]*b[2],
    #      a[0]*b[1] - a[1]*b[0]]

    # return c
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

# we are radio1, we are trying to trianglualte location of radio4

ser = serial.Serial('/dev/cu.usbserial', timeout=.5)

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

# version = 'vb'
# remote_at = xlr.RemoteAT2(version, "radio2")
# remote_at.update()
# remote_at.send(ser,50)

# remote_at = xlr.RemoteAT2(version, "radio3")
# remote_at.update()
# remote_at.send(ser,50)

# remote_at = xlr.RemoteAT2(version, "radio4")
# remote_at.update()
# remote_at.send(ser,50)

# at_command = xlr.ATCommand(version)
# at_command.update()
# at_command.send(ser,50)

# switch from sys arguments to argument parser
# command line input ex: python trigV2.py -radio1 1 2 3 -radio2 4 5 6 -radio3 6 7 8

parser = argparse.ArgumentParser()

parser.add_argument("-radio1", nargs='+')
parser.add_argument("-radio2", nargs='+')
parser.add_argument("-radio3", nargs='+')

args = parser.parse_args()

#abs coordinates
p1 = tuple(args.radio1)
# print 'p1'
# print type(p1)
# print p1
p2 = tuple(args.radio2)
# print 'p2'
# print p2
p3 = tuple(args.radio3)
# print 'p3'
# print p3

# set data rates

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

# distance betwen 1 + 2
# rg = xlr.Distance("radio2")
# rg.update()
# range12 = float(rg.send(ser, 50)[1])
# print "range12", range12
range12 = LatLonConversion.get_distance(p1,p2)
print 'range12'
print range12

	
# distance betwen 1 + 3
# rg = xlr.Distance("radio3")
# rg.update()
# range13 = float(rg.send(ser, 50)[1])
# print "range13", range13
range13 = LatLonConversion.get_distance(p1,p3)
print 'range13'
print range13
	
# distance betwen 2 + 3
# remoterg = xlr.RemoteDistance("radio2", "radio3")
# remoterg.update()
# range23 = float(remoterg.send(ser, 50)[1])
# print "range23",range23
range23 = LatLonConversion.get_distance(p2,p3)
print 'range23'
print range23

# TODO: needs to handle 2D vectors and 3D vectors
def distance(p0, p1):
    #return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2 + (p0[2] - p1[2])**2)
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

#distances to target
# for i in range(20):
	# 1 + 4
rg = xlr.Distance("radio4")
rg.update()
range14 = float(rg.send(ser, 50)[1])
print "range14", range14,rg.send(ser, 50)[0]
#2+4
rg = xlr.RemoteDistance("radio2", "radio4")
rg.update()
range24 = float(rg.send(ser, 50)[1])
print "range24", range24,rg.send(ser, 50)[0]
#3+4

rg = xlr.RemoteDistance("radio3", "radio4")
rg.update()
range34 = float(rg.send(ser, 50)[1])
print "range34", range34,rg.send(ser, 50)[0]



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
print "radio1 : ", radio1
print "radio2 : ", radio2
print "radio3 : ", radio3
# radio4 = x,y,z
radio4 = x,y

# get absolute value of 4th radio

# ex is a unit vector in the direction from p1 towards p2
# ex = num_ex/den_ex

# print map(operator.sub,p2,p1)
# print "map type" , type(map(operator.sub,p2,p1))
p1 = (float(p1[0]),float(p1[1]))
p2 = (float(p2[0]),float(p2[1]))
p3 = (float(p3[0]),float(p3[1]))
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
# xex + yez
m = tuple(map(operator.add,j,k)) 
# xex + yey + zez and xex + yey - zez
# n = tuple(map(operator.add,m,l)) 
# n2 = tuple(map(operator.add,m,l2)) 
# p1 + xex + yey + zez and p1 + xex + yey - zez
p4 = tuple(map(operator.add,m,p1)) 
# p4 = tuple(map(operator.add,n,p1)) 
# p4_2 = tuple(map(operator.add,n2,p1)) 
print "P4: ", p4 
# print p4_2




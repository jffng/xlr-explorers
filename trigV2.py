import xlr, serial
import math
import operator
import numpy
import sys

# we are radio1, we are trying to trianglualte location of radio4

ser = serial.Serial('/dev/cu.usbserial', timeout=.5)

#abs coordinates
p1 = sys.argv[1],sys.argv[2]
p2 = sys.argv[3],sys.argv[4]
p3 = sys.argv[5],sys.argv[6]

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
rg = xlr.Distance("radio2")
rg.update()
range12 = rg.send(ser, 50)[1]
	
# distance betwen 1 + 3
rg = xlr.Distance("radio3")
rg.update()
range13 = rg.send(ser, 50)[1]
	
# distance betwen 2 + 3
remoterg = xlr.RemoteDistance("radio2","radio3")
remoterg.update()
range23 = remoterg.send(ser, 50)[1]

#distances to target
# 1 + 4
rg = xlr.Distance("radio4")
rg.update()
range14 = rg.send(ser, 50)[1]

#2+4
rg = xlr.Distance("radio2", "radio4")
rg.update()
range24 = rg.send(ser, 50)[1]

#3+4

rg = xlr.Distance("radio3", "radio4")
rg.update()
range34 = rg.send(ser, 50)[1]

# radio 3
i = (math.pow(range13,2)+math.pow(range12,2)-math.pow(range23,2))/(2*range12)
j = math.sqrt(math.pow(range13,2)-math.pow(i,2))

# radio 4
x = (math.pow(range14,2) - math.pow(range24,2) + math.pow(range12,2))/(2*range12)
y = (math.pow(range14,2)-math.pow(range34,2)+math.pow(range13,2)-(2*i*x))/(2*j)

# relative coordinate positions
radio1 = 0,0
radio2 = range12,0
radio3 = i,j
radio4 = x,y

# get absolute value of 4th radio

# ex is a unit vector in the direction from p1 towards p2
# ex = c/a
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

c =  tuple(map(operator.sub,p2,p1)) 
a =  distance(p2,p1)
ex = tuple([round((i/a),4) for i in c])


d = tuple(map(operator.sub,p3,p1))
smx = sum(map(operator.mul, ex, d))

# ey is a unit vector in the y direction

q = tuple([i*smx for i in ex])
#print q
np = numpy
num_ey = tuple(map(operator.sub,d,q))

den_ey = distance(d,q)
ey = tuple([i/den_ey for i in num_ey])

#P4 = p1 + xex + yey
j = tuple([num*x for num in ex])
k = tuple([num*y for num in ey])
l = tuple(map(operator.add,j,k)) 
p4 = tuple(map(operator.add,l,p1)) 
# print p1
# print j
# print k
print p4 




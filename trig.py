import math
import operator
import numpy

#abs coordinates
# TODO - these should prob be sys arguments
p1 = 1,2
p2 = 9,1.9
p3 = 5,5

# TODO - define the distances by calling requests
range12 = 8
# sending a distance measurement command
range23 = 5
range13 = 5

# TODO - define the distances by calling requests
range14 = 2.5
range24 = 5.7
range34 = 2.2

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

# print ex
# print smx(ex)

# ey is a unit vector in the y direction
#print ex
q = tuple([i*smx for i in ex])
#print q
np = numpy
#num_ey = np.array([4,3]) - 3.89*(np.array([.999,-.0125]))
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


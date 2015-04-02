import math
import operator

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

#abs coordinates
# TODO - these should prob be sys arguments
p1 = 1,2,0.1
p2 = 9,1.9,-0.1
p3 = 5,5,0.2

# TODO - define the distances by calling requests
range12 = 8
# sending a distance measurement command
range23 = 5
range13 = 5

# radio 3
i = (math.pow(range13,2)+math.pow(range12,2)-math.pow(range23,2))/(2*range12)
j = math.sqrt(math.pow(range13,2)-math.pow(i,2))

# TODO - define the distances by calling requests
range14 = 2.5
range24 = 5.7
range34 = 2.2

# radio 4
x = (math.pow(range14,2) - math.pow(range24,2) + math.pow(range12,2))/(2*range12)
y = (math.pow(range14,2)-math.pow(range34,2)+math.pow(range13,2)-(2*i*x))/(2*j)
z = math.sqrt(abs(math.pow(range14,2) - math.pow(x,2) - math.pow(y,2)))

# relative coordinate positions
radio1 = 0,0,0
radio2 = range12,0,0
radio3 = i,j,0
radio4 = x,y,z


# get absolute value of 4th radio

# ex is a unit vector in the direction from p1 towards p2
# ex = num_ex/den_ex
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2 + (p0[2] - p1[2])**2)

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
print ey

# ez is the cross product of ex and ey
ez = cross(ex,ey)

#P4 = p1 + xex + yey +- zez

# xex
j = tuple([num*x for num in ex])
# yez
k = tuple([num*y for num in ey])
# zez and -zez
l = tuple([num*z for num in ez])
l2 = tuple([num*-z for num in ez])
# xex + yez
m = tuple(map(operator.add,j,k)) 
# xex + yey + zez and xex + yey - zez
n = tuple(map(operator.add,m,l)) 
n2 = tuple(map(operator.add,m,l2)) 
# p1 + xex + yey + zez and p1 + xex + yey - zez
p4 = tuple(map(operator.add,n,p1)) 
p4_2 = tuple(map(operator.add,n2,p1)) 

print p4 
print p4_2


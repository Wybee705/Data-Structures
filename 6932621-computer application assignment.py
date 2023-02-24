
import numpy as np
l=12  #length of beam in meters
w=10#intensity of load in  kn/m
#question 1
#Bending moment(M) and shear force(V)at the first end, 
x=0 
m="the bending moment at x=0"
M=(w*(-6*x**2 + 6*l*x-l**2))/12
V=w*(l/2-x)
n="the shear force at x=0"
print()
#Bending moment(m) and shear force(v) at the end
x=l
M=(w*(-6*x**2+6*l*x-l**2))/12
V=w*(l/2-x)
print()
#question b
"""
when the bending moment is zero, we get an expression x**2-lx+l**2/6=0
"""
a=1
b=-l
c=l**2/6
discriminant=b**2-4*a*c
x1=(-b+np.sqrt(discriminant))/2*a
x2=(-b-np.sqrt(discriminant))/2*a
print()
print("(b)the points of contra flexure are {0} and{1}".format(x1,x2))
#question c
"""
When the shear force is zero, x=l/2
"""
x=l/2
print()
print("(c)the point where v=0 is {}".format(x))


#question d
p=0
s=0.01
q=l+s
x=np.arrange(p,q,s)
M=(w*(-6*x**2+6*l*x-l**2))/12
print()
print ("(d) use the initial variables, the bending momentat each step in the array is{0}".format(M))

#question e
v=w*(l/2-x)
print()
print("(e) the shear force for each procedure along the total lenght is {}".format(v))

#questionf
"""
Let the exact value of bending moment array be AM
minimum AM be m_AM0
"""
AM=abs(M)
m_AM0=min(AM)
"""
when the bending moment is m_AM, an expression x**2-lx+(l**2/6)+(2*m_AM)/w=o
"""
a=1
b=-l
c=(l**2/6)+(2*m_AM0)/w
discriminant =b**2-4*a*c
x1=(-b +np.sqrt(discriminant))/2*a
x2=(-b-np.sqrt(discriminant))/2*a
print()
print("(f) the points along l at which the exact values of the bending moment arrayis minimum are{0} and {1}".format(x1,x2))

#question g
"""
Let the distinct errors be r_e
"""
r_e1 =((root_1b-root_1f)/root_1b*100
(r_e2=((root_2f-root_2b)/root_2f*100)
 print("(g) the distinct errors between the estimatedpoints of contra_flexure are {0}% and {1}%".format(r_e1,r_e2))


      




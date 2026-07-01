Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a='python'
b='course'
print(a+" "+b)
python course
fname="vaishu"
lname="ravula"
print(fname+" "+lname)
vaishu ravula
print(fname.title()+" "+lname.title())
Vaishu Ravula
print((fname+" "+lname).title())
Vaishu Ravula

#formatting
a=2
b=8
print(a+b)
10
print("the sum is",a+b)
the sum is 10
city='Nizamabad'
print("the city is",city)
the city is Nizamabad
>>> 
>>> #format method()
>>> a='motu'
>>> b='patlu'
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> 
>>> 
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> 
>>> 
>>> a=2
>>> b=3
>>> c=a*b
>>> print("{}".format(c))
6
>>> print(f"{c}")
6
>>> 
>>> 
>>> a=40
>>> b=20
>>> c=a*b
>>> print("{}".format(c))
800
>>> print(f"{c}")
800
>>> print("{}".format(a*b))
800
>>> 
>>> a=35
>>> b=60
>>> print("{}".format(a*b))
2100
>>> 
>>> print(f"{a*b}")
2100

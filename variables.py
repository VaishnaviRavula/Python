Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(3+8)
11
a=10
print(a)
10
b=20
print(b)
20
x=40
print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
40
z=50
print(z)
50
3=80
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=80
print(a3)
80
6a=90
SyntaxError: invalid decimal literal
b123456789=500
print(b123456789)
500
@=60
SyntaxError: invalid syntax
_=50
print(_)
50
 =90
 
SyntaxError: unexpected indent
_=100
print(_)
100
if=20
SyntaxError: invalid syntax
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=8
print(a,b)
4 8
a,b=3,4
print(a,b)
3 4
print(b,a)
4 3
a=2,3,4
print(a)
(2, 3, 4)
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(a,b,c)
10 10 10
a,b,c=(2,3,4)
print(a,b,c)
2 3 4
a,b,c=2,3,4,5,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8,9
ValueError: too many values to unpack (expected 3, got 8)
>>> first name="vaishu"
SyntaxError: invalid syntax
>>> first_name="pooja"
>>> print(first_name)
pooja
>>> firstname="vaishu"
>>> print(firstname)
vaishu
>>> fname="vaishu"
>>> lname="ch"
>>> print(fname+lname)
vaishuch
>>> print(fname+" "+lname)
vaishu ch
>>> print(fname,lname)
vaishu ch
>>> a=5
>>> print(a)
5
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> name="vaishu"
>>> print(name)
vaishu
>>> NAME="vaishu"
>>> print(NAME)
vaishu
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> Name="vaishu"
>>> print(Name)
vaishu

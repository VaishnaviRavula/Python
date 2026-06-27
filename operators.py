Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmetic
a=6
b=2
print(a+b)
8
print(a-b)
4
print(a//b)
3
print(a/b)
3.0
print(a**b)
36
print(a%b)
0
#assignment
a=4
b=2
b+=a
b
6
b-=2
b
4
b//=2
b
2
b/=2
b
1.0
b**=2
b
1.0
b%=2
b
1.0
#comparision

a=7
b=3
a>b
True
a<b
False
a==b
False
a!=b
True
a>=b
True
a<=b
False
#Logical

a=6
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a>b and b<a
False
a>=b or a<=b
True
a<b and b<a
False
a<b or b<a
True
a!=b or a==b
True
#Idetity
a=5
type(a) is int
True
a='vaishu'
type(a) is str
True
type(a) is not str
False
a=True
type(a) is bool
True
a=3.9
type(a) is float
True
#Membership

a=1,3,4,5,7,8,9
3 in a
True
15 in a
False
20 not in a
True
#bitwise

a=4
b=2
a&b
0
a=6
b=4
a&b
4
bin(4)
'0b100'
bin(6)
'0b110'
a=3
b=5
bin(3)
'0b11'
bin
<built-in function bin>
bin(5)
'0b101'
a&b
1
a=3
b=5
a|b
7
a=2
b=8
a|b
10
bin(2)
'0b10'
bin(8)
'0b1000'

a=2
-(a+1)
-3
~a
-3
a=5
~a
-6
b=-10
~b
9
c=-50
~c
49
d=45
>>> ~d
-46
>>> a=8
>>> b=3
>>> a^b
11
>>> a=5
>>> b=7
>>> a^b
2
>>> 
>>> a=3
>>> a<<2
12
>>> b=4
>>> b>>2
1
>>> bin(4)
'0b100'
>>> b=6
>>> bin(6)
'0b110'
>>> b>>2
1
>>> a=5
>>> bin(5)
'0b101'
>>> a<<3
40
>>> c=7
>>> bin(7)
'0b111'
>>> c>>3
0
>>> c<<3
56
>>> a=4
>>> a>>2
1

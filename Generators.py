#Generators
#no tuple comprehension in above cases if we rremove those braces and keep paranthesis then outcome is generator.
#a=[expr for var in collection/range]

'''a=[i for i in range(21)]
print(a)
print(type(a))'''

#(expr for var in collection/range)
'''a=(i for i in range(21))
print(a)
print(type(a))
print(*a)
print(type(a))'''

#print(list(a))
#print(tuple(a))
#print(set(a))-- we can give either data type name or star symbol..
#print(*a)-- cannot give both of them at a time.

#main def-- A generator is also a function which can be used as an iterator(loop) by producing group of values where we can use yiels keyword.
# yield vs return-- return will terminate the function ehere as yield can pass the function and go on with every successive iteration.

'''a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''



'''a,b=(int(x) for x in input("enter the values").split(","))
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''



#yield vs return
'''def mygen():
    #return "vja"
    #return "hyd"
    return"vzg"
print(*mygen())'''



'''def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())'''

#next()
'''d=mygen():
print(next(d))
print(next(d))
print(next(d))
#print(next(d))'''#stop iteration..


#tasks...
#right angle yrialgle using stars
'''n=int(input("enter number of rows:"))
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''
#output single line rakunda undataniki we are using print outside the forloop.

#reverse right angle triangle
'''n=int(input("enter number of rows:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''

#square
'''n=int(input("enter number of rows:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''

#pyramid
#for odd
'''n=int(input("enter number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))'''

#for even
'''n=int(input("enter number of values:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("* "*i)'''























#built-in functions

'''print(dir())
print(dir("__builtins__"))'''

'''a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))'''

#fromkeys()- it only works for dictionaries.
'''b=dict.fromkeys(a)
print(b)'''

'''c=dict.fromkeys(a,"vaishu")
print(c)'''

'''c["d"]="vaishu"
print(c)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

#we can give any datatype in eval...instead of giving it seperately.
'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()-> we can combine multiple collections into one collection.
'''a=[10,20,30,40,50]
names=["vaishu","jashu","rani","chutki","kavya"]
print(a+names)'''

'''b=zip(a,names)
print(b)'''
    
'''c=list(zip(a,names))
print(c)'''

'''c=tuple(zip(a,names))
print(c)'''

'''c=set(zip(a,names))
print(c)'''

'''c=dict(zip(a,names))
print(c)'''

#enumerate()-> we can give counter to the collection.
'''names=["vaishu","jashu","rani","chutki","kavya"]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,100))
print(b)

c=list(enumerate(names))
print(c)

b=set(enumerate(names))
print(b)

b=tuple(enumerate(names))
print(b)'''

#ASCII
#chr(),ord()
'''print(chr(65))

print(chr(90))'''

#ord()
'''print(ord("z"))

print(ord("z"))'''

#task
'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

'''n=input()
for i in n:
    print(ord(i),end=" ")'''

#max(),min(),sum()
'''print(max(2,4,8,6,10,44))

print(min(2,4,8,6,10,44))

a=4,5,6,2,1,8
print(sum(a))'''































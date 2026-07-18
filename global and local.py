#global and local variables..
#A variable which is inside and outside the function is called global and local variable
#A variable define above the function and accessible to the entire globsl space is called global variable
#A variable is defined inside the function is called local variable.


#first case of global variables
'''a=3
def check1():
    print("Inside value is",a)
check1()
print("outside value is",a)'''

#second case of global variable
'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

#third case of both global and local variables
'''a=2
b=9
def check3():
    a=7
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=14
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''

#usage of global keyword
#when user wants to access the global variable inside the function directly and carry forward the updated value
#even outside the function then we need to use global keyword.

#usage of global keyword..
'''a=5
def final():
    global a
    print("inside value is",a)
    a=10
    print("updated value is",a)
    global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''


#task(attendence tracker)
n=int(input("no.of students:"))
p=0
a=0
for i in range(1,n+1):
    s=input(f"student{i}(p/a):")
    if s=='p':
        p+=1
    if s=='a':
        a+=1
print("Attendence tracker")
print("no.of students",n)
print("no.of students present",p)
print("no.of students absent",a)




















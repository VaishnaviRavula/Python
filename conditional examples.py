#voting
age=int(input())
if age>=18:
    print("Eligible")
else:
    print("not eligible")


#even or odd
n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")



#leap year
n=int(input())
if (n%100!=0 and n%4==0) or (n%400==0):
    print("leap year")
else:
    print("not leap year")



#Guest code
name=input("Enter a name").lower()
if name=='vaishnavi':
    print("welcome",name)
else:
    print("welcome guest")


n=['vaishu','jashu','rani','raju','rahul']
a=input("enter the name").lower()
if a in n:
    print("welcome",a)
else:
    print("Welcome guest")



#vowels
n=['a','e','i','o','u']
a=input()
if a in n:
    print("vowels")
else:
    print("consonents")


#login
username=input()
password=input()
if username=='vaishnavi':
    if password=='1234':
        print("login successful")
    else:
        print("wrong password")
else:
    print("invalid username")




age=int(input())
marks=int(input())
attendence=int(input())
if age>=18:
    print("eligible to vote")
if marks>80:
    print("eligible for scholarship")
if attendence>=75:
    print("eligible for exam")

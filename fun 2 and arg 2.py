#arguments..
#variable length argumrnts
#these are automatically stores in tuple and we use star arguments.

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[2,3,4,5,6,7]
check(*b)
c={7,8,9,10,11}
check(*c)
d={"year":2026,"month":7}
check(*d)'''


'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,5.3,2.7)
check1(2,3.4,5,6.1,"vaishu")'''#only int and float matrame add avtundhi...strings are not allowed.

#double * argumnets
#kwargs(**)

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"names":["vaishu","raghu","pari"],"marks":[90,80,70],"status":["p","a","a"]}
details(**d)'''


'''def details(**a):
    print(a)
    print(type(a))
details()
d={"names":["vaishu","raghu","pari"],"marks":[90,80,70],"status":["p","a","a"]}
details(**d)'''

#both * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5.2,7.8)
final(*data)
d={"name":["vaishu","raghu"],"marks":[90,90]}
final(**d)
final(*data,**d)'''

#task
'''def railway(Gender,age):
    ticket=1000
    if Gender=="male":
        if age>60:
            print(ticket*0.30)
        else:
            print(ticket)
    if Gender=="female":
        if age>60:
            print(ticket*0.50)
        else:
            print(ticket*0.30)
Gender=input("Enter Gender(male/female):")
age=int(input("enter age"))
railway(Gender,age)'''
            
    




































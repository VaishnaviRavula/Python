'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    c=b//a
    print("per head bill is {}".format(c))
    print(f"perhead bill is {c}")
splitbill()'''


'''def cal():
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(choose the option
                        1.add
                        2.sub
                        3.mul))
    if option==1:
        print(a+b)
    if option==2:
        print(a-b)
    if option==3:
        print(a*b)
cal()'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(choose the option
                        1.add
                        2.sub
                        3.mul))
    if option==1:
        add()
    if option==2:
        sub()
    if option==3:
        mul()'''

    
'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        option=int(input(choose the option
                            1.add
                            2.sub
                            3.mul))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
    cal()'''

#keyword and positional arguments
#first step
'''def Details(id,name,mailid):
    id=10
    name="vaishu"
    mailid="vaishu@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

#second step
#u can add multiple details
'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="vaishu",mailid="vaishu@gmail.com")
Details(id=30,name="raghu",mailid="raghu@gmail.com")'''

#third step
'''def Details(id,name,mailid):
    print(id,name,mailid)
#1 only single user details thiskuntadhi
Details(id="id",name="name",mailid="mailid")
#2 multiple details add cheskovachu
Details(id=20,name="vaishu",mailid="vaishu@gmail.com")
Details(id=30,name="raghu",mailid="raghu@gmail.com")
#3 already paina pos arg ichinsm ksbstti ikkada ivalsina avasaram ledhu...and manam ela isthe alage print avthayi..
Details(40,"renu","renu@gmail.com")
#4 without positional arguments manam jumble ga isthe...jumble ga ne vasthayi..
Details("h@gmail.com","rani",50)
#5 positional arguments isthe manam jumble ga ichina kani avi direct dhani placce lo adhi vastadhi
Details(mailid="r@gmail.com",id=60,name="raju")'''

#default argumenets
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(item="ghee",price):
#non default arg follows default arg
#frst one define chesi scnd one cheyakunda undodhu it will raise the above error.
#like above code frst one define cheyakunda scnd one cheyochu bou not reverse.
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#task
'''def cake(name="pineapple",price=350,qty=1):
    print("name is %s" %name)
    print("price is %.2f" %price)
    print("qty: %.1f" %qty)
cake()'''

'''def cake(name,price,qty):
    print("name is %s" %name)
    print("price is %.2f" %price)
    print("qty: %.1f" %qty)
cake("redvelvet",600,1)'''

'''def cake(name,price=500,qty=2):
    print("name is %s" %name)
    print("price is %.2f" %price)
    print("qty is %s" %qty)
cake("blackforest")'''

'''def cake(name="chocolate",price=400,qty):
    print("name is %s" %name)
    print("price is %.2f" %price)
    print("qty: %.1f" %qty)
cake(2)'''
#this shows error as we didnt defined the qty...


#* arguments (* is used to unpack the elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''b=(5,6,7,8,9)
print(b)
print(*b)'''

'''c={6,7,8,9}
print(c)
print(*c)'''

'''d={"name":"vaishu","year":2020,"month":7}
print(d)
print(*d)'''

'''a="vaishnavi"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(c)'''# shows error

'''a,b,*c=1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(*c)'''

'''a,b,c="vaishnavi"
print(a)
print(b)
print(c)'''#error

'''a,b,*c="vaishu"
print(a)
print(b)
print(*c)'''

'''a,b,c="cod"
print(a)
print(b)
print(c)'''
#as we defined 3 variables we need to insert only 3 values..
#so that it gives output or else it shows error...





    
    




























































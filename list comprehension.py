#list comprehension.
#every list comprehension can be rewritten as forloop but every forloop cannot be rewritten as list comprehension.
#we can use forloop in list comprehension but cannot use list comprehension in forloop.

a=["codegnan","python","course"]
'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#syntax for list comprehension..
#a=[expression for var in collection/ranges]

'''a=[i.upper() for i in a]
print(a)'''

#task 1
'''a=["vja","hyd","vzg"]
b=[i.title() for i in a]
print(b)'''

#task 2
'''a=[1,2,3,5,6,8,12,13]
b=[i**2 for i in a] or [i*i for i in a] or [pow(i,2) for i in a]
print(b)'''

#if-usage in list comprehension
#task 4
#to print even 
'''a=[i for i in range(16) if i%2==0]
print(a)'''

#to print odd
'''a=[i for i in range(16) if i%2!=0]
print(a)'''

#to print 0-20
'''a=[i for i in range(21)]
print(a)'''

#print the fruits which contains letter A
'''fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
b=[i for i in fruits if 'a' in i]
print(b)'''

'''fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]
b=[i for i in fruits if 'a' not in i]
print(b)'''

#no-elif usage in list comprehension

#if-else usage in list comprehension
'''a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]       
print(c)'''
#length is 5 and a[i] lo 0-5 index numbers store ayithayi same for b and rendu add ayithayi..



#atm application..
account_balance = 100000
valid_card = "c"
password = 1234
card = input("Insert the card (Enter c): ")
if card != valid_card:
    print("Invalid Card")
else:
    print("Welcome vaishu")
    pwd = int(input("Enter the Password: "))
    if pwd != password:
        print("Incorrect Password")
    else:
        print("\n----- ATM MENU -----")
        print("1. Balance Enquiry")
        print("2. Withdraw")
        option = int(input("Enter your option: "))
        if option == 1:
            print("Account Balance is:", account_balance)
        elif option == 2:
            amount = int(input("Enter Withdraw Amount: "))
            if amount <= account_balance:
                account_balance = account_balance - amount
                print("Withdrawal Successful")
                print("Remaining Account Balance is:", account_balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Option")
    




































     














































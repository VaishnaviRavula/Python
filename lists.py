Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[3,5.6,"python",9+7j,True,False]
print(a)
[3, 5.6, 'python', (9+7j), True, False]
type(a)
<class 'list'>

a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
#In append we can give only one argument...more than one is not possible.

a=["java","html","css"]
a.extend(["js","bootstrap"])
a
['java', 'html', 'css', 'js', 'bootstrap']
#If you want to give more than one argument then we can use extend.

b=["apple","banana","mango"]
b.insert(1,"grapes")
b
['apple', 'grapes', 'banana', 'mango']
b.insert(0,"watermelon")
b
['watermelon', 'apple', 'grapes', 'banana', 'mango']
#If we want to add an argument in any particular position then we can use "insert".

a=["kiwi","apple","grapes","dragon"]
a.sort()
a
['apple', 'dragon', 'grapes', 'kiwi']
b=[4,1,6,5,9,2]
a.sort()
a
['apple', 'dragon', 'grapes', 'kiwi']
b=[4,1,6,5,9,2]
b.sort()
b
[1, 2, 4, 5, 6, 9]
#sorts the arguments by alphabetical order.

#reverse()
a=["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
b=[6,7,16,4,31,28]
b.reverse()
b
[28, 31, 4, 16, 7, 6]

a=["black","white","pink","brown","red"]
a.pop()
'red'
a.pop(0)
'black'
a.remove("white")
>>> a
['pink', 'brown']
>>> 
>>> a=["vaishu","jashu","rani","raju"]
>>> a.copy()
['vaishu', 'jashu', 'rani', 'raju']
>>> b=a.copy()
>>> b
['vaishu', 'jashu', 'rani', 'raju']
>>> a
['vaishu', 'jashu', 'rani', 'raju']
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
>>> 
>>> a=["ho","hello","when","how","who"]
>>> len(a)
5
>>> b="vaishu"
>>> len(b)
6
>>> c=["hello"]
>>> len(c)
1
>>> c.count()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> count(c)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    count(c)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a=[3,5,1,7,6]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?

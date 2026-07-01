Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a='codegnan'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> 
>>> #positive slicing
>>> a='Time is very precious'
>>> a[8:12]
'very'
>>> a[0:4]
'Time'
>>> a[13:21]
'precious'
>>> 
>>> b='work until you succeed'
>>> b[15:22]
'succeed'
>>> b[5:10]
'until'
>>> b[11:14]
'you'
>>> b[0:4]
'work'
>>> 
>>> a='machine learning'
>>> a[::5]
'mnag'
>>> a[::7]
'm n'
>>> a[:8]
'machine '
>>> a[9:]
'earning'
>>> a[::4]
'miln'
>>> a[::10]
'ma'
>>> a[0;14;2]
SyntaxError: invalid syntax
>>> a[0:14:2]
'mcielan'


a='cloud computing'
a[1:9:2]
'lu o'

a[2:13:3]
'o mt'
a[6:14:4]
'cu'
a[5:12:2]
' opt'
a[3:9:5]
'um'

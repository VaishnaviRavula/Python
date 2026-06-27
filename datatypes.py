Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=5
>>> type(a)
<class 'int'>
>>> b=5.2
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="python"
>>> type(d)
<class 'str'>
>>> e='''vaishu'''
>>> type(e)
<class 'str'>
>>> f=True
>>> type(f)
<class 'bool'>
>>> g=3+4j
>>> type(g)
<class 'complex'>
>>> h=7j+8
>>> type(h)
<class 'complex'>
>>> i=8h+3
SyntaxError: invalid decimal literal
>>> i=7j
>>> type(i)
<class 'complex'>
>>> j=False
>>> type(j)
<class 'bool'>
>>> k=true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    k=true
NameError: name 'true' is not defined. Did you mean: 'True'?

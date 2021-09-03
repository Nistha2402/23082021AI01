Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="mnbadsbnamnbanmbamnbanmbasabns"
>>> list(set(list(s)))
['d', 'n', 'a', 's', 'b', 'm']
>>> {i:s.count(i) for i in s}
{'m': 5, 'n': 7, 'b': 7, 'a': 7, 'd': 1, 's': 3}
>>> t={i:s.count(i) for i in s}
>>> t
{'m': 5, 'n': 7, 'b': 7, 'a': 7, 'd': 1, 's': 3}
>>> u=[]
>>> u=["my string" for i in range(0,6) if t[i]=t[i+1]]
SyntaxError: invalid syntax
>>> u=["my string" for i in range(0,6) if t[i]==t[i+1]]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    u=["my string" for i in range(0,6) if t[i]==t[i+1]]
  File "<pyshell#7>", line 1, in <listcomp>
    u=["my string" for i in range(0,6) if t[i]==t[i+1]]
KeyError: 0
>>> for i in range:
	t[i]

	
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for i in range:
TypeError: 'type' object is not iterable
>>> for i in range(0,7):
	t[i]

	
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    t[i]
KeyError: 0
>>> for i in range(0,7):
	print(t[i])

	
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    print(t[i])
KeyError: 0
>>> t[1]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t[1]
KeyError: 1
>>> t
{'m': 5, 'n': 7, 'b': 7, 'a': 7, 'd': 1, 's': 3}
>>> for i in t:
	print(t[i])

	
5
7
7
7
1
3
>>> u=["my string" for i in t if t[i]=t[i+1]]
SyntaxError: invalid syntax
>>> u=["my string" for i in t if t[i]==t[i+1]]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    u=["my string" for i in t if t[i]==t[i+1]]
  File "<pyshell#22>", line 1, in <listcomp>
    u=["my string" for i in t if t[i]==t[i+1]]
TypeError: can only concatenate str (not "int") to str
>>> for i in t:
	b=[]
	b+=t[i]

	
Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    b+=t[i]
TypeError: 'int' object is not iterable
>>> 
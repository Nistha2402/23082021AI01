Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="this is very nice"
>>> s.split(" ")
['this', 'is', 'very', 'nice']
>>> (",".join(s.split(" ")))
'this,is,very,nice'
>>> (" ".join(s.split(" ")))
'this is very nice'
>>> q=[]
>>> for i in range(0,4):
	s.split(" ")[i][::-1]

	
'siht'
'si'
'yrev'
'ecin'
>>> for i in range(0,4):
	q+=s.split(" ")[i][::-1]

	
>>> q
['s', 'i', 'h', 't', 's', 'i', 'y', 'r', 'e', 'v', 'e', 'c', 'i', 'n']
>>> for i in range(0,4):
	q[i]=s.split(" ")[i][::-1]

	
>>> q
['siht', 'si', 'yrev', 'ecin', 's', 'i', 'y', 'r', 'e', 'v', 'e', 'c', 'i', 'n']
>>> 
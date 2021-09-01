Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # exponent operation
>>> 5**9
1953125
>>> # floor division
>>> 3//2
1
>>> 7//3
2
>>> # assignmenr
>>> 6 == 6
True
>>> a=20;a+=30;a%=3;print(a)
2
>>> 50 % 3
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>>  ((6>3) and (7<4) or (18==3)) and (9>3)
 
SyntaxError: unexpected indent
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False is True
False
>>> False is False
True
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> False in False
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    False in False
TypeError: argument of type 'bool' is not iterable
>>> ((True == False) or (False> True)) and (False<=True)
False
>>> False<True
True
>>> s1 = "Nice to have it"
>>> s2="here"
>>> s1+s2
'Nice to have ithere'
>>> s1+" "+s2
'Nice to have it here'
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> a.append(s2)
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> a.insert(0,s1)
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
... 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
... 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
... 742, 717, 958,743, 527]
SyntaxError: invalid syntax
>>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,687,217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,742, 717, 958,743, 527]
>>> 
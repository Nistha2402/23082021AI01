Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,6):
	print("*" *i)

	
*
**
***
****
*****
>>> for i in range(1,6):
	print(" " *(5-i),end="")
	print("*" *i)

	
    *
   **
  ***
 ****
*****
>>> for i in range(1,7):
	for i in range(1,i):
		print(i,end="")
	print("")

	

1
12
123
1234
12345
>>> for i in range(1,7):
	print(f"{i}" *i)

	
1
22
333
4444
55555
666666
>>> for i in range(1,6):
	print(f"{i}" *i)

	
1
22
333
4444
55555
>>> for i in range(1,6):
	print("*" *i,end="")
	print(" " *(10-2*i),end="")
	print("*" *i)

	
*        *
**      **
***    ***
****  ****
**********
>>> 
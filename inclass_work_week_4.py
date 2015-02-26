Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mylist = list ("Hello world")
>>> 
>>> mylist
['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> 
>>> x = [1,2,3]
>>> x
[1, 2, 3]
>>> y = []
>>> y
[]
>>> type (y)
<class 'list'>
>>> 
>>> x[1] = 7
>>> print (x)
[1, 7, 3]
>>> 
>>> # it start counting from "0"
>>> names = ["enes" , "yunus" , "emre" , "bedir" ]
>>> del names [3]
>>> 
>>> print(names)
['enes', 'yunus', 'emre']
>>> 
>>> name = list("perl")
>>> print(name)
['p', 'e', 'r', 'l']
>>> name[2:] list("ar")
SyntaxError: invalid syntax
>>> name[2:] = list("ar")
>>> print list
SyntaxError: Missing parentheses in call to 'print'
>>> print (name)
['p', 'e', 'a', 'r']
>>> 
>>> #interesting ":" mean after this "4:" mean after 4thplace
>>> 
>>> krypton = ["krypton" , "KR", -157.12 , 153, True]
>>> krypton [3]
153
>>> krypton [2]
-157.12
>>> 
>>> len(krypton)
5
>>> half_lives = [67, 45,  4333, 4333]
>>> max(half_lives)
4333
>>> sum(half_lives)
8778
>>> sorted(half_lives)
[45, 67, 4333, 4333]
>>> lst = [1,2,3]
>>> lst.append(4)
>>> print(lst)
[1, 2, 3, 4]
>>> lst.append(659)
>>> print(lst)
[1, 2, 3, 4, 659]
>>> lst
[1, 2, 3, 4, 659]
>>> print(["to", "be", "or" , "not" "to" ])
['to', 'be', 'or', 'notto']
>>> print(["to", "be", "or" , "not" ,"to" ]).count("to")
['to', 'be', 'or', 'not', 'to']
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(["to", "be", "or" , "not" ,"to" ]).count("to")
AttributeError: 'NoneType' object has no attribute 'count'
>>> print(["to", "be", "or" , "not" ,"to" ]).count("to"))
SyntaxError: invalid syntax
>>> print(["to", "be", "or" , "not" ,"to" ].count("to"))
2
>>> a = a.append(b)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a = a.append(b)
NameError: name 'a' is not defined
>>> knights = [ "we" , "are" , "knights"]
>>> knights.index("are")
1
>>> knights.index("me")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    knights.index("me")
ValueError: 'me' is not in list
>>> lst.append("me")
>>> knights.append("me")
>>> knights
['we', 'are', 'knights', 'me']
>>> 

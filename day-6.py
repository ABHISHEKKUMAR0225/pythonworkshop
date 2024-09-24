Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="Abhishek"
type(s)
<class 'str'>
s='Abhi'
type(s)
<class 'str'>
y="""hbgrgguibfhjbvf8vbjvj
ijifmikmc
rficmicmci"""
type(y)
<class 'str'>
y
'hbgrgguibfhjbvf8vbjvj\nijifmikmc\nrficmicmci'
s[0]
'A'
s[1]
'b'
s[5]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[5]
IndexError: string index out of range
s[1]
'b'
s[-1]
'i'





s="This is GEC Vaishali Pyhon Workshop."
s[0:4]
'This'
s[5:6]
'i'
s[5:7]
'is'

s[0:-4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s[-4:-1]
'hop'


s[-1:-9]
''
s[-9:-1]
'Workshop'
s[1:5]
'his '






s="abhishek"
j="kumar"
s+j
'abhishekkumar'






s="Abhishek"
print("My name is %s"%s)
My name is Abhishek




s="{} is a state college".format("GEC VAISHALI")
s
'GEC VAISHALI is a state college'





p="Abhishek"
print("My name is %s"%s)
SyntaxError: multiple statements found while compiling a single statement
p="Abhishek"
print("My name is %p"%p)
SyntaxError: multiple statements found while compiling a single statement
p="Abhishek"
print("My name is %s"%p)
SyntaxError: multiple statements found while compiling a single statement
s="Abhishek"
print("My name is %p"%s)
SyntaxError: multiple statements found while compiling a single statement


KeyboardInterrupt
s="Abhishek"
print("My name is %s"%s)
SyntaxError: multiple statements found while compiling a single statement




l=[7,"abhihek",4.5,True]
type(l)
<class 'list'>
l[1]
'abhihek'
l[0]=76
l[0]
76
l
[76, 'abhihek', 4.5, True]
l[1]=Abhishek
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    l[1]=Abhishek
NameError: name 'Abhishek' is not defined
l[1]="Abhishek"
l
[76, 'Abhishek', 4.5, True]



l.append(65)
l
[76, 'Abhishek', 4.5, True, 65]

l.insert(2,45)
l
[76, 'Abhishek', 45, 4.5, True, 65]
l.insert(2,135)
l
[76, 'Abhishek', 135, 45, 4.5, True, 65]
l.pop()
65
l
[76, 'Abhishek', 135, 45, 4.5, True]
l.remove(4.5)
l
[76, 'Abhishek', 135, 45, True]




>>> l[1:3]
['Abhishek', 135]
>>> l[0:3]
[76, 'Abhishek', 135]
>>> len(l)
5
>>> 
>>> 
>>> 
>>> 
>>> 
>>> t=(5,"Abhishek",7.5)
>>> type(t)
<class 'tuple'>
>>> t[0]
5
>>> t[0]=3
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    t[0]=3
TypeError: 'tuple' object does not support item assignment
>>> #touple can`t be edited or deleted
>>> 
>>> 
>>> #listing can edited
>>> 
>>> 
>>> 
>>> 
>>> #SET
>>> 
>>> sets={"MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"}
>>> type(sets)
<class 'set'>
>>> sets2=(["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"])
>>> type(sets)
<class 'set'>
>>> type(sets2)
<class 'list'>
>>> sets=(["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"])
>>> sets2=(["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"])
>>> type(sets2)
<class 'list'>
>>> sets2=set(["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"])
>>> type(sets2)
<class 'set'>

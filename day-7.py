Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={"MON","TUE","WED"}
type(s)
<class 'set'>
s[1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[1]
TypeError: 'set' object is not subscriptable
s.add("THU")
s
{'WED', 'TUE', 'MON', 'THU'}
s.update("FRI")
S
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
s
{'R', 'WED', 'F', 'I', 'MON', 'THU', 'TUE'}
s.remove("MON")
s
{'R', 'WED', 'F', 'I', 'THU', 'TUE'}
s.discard("TUE")
s
{'R', 'WED', 'F', 'I', 'THU'}



#dictionary
D={}
type(D)
<class 'dict'>
D={"101":"civil","102":"ME","105":"CSE"}
D
{'101': 'civil', '102': 'ME', '105': 'CSE'}
D.keys()
dict_keys(['101', '102', '105'])
D.values()
dict_values(['civil', 'ME', 'CSE'])
D[105]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    D[105]
KeyError: 105
D[105]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    D[105]
KeyError: 105
D["105"]
'CSE'
D["105"]="CSE(IOT)"
D
{'101': 'civil', '102': 'ME', '105': 'CSE(IOT)'}
D.pop("105")
'CSE(IOT)'
D
{'101': 'civil', '102': 'ME'}

D.items()
dict_items([('101', 'civil'), ('102', 'ME')])

D.update({"105":["CSE"]})
D
{'101': 'civil', '102': 'ME', '105': ['CSE']}
















#OOPS


class Car:
    def__init__(self):
        
SyntaxError: invalid syntax


class car:
    def __init__(self):
        self.brand-"Suzuki"
        self.color="Blue"
        self.top_speed=200

        
car=car()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    car=car()
  File "<pyshell#62>", line 3, in __init__
    self.brand-"Suzuki"
AttributeError: 'car' object has no attribute 'brand'
car=Car()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    car=Car()
NameError: name 'Car' is not defined. Did you mean: 'car'?
Car=Car()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    Car=Car()
NameError: name 'Car' is not defined. Did you mean: 'car'?
Car=car()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    Car=car()
  File "<pyshell#62>", line 3, in __init__
    self.brand-"Suzuki"
AttributeError: 'car' object has no attribute 'brand'
class Car:
    def __init__(self):
        
        self.brand-"Suzuki"
        self.color="Blue"
        self.top_speed=200

        
car=Car()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    car=Car()
  File "<pyshell#68>", line 4, in __init__
    self.brand-"Suzuki"
AttributeError: 'Car' object has no attribute 'brand'
car=Car()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    car=Car()
  File "<pyshell#68>", line 4, in __init__
    self.brand-"Suzuki"
AttributeError: 'Car' object has no attribute 'brand'
class Car:
    def __init__(self):
        
        self.brand="Suzuki"
        self.color="Blue"
        self.top_speed=200

        
car=Car()
car.brand
'Suzuki'
car.color
'Blue'
car.top_speed
200



class Car:
    def __init__(self,b,c,ts):
        
        self.brand=b
        self.color=c
        self.top_speed=ts

        
car=Car("Maruti","Black",150)
car.brand
'Maruti'
car=Car("Tata","Grey",250)
car.brand
'Tata'



>>> 
>>> class Car:
...     def __init__(self,b,c,ts):
...         
...         self.brand=b
...         self.color=c
...         self.top_speed=ts
...     def accelerate(self):
...         print("Your car top speed is:",self.top_speed)
... 
...         
>>> car=Car("Tata","Grey",250)
>>> car.accelerate()
Your car top speed is: 250
>>> 
>>> 
>>> 
>>> #doing itself
>>> class Dog:
...     def __init__(self,a,b,c):
... 
...         self.color=a
...         self.eat=b
...         self.brand=c
...     def accelerate(self):
...         print("Your dog is:",self.brand)
... 
...         
>>> dog=Dog("White","Bone","Lebra")
>>> dog.accelerate()
Your dog is: Lebra
>>> 
>>> 
>>> class College:
...     def __init__(self,n,loc):
...         self.name=n
...         self.location=loc
...     def msg(self):
...         print(self.name+" is prsent at "+self.loc)
... 
...         
>>> class Department(College):
...     def __init__(self,name,ids):
...         self.id=ids
... 
...         

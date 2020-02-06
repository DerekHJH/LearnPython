#General Knowledge 
#For immutable object, any method acted on them will not change their contents, intead, a new object with the changed value is created.



#list and tuples
#classmates=['Derek','Dick','Bob'];
#print them out classmates
#len(classmates)
#classmates[-len,len-1];
#classmates.append('Adam');
#classmates.insert(1,'Jack');
#classmates.pop() delete the last element
#classmates.pop(1) delete the first element
#L=['=Apple',1,True,[1,2,3]];
#tuple is the same as lists except that the elements cannot be changed.
#t=(1) is not a tuple we can use t=(1,);
#classmets.sort();
#classmates[0:3]/classmates[:0]; Get 0-2 elements;
#classmates[-2:0]/classmates[-2:]; Get -2,-1 elements;
#L=list(range(100));
#L=[0:10:2]; Get one every two;
#L=[::5]; Get among all numbers every 5;
#L[:]; All numbers/The list itself
#[::] also applies to strings and tuples





#dict
#d=['Derekerek':95,'Bob':75,'Dick':85];
#d['Derek'];
#d['Derek']=100;
#'Derek' in d;  return True or False
#d.get('Derek'); If not foundd return None;
#d.get('Derek',-1); If not found return -1;
#d.pop('Derek');Delete 'Derek' and return its value;
#key of dict should be immutable object

#set
#s=set([1,2,3]); Use a list to initialize a set, distinct elements;
#s.add(4);
#s.remove(4);
#s1=([1,2,3]);
#s2=([2,3,4]);
#s1&s2;
#s1|s2;
#Should put in immutable object

#string
#a='abc';
#a.replace('a','A'); Return 'Abc' but a itself is not changed.











#检查传入参数类型并抛出异常
'''
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('Bad Operand Type\n');
	if x>=0:
		return x;
	else:
		return -x;
'''
#什么都不做可用nop
'''
def nop():
	pass;
'''
#返回多个元素实际上是返回一个tuple
'''
import math
def Move(x,y,Step,Angle=0):
	nx=x+Step*math.cos(Angle);
	ny=y+Step*math.sin(Angle);
	return nx,ny;
x,y=Move(0,0,100,math.pi/4);
print(x,y);
'''

#默认参数，默认参数必须指向不变对象
'''
def Power(a,b=2):
	ans=1;
	while(b>0):
		if(b&1):
			ans=ans*a;
		a=a*a;
		b>>=1;
	return ans;
'''

#可变参数
'''
def Calc(*Numbers):
	sum=0;
	for x in Numbers:
		sum+=x;
	return sum;
'''
#tuple=(1,2,3);
#Calc(*tuple);

#关键字参数
'''
def person(name, age, **kw):
	print('name:',name,'age:',age,'other',kw);
'''
#person('Michael',30,city='Bejing',gender='M');
#name:Michael age:30 other: {'city': 'Bejing', 'gender': 'M'}
#extra={'city':'Bejing','gender':'M'};
#person('Michael',30,**extra); create another copy of extra
#def person(name, age, *, city, job)#after * the parameters are named keyword parameters
#def person(name, age, *args, city, job)#after *args the parameters are named keyword parameters
#Any function can be declared as func(*args,**kw);

#尾递归优化
#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，
#需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
'''
def fact(n):
	return fact_iter(n, 1);

def fact_iter(num, product):
	if num == 1:
		return product;
	return fact_iter(num - 1, num * product);
'''
#可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。

#iteration
#for value in 'ABC':
#for value in d.values():
#for k,v in d.items():
#import collections import Iterable
#isinstance([1,2,3],Iterable); ---True
#for i,v in enumerate([1,2,3]):  #Turn a list into an index-value pair;

#List Comprehensions
#L=list(renge(1,11); generate 1-10
#[x*x for x in range(1,11)]; Generate [1,4,9....100];
#[x*x for x in range(1,11) if x%2==0]; Generate [4,16....100];
#[m+n for m in 'ABC' for n in 'XYZ'];
#L = ['Hello', 'World', 'IBM', 'Apple'];
#[s.lower() for s in L]; Change to lower case letter;

#genertor
#g=(x*x for x in range(1,11));
#next(g);Getting the next element, irreversible;
#for n in g:  irreversible
'''
def fib(Max):
	n,a,b=0,0,1;
	while(n<Max):
		yield b;
		a,b=b,a+b;
		n=n+1;
	return 'done';
	'''
#irreversible, every time stop at yield and next time resume right after yield
#With function generator, we cannot directly get the returned value.
#isinstance(fib(6),Iterator);
'''
g=fib(6);
while True:
	try:
		x=next(g);
		print('g:',x);
	except StopIteraion as e:
		print("Generator return value:",e.value);
		break;
'''
#Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算.
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的
#L=[1,2,3,4,5];
#L=iter(L); change a list into a generator;

#f=abs; #Let f point to the function abs;abs(-10)=f(-10);
#由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。
#那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

#map(func, Iterable), return Iterator
'''
def f(x):
	return x*x;
r=map(f,list(range(1,11)));
r=list(r);#calculate them all and group as a list.
'''
#list(map(str,list(range(1,11))));

#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#from functools import reduce;
'''
def add(x,y):
	return x+y;
L=reduce(add,range(1,11));
'''
#it equals to that L=sum(range(1,11));
'''
Digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9};
def str2int(s):
	def fn(x,y):
		return 10*x+y;
	def char2num(s):
		return Digits[s];
	return reduce(fn,map(char2num,s));#change the list into an integer
'''

#filter
'''
def is_odd(x):
	return x%2==1;
L=filter(is_odd,range(1,101)); # return an iterator
'''
#Filter the prime numbers
'''
def iter_odd():
	x=1;
	while(True):
		x=x+2;
		yield x;

def not_divisable(n):
	return lambda x:x%n>0;
	
def Prime():
	yield 2;
	it=iter_odd();
	while(True):
		n=next(it);
		yield n;
		it=filter(not_divisable(n),it);

for x in Prime():
	if(x<100):
		print(x);
	else:
		break;
'''

#sorted
#sorted([2,5,-9,-1,15]);
#sorted([2,5,-9,-1,15],key=abs);
#sorted([2,5,-9,-1,15],key=abs,reverse=True);

#return functions
#我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
#相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''
def lazy_sum(*args):
	def sum():
		ans=0;
		for x in args:
			ans=ans+x;
		return ans;
	return sum;
L=tuple(range(1,11));
L=lazy_sum(*L);
R=tuple(range(12,20));
R=lazy_sum(*R);
print(L());
print(R());
'''
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
def Count():
	fs=[];
	for i in range(1,4):
		def f():
			return i*i;
		fs.append(f);
	return fs;
f1,f2,f3=Count();
'''

#Anonymous function --- lambda 
#L=list(map(lambda x:x*x,list(range(1,11))));
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#f=lambda x:x*x;

#Decorator
#abs.__name__; function's name in string
#把@log放到now()函数的定义处，相当于执行了语句：now=log(now)

#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
#但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)
#本质上，decorator就是一个返回函数的高阶函数——既可以接受函数参数，又可以返回函数
'''
import functools
def log(func):
	def wrapper(*args,**kw):
		@functools.wraps(func);#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
		print("call %s():"%func.__name__);
		return func(*args,**kw);
	return wrapper;#Notice the difference between return wrapper and return wrapper(*args,**kw);
@log
def now():
	print("2020-1-17");
'''
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
'''
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__));
			return func(*args, **kw);
		return wrapper;
	return decorator;
'''

#Partial function
#int('32154',base=8);
#import functools
#int2=functools.partial(int,base=2);
#int2(x)==int(x,base2)把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值 int2('3132',base=10);
#max2=functools.partial(max,10)
#max2(1,2,3)==max(10,1,2,3);

#模块部分阅读“模块”

#面向对象
#可以自由地给一个实例变量绑定属性，比如，给实例Derek绑定一个gender属性只需要Derek.gender='M'
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的,
#通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量,不同版本的Python解释器可能会把__name改成不同的变量名。
#在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
#你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#直接改__Name，表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。
'''
class Student(object):
	def __init__(Self,Name,Score):
		Self.__Name=Name;
		Self.__Score=Score;
	def Print_Self(Self):
		print("%s:%s"%(Self.__Name,Self.__Score));
	def Get_Name(Self):
		return Self.__Name;
	def Get_Score(Self):
		return Self.__Score;
	def Set_Score(Self,Score):
		if(0<=Score<=100):
			Self.__Score=Score;
		else:
			raise ValueError("Bad Score!");
'''
#isinstance(b, Animal)
#实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。Animal的子类也属于Animal
#“开闭”原则：
#对扩展开放：允许新增Animal子类；
#
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''
class Animal(object):
	def Run(Self):
		print("Animal is running...");
class Dog(Animal):
	def Eat(Self):
		print("Eating meat...");
	def Run(Self):
		print("Dog is running...");
class Cat(Animal):
	def __len__(Self):
		return 101;
'''
#type(dog)==Animal;True
#import types
#type(abs)==types.BuitinFunctionType
#type((x for x in range(10)))==types.GeneratorType
#type(lambda x: x)==types.LambdaType
#type(fn)==types.FunctionType     Selfdefined
# isinstance((1, 2, 3), (list, tuple)) list or tuple
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
#dir('ABC');
#如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
#想用len()函数作用的对象自己本身必须要有__len__方法
#剩下的都是普通属性或方法，比如lower()返回小写的字符串,不需要含有任何方法来支持
'''
dog=Dog();
hasattr(dog,'Name');#是否有这个属性
setattr(dog,'Age',2);#Set one attribute
getattr(dog,'Age');#get the value of this attribute
getattr(dog,"Gender","M")#可以传入一个default参数，如果属性不存在，就返回默认值
fn=getattr(dog,Eat);
fn();
'''
'''
class Student():
	Name="Student";
s=Student();
print(s.Name);
print(Student.Name);
s.Name='Derek';
print(s.Name);
del s.Name;
print(s.Name);
'''

#Tied a method to an instance
#class Student(object):
#	__slots__=("Name","Age");#Only these two attributes are permitted to be added
#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
#def Set_Age(Self,Age):
#	Self.Age=Age;
#from types import MethodType
#s.Set_Age=MethodType(Set_Age,s);
#给一个实例绑定的方法，对另一个实例是不起作用的：
#为了给所有实例都绑定方法，可以给class绑定方法：
#Student.Set_Age=Set_Age;
#s=Student();
#s.name="Derek";
#上面的Set_Age方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
'''
@property
class Student(object):
	__slots__=("__Score");
	@property
	def Score(Self):
		return Self.__Score;
	@Score.setter
	def Score(Self,Value):
		if not isinstance(Value,int):
			raise ValueError("Score must be an integer!!");
		if Value<0 or Value>100:
			raise ValueError("Score must be between 0 and 100!!");
		Self.__Score=Value;
'''
#只定义getter方法(上面的property)，不定义setter(下面的Score.setter)方法就是一个只读属性

#__str__
'''
class Student(object):
	__slots__=("Name");
	def __init__(Self,Name):
		Self.Name=Name;
	def __str__(Self):#print(s) can be more clear
		return "Student object Name:%s"%Self.Name;
	__repr__=__str__;#directly s can be shown clearly
'''
#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
'''
class Fib(object):
	def __init__(Self):
		Self.a,Self.b=0,1;
	def __iter__(Self):
		return Self;
	def __next__(Self):
		Self.a,Self.b=Self.b,Self.a+Self.b;
		if(Self.a>100000):
			raise StopIteration();
		return Self.a;
'''
'''
class Fib(object):
	def __getitem__(Self,n):
		if(isinstance(n,int)):
			a,b=1,1;
			for x in range(n):
				a,b=b,a+b;
			return a;
		elif(isinstance(n,slice)):
			Start=n.start;
			Stop=n.stop;
			if(Start is None):
				Start=0;
			a,b=1,1;
			L=[];
			for x in range(Stop):
				if(x>=Start):
					L.append(a);
				a,b=b,a+b;
			return L;
'''
#没有对step参数作处理,也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的
#与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

#只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
'''
class Student(object):
	def __getattr__(Self,Attr):
		if(Attr=="Score"):
			return 100;
		else:
			raise AttributeError("\'Student\' object does not have an attribute \'%s\'"%Attr);
'''
'''
class Student():
	def __init__(Self,Name="Derek"):
		Self.Name=Name;
	def __call__(Self):
		print("My name is %s"%Self.Name);
callable(Student)==True;#Check if it is callable
'''

'''
from enum import Enum
Month=Enum('Month',("Jan","Feb"));
for Name,Member in Month.__members__.items():
	print(Name,"=>",Member,',',Member.value);
'''

#Enumerate class
'''
from enum import Enum, unique;
@unique #To check if there is any repeated numbers;
class Weekday(Enum):
	Sun=0;
	Mon=1;
	Tue=2;
	Wed=3;
	Thu=4;
	Fri=5;
	Sat=6;
'''
#Weekday.Mon is a value instead of a variable
#Weekday['Mon']==Weekday.Mon==Weekday(1);

#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，
#比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
#要创建一个class对象，type()函数依次传入3个参数：
#1. class的名称；
#2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。(已经在外面写好了函数就不用再写了，直接绑定就可以)
'''
def fn(Self,Name="World"):
	print("Hello %s"%Name);
Hello=type("Hello",(object,),dict(hello=fn));
h=Hello();
h.hello();
'''
#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

#metaclass:先定义metaclass，就可以创建类，最后创建实例。
#metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

#try except finally
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
#执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
'''
try:
	print("I am trying...");
	r=10/int('a',base=16);
	print("the result is %d"%r);
except ZeroDivisionError as e:
	print("Except:",e);
except ValueError as e:
	print("ValueError",e);
else:
	print("No error!!");#If no error occurs, we print "no error"
finally:
	print("Finally...");
print("END");
'''
#Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
#所以入如多第一个except捕获的是BaseException，那么后面的所有异常都无法捕获。

#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
#也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
#如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息(调用栈)，然后程序退出。
'''
def foo(s):
	return 10 / int(s);
def bar(s):
	return foo(s) * 2;
def main():
	try:
		bar('0');
	except Exception as e:
		print('Error:', e)
	finally:
		print('finally...');
'''
#logging模块可以非常容易地记录错误信息,同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
'''
import logging;
def foo(s):
	return 10 / int(s);
def bar(s):
	return foo(s) * 2;
def main():
	try:
		bar('0');
	except Exception as e:
		logging.exception(e);
	finally:
		print('finally...');
main();
print("END");
'''

#如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
#只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
'''
class FooError(ValueError):
	pass;
def foo(s):
	n=int(s);
	if(n==0):
		raise FooError("Invalid value %s"%s);
	else:
		return 10/n;
def bar():
	try:
		foo('0');
	except FooError as e:
		print("ValueError!");
		raise;
'''
#由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
#raise语句如果不带参数，就会把当前错误原样抛出
#在except中raise一个Error，还可以把一种类型的错误转化成另一种类型,但是，决不应该把一个IOError转换成毫不相干的ValueError
'''
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
'''

#assert 0==1,"hahahha";
#不过，启动Python解释器时可以用-O(大写的O)参数来关闭assert
'''
import logging;
logging.basicConfig(level=logging.INFO);#加上这句话之后才会显示错误信息
n=0;
logging.info("n=%d"%n);
print(10/n);
'''
#这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
#当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
#debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#pdb启动输入python -m pdb haha.py
'''
import pdb;
s='0';
n=int(s);
pdb.set_trace();
print(n/0);
'''

#单元测试和文档测试没有看
'''
try:
	f=open("test.txt","r");
	print(f.read());#一次性读完
finally:
	if(f):
		f.close();
'''
#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
#所以，为了保证无论是否出错都能正确地关闭文件,我们可以使用try ... finally来实现：
#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
'''
with open("test.txt","r") as f:
	print(f.readline());#调用readline()可以每次读取一行;
	print(f.read(5));#一次性读5字节
	print(f.readlines());#调用readlines()一次读取所有内容并按行返回list
'''
'''
f=open("test.txt","r",encoding="utf8",errors="ignore");#遇到编码错误直接忽略
for Line in f.readlines():
	print(Line.strip());#去掉\n;
f.close();
'''
#你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
#with open("Write.txt","a",encoding="utf8",errors="ignore") as f:#append
#	f.write("Hello World!!");

#stringIO
'''
from io import StringIO;
f=StringIO("initialization with string\n");
f.write("Hellow!!!!!\n");#返回成功写入的字符数
f.write("World!!!\n");#会被initialzation覆盖掉，但是不会覆盖Hellow
print(f.getvalue());
while True:
	s=f.readline();
	if(s==""):
		break;
	print(s.strip());
'''
#BytesIO
'''
from io import BytesIO;
f=BytesIO();#括号内可用来初始化
f.write("傻逼".encode("utf-8"));
print(f.getvalue());
'''

#os.name如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
#要获取某个环境变量的值，可以调用os.environ.get('key')：
'''
import os;
print(os.path.abspath("."));
print(os.path.join("F:/Temp","testdir"));#os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
#os.mkdir("testdir2");
os.rmdir(os.path.join("F:/Temp","testdir2"));
'''
'''
import os;
#os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split(os.path.abspath(".")));
'''
#os.rename("test.txt","test.py");
#os.remove("test.py");
#幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#import os;
#print([x for x in os.listdir(".") if os.path.isdir(x)]);
#print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splittext(x)[1]==".py"]);#Windows 下没有splittext







#初识函数
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError("bad operand type")
	if x>=0:
		return x
	else:
		return -x
print(my_abs(1))

#多参函数的设置
import math
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y+step*math.sin(angle)
	return nx,ny

#默认参数
def enroll(name,gender,age=13,city='Beijing'):
	print("name:",name)
	print("gender:",gender)
	print("age:",age)
	print("city:",city)

def add_end(L=[]):
	L.append("END")
	return L

#可变参数
def calc(*number):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

#关键字参数
def person(name,age,**kw):
	print("name:",name,"age:",age,"other:",kw)

#命名关键字参数
def person(name,age,*,city,job):
	print(name,age,city,job)	
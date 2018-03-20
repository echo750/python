class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s:%s' %(self.name,self.score))
#__init__方法的第一个参数永远是self，
#表示创建的实例本身，在__init__方法内部，
#可以把各种属性绑定到self，因为self就指向创建的实例本身
#有了__init__方法，在创建实例的时候，就不能传入空参数，
#必须传入与该方法匹配的参数，但是self不需要传。

bart=Student('Bart Simpson',98)
bart.name
bart.print_score()
# 在类中定义的函数与普通函数只有一点不同，
# 就是第一个参数永远是实例变量self

class Student1(object):
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
    def get_gender(self):
        return self._gender
    def set_gender(self,gender):
        self._gender=gender
# 测试:
bart = Student1('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Animal(object):
	  def run(self):
	  	  print("Animal is running")

class Dog(Animal):
	pass
class Cat(Animal):
	pass

class Dog(Animal):
	def run(self):
		print("Dog is running...")
dog=Dog()
dog.run()

def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())
run_twice(Dog())

class Tortoise(Animal):
	def run(self):
		print('Tortoise  is running slowly...')
run_twice(Tortoise())
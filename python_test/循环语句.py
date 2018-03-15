#print absolute value of an interger;
#循环语句
#if和elif
a=100
if a>100:
	print(a)
else:
	print(-a)

age=5
if age>=18:
	print("your age is",age)
	print("adult")
elif age>=12:
	print("your age is",age)
	print("teenager")
else:
	print("your age is",age)
	print("kid")

#for循环
names=["John","Non"]
for name in names:
	print(name)
sum=0
for x in [1,2,3,4,5]:
	sum=sum+x
print(sum)

sum=0
for x in range(101):
	sum=sum+x
print(sum)
#while循环
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print(sum)

n=1
while n<=100:
	if n>10:
		break
	print(n)
	n=n+1
print("End")
#1���淶Ӣ����ĸ
def normalize(name):
    return name[0].upper()+name[1:].lower()

# ����:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#2����reduce()���
def prod(L):
    def f1(x,y):
        return x*y
    return reduce(f1,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('���Գɹ�!')
else:
    print('����ʧ��!')


#3�����ַ���'123.456'ת���ɸ�����123.456
from functools import reduce

def str2float(s):
    def fn(s):
        d={'.':'.','1':1,'2':2,'3':3,'4':4,'5':5,'6':6}
        return d[s]
    def fm(x,y):
        return x*10+y
    n=0
    for index,value in enumerate(s):
        if value=='.':
           n=index;
    return reduce(fm,map(fn,s[0:n]))+(0.1**len(s[n+1:]))*(reduce(fm,map(fn,s[n+1:])))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('���Գɹ�!')
else:
    print('����ʧ��!')
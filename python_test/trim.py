#����1��
def trim(s):    
    if len(s)==0:
       return s
    elif s[0]==' ':
         return trim(s[1:])
    elif s[-1]==' ':
         return trim(s[:-1])
    return s


#����2��
def trim(s):
    length=len(s)
    for i in range(length):
	if s[i]!='':
	   break
    j=length-1
    while s[j]==' 'and j>=i:
          j-=1
    s=s[i:j+1]
    return s


# ����:
if trim('hello  ') != 'hello':
    print('����ʧ��!')
elif trim('  hello') != 'hello':
    print('����ʧ��!')
elif trim('  hello  ') != 'hello':
    print('����ʧ��!')
elif trim('  hello  world  ') != 'hello  world':
    print('����ʧ��!')
elif trim('') != '':
    print('����ʧ��!')
elif trim('    ') != '':
    print('����ʧ��!')
else:
    print('���Գɹ�!')


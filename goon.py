print('liu \'kang  "jjjj"')
# 原始字符串
print(repr('love \nnijiushi'))
print(str('hah,\nwangba'))
print('''hhhhhhh\dfdgfdfgdf\gdfdgdfg\ndfgdfg''')
# 打印路径的时候
print('c:\liukang\lk')
print(r'c:\nliukang\lk')
num=[1,2,3,4,5,6,7,8,9,10]
print(num[5::-2])
name=list('perl')
name[1:]=list('ar')
print(name)
name[1:]=[]
print(name)
name[1:]=list('python')
print(name)
del name[1:3]
print(name)
qing=[1,2,3]
wang=[4,5,6]
# qing[len(qing):]=wang
qing.extend(wang)
qing.insert(9,2)
print(qing)
print(qing.pop())
print(qing)
from  math import pi
Q='{name} is number {value:.2f}.'.format(value=pi,name='qingbang')
Q1='{name} is number {value:.3f}.'.format(value=pi,name='qingbang')
print(Q)
print(Q1)
A='{},{}and{}'.format(1,2,3)
print(A)
print('{0:<10.2f}\n{0:>10.2f}\n{0:^10.2f}'.format(pi))
print('192.168.2.7'.center(40,'*'))
print('192.168.2.7'.center(30,'*'))
print('192.168.2.7'.center(20,'*'))
print('192.168.2.7'.center(15,'*'))
print('192.168.2.7'.find('168'))
print('192.168.2.7'.split('.'))
print('   192.168.2.7   '.strip())
'''name=input('company:')
if name.endswith('qingbang'):
    print('qingbang,192.168.0.1')'''
parse=1
assert 0<parse<2,'wrong'


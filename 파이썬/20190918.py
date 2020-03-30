print(format(3.141593, '10.3f'))
import math 
for k in range(1,3) : 
    print('sqrt({0}) = {1}'.format(k, math.sqrt(k)))
import math 
for k in range(1,3) : 
    print('sqrt({0}) = {1:5.3f}'.format(k, math.sqrt(k))) 
a =1;a < 0
True + True
bool(3)
a=2; bool(a>3)
s= "Hello World!"
s[0]
s[-1]
s[1:]
s[::-1]
s[::2]

'Hello' + 'World!'
'world' in s
'World' in s
'World' not in s
s.upper() #대문자로 전환
s.split() #공백을 기준으로 분리return list
s.find('World') #부문 문자열의 위치
s.find('wordl') #없으면 -1
s.startswith('Hello') # 시작부분 문자열 확인
s.endswith('ld') # 끝부분 문자열 확인
s.encode()
b=b"Hello World!"
b
type(b)
b.decode()
L = [1,2,3]
len(L)
L[1]
L[1:3]
L+L
L*2
L=L*3
L[::2]
4 in L
L=[1,2,3]
L[:-1]
s[-100:100]
L.append(4)
del L[0]
L.reverse()
L.sort()
L
t=(1,2,3)
d={'one':'하나','two':'둘'}
d=dict('one':'하나','two':'둘')
d['one']
d['three'] = '셋'
d['one']=1
d.keys()
d.items()
s.center(30)
s.center(30,"*")
s.ljust(30)
s.rjust(30)
phone = '010-1234-5678'
phone.partition('-')
phone.rpartition('-')
phone.split('-')
phone.rsplit('-')
phone.rsplit('-',1)

statement = '''Hellow World!
Python is very powerful.
You must enjoy it.'''
statement
statement.splitlines()

sentence = ''' sdalasdfsafa
sadfsafsafwqerwqlkjrwelqkjrkalsdfkl
sdalfkjkalejfaf'''

sentence

sentence.upper().split()


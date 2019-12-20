fruit='banana'
letter=fruit[1] # 문자열은 0부터 시작
print(letter)

x=3
w=fruit[x-1]
print(w)

print(len(fruit)) # 문자열의 길이를 나타내는 함수

fruit='banana'
index=0
while index < len(fruit) :
    letter=fruit[index]
    print(index, letter)
    index=index + 1


fruit = 'banana'
for letter in fruit :
    print(letter)


word='banana'
count=0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)


s='monty python'
print(s[0:4]) # 0~3까지. 마지막 index는 포함하지 않음

print(s[6:7])

print(s[6:20]) # 문자열 길이에 안맞아도 상관없음

print(s[:2]) # 첫번째나 마지막 인덱스는 생략해도 됨

print(s[8:])
print(s[:])


# string concatenation

a='hello'
b=a+ 'there' # 공백은 더해지지 않음
print(b)

c=a+' '+'there'
print(c)

fruit='banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit :
    print('found it!')


# string comparison

if word == 'banana' :
    print('all right, bananas.')

if word < 'banana' :
    print('your word,' + word + ', comes before banana.')
elif word > 'banana' :
    print('your word,' + word + ', come after banana.')
else :
    print('all right, bananas.')


# string library
greet = 'Hello Bob'
zap = greet.lower() # 소문자로 변환
print(zap)
print(greet) # greet은 바뀌지 않음
print('Hi There'.lower())

stuff = 'Hello world'
type(stuff)

dir(stuff) # 문자열과 관련된 함수 출력


# searching a string
fruit='banana'
pos=fruit.find('na') # 첫번째로 나타나는 na를 찾아서 그 위치를 반환
print(pos)

aa=fruit.find('z') # z는 문자열에 없으므로 -1 반환
print(aa)

# making everything upper case
greet='Hello Bob'
nnn=greet.upper() # 대문자 변환
print(nnn)

www=greet.lower() # 소문자 변환
print(www)


# search and replace
greet='Hello Bob'
nstr=greet.replace('Bob', 'Jane') # Bob을 Jane으로 변경
print(nstr)

nstr=greet.replace('o', 'X') # 문자열에 있는 모든 o을 탐색 후 X로 변환
print(nstr)


# stripping Whitespace
greet='  Hello Bob  '
greet.lstrip() # 왼쪽 공백을 없앰
greet.rstrip() # 오른쪽 공백을 없앰
greet.strip() # 양쪽 공백을 없앰

line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p')


data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos=data.find('@') # @ 기호의 위치 찾기
print(atpos)

sppos=data.find(' ', atpos) # ('찾을 문자열', '탐색을 시작할 위치')
print(sppos)

host=data[atpos+1 : sppos] # 22-31까지
print(host)


# two kinds of strings
# python 3.5.1
x='이광춘'
type(x)
x=u'이광춘'
type(x) # 같은 str로 인식

# python 2.7.10
x='이광춘'
type(x)
x=u'이광춘'
type(x) # unicode로 인식




# ex 6.5
str='X-DSPAM-Confidence:0.8475'
ipos=str.find(':')
piece=str[ipos+1:]
print(piece)

value=float(piece)
print(value)




# open function : 파일을 읽거나 저장하기 전에 open 함수 사용

stuff = 'Hello\nWorld'
stuff
print(stuff)

stuff='X\nY'
print(stuff)
len(stuff)

xfile=open('mbox.txt')
for cheese in xfile :
    print(cheese)


# 텍스트 파일 줄 세기
fhand = open('mbox.txt')
count=0
for line in fhand : # fhand 안의 줄을 각 줄을 지날때마다 세기
    count=count+1
print('Line Count:', count)


fhand=open('C:/Users/sangdon/Desktop/python/mbox-short.txt')
inp=fhand.read()
print(len(inp))

print(inp[:20])

# 접두사 From이 들어간 문자열 찾기
fhand=open('C:/Users/sangdon/Desktop/python/mbox-short.txt')
for line in fhand :
    if line.startswith('From:') :
        print(line)

# 출력된 문장에는 개행 문자가 포함되어있고 print문에 개행문자가 포함되어 있으므로 자동으로 공백인 줄이 생성됨

fhand=open('C:/Users/sangdon/Desktop/python/mbox-short.txt')
for line in fhand :
    line=line.rstrip() # 오른쪽 끝에 공백 지우기
    if line.startswith('From:') :
        print(line)

# skip with continue
fhand=open('C:/Users/sangdon/Desktop/python/mbox-short.txt')
for line in fhand : # fhand에서 차례로 한줄씩 꺼내서 line에 대입
    line=line.rstrip() # 오른쪽 끝에 공백 지우기
    if not line.startswith('From:') :
        continue
    print(line)


fhand=open('C:/Users/sangdon/Desktop/python/mbox-short.txt')
for line in fhand :
    line=line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)


# prompt for file name
fname=input('Enter the file name: ')
fhand=open(fname)
count=0
for line in fhand :
    if line.startswith('Subject:') :
        count=count+1
print('There were', count, 'subject lines in', fname)


# 잘못된 파일명이 들어오는 경우
fname=input('Enter the file name: ')
try :
    ffhand=open(fname)
except :
    print('File cannot be opened', fname)
    quit() # 코드가 더이상 진행되지 않음

count=0
for line in fhand :
    if line.startswith('Subject:') :
        count=count+1
print('There were', count, 'subject lines in', fname)


# ex 7.1
fh=open('C:/Users/sangdon/Desktop/python/mbox-short.txt')

for lx in fh :
    ly=lx.rstrip()
    print(ly.upper())



# list
print([1, 24, 76])
print(['red', 24, 98.6])
print([1, [5, 6,], 7])


for i in [5, 4, 3, 2, 1] :
    print(i)
print('blastoff!')


friends=['joseph', 'glenn', 'sally']
for friend in friends :
    print('happy new year:', friend)
print('done')

print(friends[0])
fruit='Banana'
fruit[0]='b'
x=fruit.lower()
print(x)

lotto=[2, 14, 26, 41, 63]
print(lotto)
lotto[2]=28
print(lotto)

# how long is a list?
greet='Hello Bob'
print(len(greet))
x=[1, 2, 'joe', 99]
print(len(x))

# range function
friends=['joseph', 'glenn', 'sally']

print(list(range(4)))

print(list(range(len(friends))))

friends=['joseph', 'glenn', 'sally']
for friend in friends : # friends를 friend에 하나씩 할당
    print('Happy New Year:', friend)

for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:', friend)


# concatenating lists using +
a=[1, 2, 3]
b=[4, 5, 6]
c=a+b
c
a

lists can be sliced using
t=[9, 41, 12, 3, 74, 15]
t[1:3] # 마지막 숫자에 해당하는 열은 포함 x
t[:4]
t[3:]
t[:]


stuff=list()
stuff.append('book') # list에 항목 추가하기
stuff.append(99)
print(stuff)

stuff.append('cookie')
stuff

# Is something in a list?
some=[1, 9, 21, 10, 16]
9 in some
15 in some
20 not in some

# list are in order
friends=['joseph', 'glenn', 'sally']
friends.sort()
print(friends)

# 내장되어있는 함수와 리스트
nums=[3, 41, 12, 9 ,74, 15]
print(len(nums))
max(nums)
min(nums)
sum(nums)


# best friends : strings and lists
abc='with three words'
stuff=abc.split() # 공백을 기준으로 문자열을 나눔
stuff
len(stuff)
stuff[0]

stuff
for w in stuff :
    print(w)

line='A lot      of spaces' # 공백이 여러개여도 하나로 취급
etc=line.split()
etc

line='first;second;third'
thing=line.split()
thing

thing=line.split(';')
thing


# ex 8
# 메일박스 자료를 불러들이고, From으로 시작하는 줄을 찾아서 세번째 줄 출력
han=open('C:/Users/sangdon/Desktop/python/mbox-short.txt')
for line in han :
    line=line.rstrip()
    # print('Line:', line)
    wds=line.split()
    # print('words:', wds)
    if len(wds) <1 :
        continue
    if wds[0] != 'From' :
        continue
    print(wds[2])


for line in han :
    line=line.rstrip()
    wds=line.split()
    if len(wds) <3 or wds[0] != 'From' : # or의 앞부분이 참이라면 뒷부분은 평가하지 않음
        continue
    print(wds[2])


# dictionaries
purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
print(purse)
purse['candy']

purse['candy']=purse['candy']+2
purse

# 리스트와 딕셔너리의 차이
# 리스트는 위치를 부여
lst=list()
lst.append(21) # 인덱싱이 위치를 부여
lst.append(183)
print(lst)
lst[0]=23
lst

ddd=dict()
ddd['age']=21 # 인덱싱에 명칭을 부여
ddd['course']=182
ddd
ddd['age']=23
ddd

# 딕셔너리 문법
jjj={'chunk' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)
ooo={}




# 점프 투 파이썬 연습문제
# 1. 평균점수
hong={'국어' : 80, '영어' : 75, '수학' : 55}
average=(hong['국어']+hong['영어']+hong['수학'])/len(hong)
average

# 2. 자연수 13이 홀수인지 짝수인지 판별하기


# 3. 홍길동의 주민번호는 881120-1068234이다. 홍길동의 주민번호를 연월일 부분과 그 뒷부분으로 나누어 출력해보자
hong='881120-1068234'
hong.split('-')

# 4. 주민번호 뒷자리의 맨 첫번째 숫자는 성별을 나타낸다. 주민번호에서 성별을 나타내는 숫자를 출력해보자.
pin=hong.split('-')
type(pin)
pin[1][0]

# 5. 다음과 같은 문자열 a:b:c:d가 있다. a#b#c#d로 바꿔서 출력해보자.
a='a:b:c:d'
a.replace('a:b:c:d', 'a#b#c#d')

# 6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어보자.
ls=[1, 3, 5, 4, 2]
ls.sort(reverse=True)
ls

# 7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
ls=['Life', 'is', 'too', 'short']
lssum=ls[0] +" "+ ls[1] + " "+ ls[2] + " " +  ls[3]
lssum



# 연습문제
# Q1
score={'국어':80, '영어':75, '수학':55}
score.values()
mean=sum(score.values())/3
mean


# Q2

i=0
even=list()
while i<1000 :
    even.append(i*2)
    i=i+1
even

num=13
if num in even :
    print('짝수')
else :
    print('홀수')


# Q3
pin="881120-1068234"
yyyymmdd=pin.split('-')[0]
num=pin.split('-')[1]
yyyymmdd
num


# Q4
num[0]


# Q5
a='a:b:c:d'
b=a.replace(':', '#')
b


# Q6
a=[1, 3, 5, 4, 2]
a.sort()
a
a.reverse()
a


# Q7
a=['Life', 'is', 'too', 'short']
result=' '.join(a)
result


# Q8
a=(1,2,3)
b=(4,)
a+b


# Q9
a=dict()
a['name']='python'
a[('a,')]='python'
a[[1]]='python' # list는 key 자리에 올 수 없음
a[250]='python'


# Q10
a={'A':90, 'B':80, 'C':70}
result=a['B']
result


# Q11
a=[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet=set(a)
aSet

b=list(aSet)
b


# Q12
a=b=[1,2,3] # 같은 주소값에 저장되므로 같이 바뀜
a[1]=4
b
a=[1,2,3]
b=a[:]

a[1]=4
b





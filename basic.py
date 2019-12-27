# 모두를 위한 파이썬 : 파이썬


Hours=input('Enter your working time: ')
Rate=input('Enter your rate: ')
Pay=float(Rate)*float(Hours)
print("Pay: ", Pay)

# conditionals
# one-way decision
x=5
print('Before 5')
if x==5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')

x=5
if x>2 :
    print('Bigger than 2')
print('Done with 2')

for i in range(5) :
    print(i)
    if i>2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

x=42
if x>1 :
    print('More than one')
    if x<100 :
        print('Less than 100')
print('All done')


# two way decision
x=4
if x>2 :
    print('Bigger')
else :
    print('Smaller')


x=0
if x<2 :
    print('Small')
elif x<10 : # 두번째 질문은 첫번째 질문이 나올 때까지 확인하지 않음
    print('Large')
print('All done')


# elif가 여러개 있을 수도 있음
x=120
if x<2 :
    print('small')
elif x<10 :
    print('medium')
elif x<20 :
    print('big')
elif x<40 :
    print('large')
elif x<100 :
    print('huge')
else :
    print('ginormous') # 거대한


if x<2 :
    print('below 2')
elif x>=2 :
    print('two or more')
else :
    print('something else') # x값에 상관없이 실행되지 않는 코드임

x=1
if x<2 :
    print('below 2') # 참일 경우 출력하고 밑에 코드는 반영 x
elif x<20 :
    print('below 20')
elif x<10 :
    print('below 10')
else :
    print('something else')

money = True
if money:
    print('택시를 타고 가라')
else:
    print('걸어가라')

pocket = ['[paper', 'money', 'cellphone']
if 'money' in pocket:
    pass  # 조건문이 아무 일도 하지 않게 설정하고 싶을 때
else:
    print('카드를 꺼내라')

pocket = ['money', 'card']
if 'money' in pocket:
    print('택시를 타고')
elif 'card' in pocket:
    print('택시를 타고')
else:
    print('걸어가라')



# 에러로 인한 프로그램 중단 대비
# try/except

astr='Hello Bob'
try :
    istr=int(astr) # error code
except :
    istr=-1 # try에서 error가 발생할 경우 실행
print('First', istr)

astr='123'
try :
    istr=int(astr) # true code
except :
    istr=-1 # try에서 error가 발생하지 않았으므로 except 생략
print('second', istr)


astr='bob'
try :
    print('hello') # true code 실행
    istr=int(astr) # error code 생략
    print('there') # error code 생략
except :
    istr=-1 # error code 대신 출력
print('Done', istr)


rawstr=input('Enter a number: ')
try :
    ival=int(rawstr)
except :
    ival=-1

if ival > 0 :
    print('Nice work')
else :
    print('Not a number')


# ifelse 실습

sh=input('Enter the Hours: ')
sr=input('Enter the Rate: ')
fh=float(sh) # 소수점이 있는 숫자
fr=float(sr)

if fh>40 :
    print('overtime')
else :
    print('regular')
xp=fh*fr
print('pay', xp)


sh=input('Enter the Hours: ')
sr=input('Enter the Rate: ')
fh=float(sh) # 소수점이 있는 숫자
fr=float(sr)

if fh>40 :
    reg=fr*fh
    otp=(fh-40.0)*(fr*0.5)
    xp=reg+otp
else :
    xp=fh*fr
print('Pay:', xp)


# ex 3.2

sh=input('Enter the Hours: ')
sr=input('Enter the Rate: ')

try :
    fh=float(sh)
    fr=float(sr)
except :
    print('Error, please enter numeric input')
    #quit() # 밑에 코드가 있더라도 더이상 진행 안됨.




# function

def thing() :
    print('hello')
    print('fun')

thing()

big=max('hello world') # 알파벳 중에 가장 나중에 오는 문자
print(big)

print(float(99)/100)
i=42
type(i)
f=float(i)
print(f)

type(f)
print(1+2*float(3)/4-5)



# parameters

def greet(lang) :
    if lang =='es' :
        print('hola')
    elif lang =='fr' :
        print('bonjour')
    else :
        print('hello')

greet('es')
greet('en')
greet('fr')


# return statement

def greet() :
    return 'hello' # 다음 줄로 진행하지 않고 값을 반환. 함수가 끝났을 때 나타날 값

greet()
print(greet(), 'glenn')
print(greet(), 'sally')


# multiple parameters /arguments

def addtwo(a, b) :
    added=a+b
    return added

x=addtwo(3, 5)
print(x)


# ex 3.6
def computepay(hours, rate) :
    # print('in computepay', hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    # print('returning', pay) # 디버깅용 출력문
    return pay

sh=input('Enter the Hours: ')
sr=input('Enter the Rate: ')
fh=float(sh)
fr=float(sr)


xp=computepay(fr, fh) # 반환한 pay값을 xp에 할당
print('pay:', xp)


# 입력값이 없는 함수
def say() :
    return 'Hi'
say()


# 결과값이 없는 함수
def add(a, b) :
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3,4)
a=add(3,4)

print(a)


# 입력값도 결과값도 없는 함수
def say() :
    print('Hi')
say()


def add_many(*args) :
    result=0
    for i in args :
        result=result + i
    return result

add_many(1,2,3,4)


def add_mul(choice, *args) :
    if choice == "add" :
        result=0
        for i in args :
            result=result+i
    elif choice == "mul" :
        result=1
        for i in args :
            result = result*i
    return result

add_mul('add', 1,2,3,4,5)


# 키워드 파라미터
def print_kwangs(**kwangs) :
    print(kwangs)


print_kwangs(a=1, name='foo')





# while loof

n=5
while n>0 :
    print(n)
    n=n-1
print('blastoff!')
print(n)


while True :
    line=input('> ')
    if line == 'done' :
        break # if가 참일 경우 if 구문에서 빠져나와서 Done! 출력
    print('line')
print('Done!')


while True :
    line=input('> ')
    if line[0]=='#' :
        continue # 더 이상 진행하지 않고, 다시 While 구문으로 이동
    if line=='done' :
        break
    print(line)
print('Done!')


prompt="""
1. Add
2. Del
3. List
4. Quit

Enter number: 
"""

print(prompt)

number=0
while number!=4 :
    print(prompt)
    number=int(input())

# while 문을 강제로 나가고 싶을 때
coffee=10
money=300
while money : # money가 0이 아닌 이상 계속 돌아감
    print('돈을 받았으니 커피를 줍니다')
    coffee=coffee-1
    print('남은 커피의 양은 %d개입니다' %coffee)
    if coffee==0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다')
        break


# while문의 맨 처음으로 돌아가기

a=0
while a<10 :
    a=a+1
    if a % 2==0 : continue # a를 2로 나누었을 때 나머지가 0인 경우
    print(a)


# 무한루프일 경우 Ctrl+c로 빠져나감

while True :
    print('cccc')




# for loop

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

friends=['joseph', 'glenn', 'sally']
for friend in friends :
    print('happy new year: ', friend)
print('Done!')


print('before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('after')

# how to find the largest value

large_so_far=-1
print('before', large_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num>large_so_far :
        large_so_far=the_num # 조건이 참일 경우 변수를 새로 할당, 아닐 경우 skip
    print(large_so_far, the_num)
print('after', large_so_far)

# if 구문 참고
x=5
if x>2 :
    print('Bigger than 2') # 조건이 참일 경우 출력, 아닐 경우 skip
print('Done with 2')


# counting in a loop

zork=0
print('before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork=zork+1
    # print(zork, thing)
print('after', zork)

# summing in a loop

zork=0
print('before', zork)
for thing in [9, 31, 12, 3, 74, 15] :
    zork=zork+thing
    # print(zork, thing)
print('after', zork)


# finding the average in a loop

count=0
sum=0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count=count+1
    sum=sum+value
    # print(count, sum, value)
print('after', count, sum, sum/count)


# filtering in a loop
print('before')
for value in [9, 41, 12, 3, 74, 15] :
    if value>20 :
        print('large number', value)
print('after')


# searching using a boolean variable : 특정한 값이 존재하는지 탐색할 때
# boolean variable == logical variable
found=False
print('before', found)
for value in [9, 31, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    # print(found, value)
print('after', found)


# how to find the smallest value

small_so_far=1000
print('before', small_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < small_so_far :
        small_so_far=the_num
print('after', small_so_far)

# 초기값 설정을 어떻게 해야 할까?
# None = 'None'만 갖는 상수. 공백을 의미할 때 사용

smallest=None
print('before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None : # is 는 == 연산자보다 강력함
        smallest = value
    elif value < smallest :
        smallest=value
    # print(smallest, value)
print('after', smallest)


# the 'is' and 'is not' operator
# 'is' 연산자는 '==' 연산자보다 강력함
# 'is'는 변수의 자료형과 값이 모두 같아야함
# boolean, None 타입 자료형에만 사용하는 것이 바람직함


add=0
for i in range(1, 11) :
    add=add+i
print(add)

for i in range(2, 10) :
    for j in range(1, 10) :
        print(i*j, end='') # end=' ' : 한줄씩 출력
    print(' ') # 줄 간격


# ex 5.1

num=0
tot=0.0
while True :
    sval=input('Enter a number: ')
    if sval == 'done' :
        break
    try :
        fval=float(sval)
    except :
        print('Invalid input')
        continue
    # print(fval)
    num=num+1
    tot=tot+fval

# print('All done')
print(tot, num, tot/num)


# Q1
a='Life is too short, you need python'

if 'wife' in a :
    print('wife')
elif 'python' in a and 'you' not in a :
    print('python')
elif 'shirt' not in a :
    print('shirt')
elif 'need' in a :
    print('need')
else :
    print('none')


# Q2
result=0
i=1
while i <=1000 :
    if i%3==0 :
        result+=i
        i+=i
print(result)


# Q3
i=0
while True :
    i+=1
    if i>5 : break
    print('*'*i)


# Q4
for i in range(1, 101) :
    print(i)


# Q5
A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total=0
for score in A :
    total+=score
    average=total/len(A)
print(average)


# Q6
numbers=[1, 2, 3, 4, 5]
result=[number*2 if number%2 !=0]
print(result)




# 파일 읽고 쓰기
f=open("새파일.txt", 'w')
for i in range(1, 11) :
    data="%d번째 줄입니다.\n" % i
    f.write(data) # 한글 깨짐
f.close()


# 현재 디렉토리
import os
print(os.getcwd())


# 파일 읽는 방법
f=open('새파일.txt', 'r')
line=f.readline()
print(line) # 첫번째 줄 출력

f=open('새파일.txt', 'r')
while True :
    line=f.readline()
    if not line : break
    print(line)
f.close()

f=open('새파일.txt', 'r')
lines=f.readlines()
for line in lines :
    print(line)
f.close()

f=open('새파일.txt', 'r')
data=f.read()
print(data)


# 원래 있던 파일에 새로운 내용을 추가할 경우
f=open('새파일.txt', 'a')
for i in range(11, 20) :
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()


# Q1
def is_odd(number) :
    if number % 2 != 0 :
        return True
    else :
        return False

is_odd(3)

# Q2
def avg_numbers(*args) :
    result=0
    for i in args :
        result+=i
    return print(result/len(args))

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)

# Q3
input1=input("첫번째 숫자를 입력하세요:") # input은 무조건 문자열로 변환
input2=input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)


# Q4
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

f1=open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2=open("test.txt", 'r')
line=f2.readline()
print(line)
f2.close()

# Q6
user_input=input("저장할 내용을 입력하세요:")
f=open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()


# Q7
f=open('test.txt', 'r')
body=f.read()
print(body)
f.close()

body = body.replace("java", "python")

f=open('test.txt', 'w')
f.write(body)
f.close()


# class
result1=0
result2=0

def add1(num) :
    global result1
    result1+=num
    return result1

def add2(num) :
    global result2
    result2+=num
    return result2

print(add1(3))
print(add1(4))

class Calculator:
    def __init__(self):
        self.result=0

    def add(self, num):
        self.result+=num
        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))


class FourCal :
    def setdata(self, first, second):
        self.first=first
        self.second=second

    def add(self):
        result=self.first + self.second
        return result

    def mul(self):
        result=self.first * self.second
        return result

    def sub(self):
        result=self.first - self.second
        return result

    def div(self):
        result=self.first / self.second
        return result

a=FourCal()
b=FourCal()

a.setdata(4,2)
b.setdata(3,8)

a.add()
b.add()



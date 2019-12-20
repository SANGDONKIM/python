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




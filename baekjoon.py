# Q1
print('Hello world')

# Q2
print('''강한친구 대한육군
강한친구 대한육군''')

# Q3
print("%-5s/\\" % "\\")
print(" " + ")" + " "*2 +"(" + " " + "'" + ")")
print("(" + " "*2 + "/" + " "*2 + ")")
print(" " + "\\" + "(__)" + "|")


# Q4
print("|\\_/|")
print("|q" + " " + "p|"+ " "*3 + "/}")
print("(" + " " + "0" + " " + ")" + '"""' + "\\")
print("|" + '"^"' + "`" + " "*4 + "|")
print("||_/=\\\\__|")


# Q5

A,B= map(int, input().split())
print(A+B)

# Q6
A,B= map(int, input().split())
print(A-B)

# Q7
A,B= map(int, input().split())
print(A*B)

# Q8
A,B= map(int, input().split())
pvalue=float(A/B)

rvalue=float("{0:0.9f}".format(pvalue))
print(rvalue)


# Q9
A,B= map(int, input().split())
print(A+B, A-B, A*B, int(A/B), A%B, sep="\n")


# Q10
A,B,C= map(int, input().split())
print((A+B)%C, (A%C+B%C)%C, (A*B)%C, (A%C*B%C)%C, sep="\n")


# 2588
A=int(input())
B=int(input())
print(A*(B%10), A*((B%100)//10), A*(B//100), A*B, sep='\n')


# Q12
A,B=input().split()
A=int(A)
B=int(B)

if A>B :
    print('>')
elif A<B :
    print('<')
else :
    print('==')


# Q13
score=input()
score=int(score)

if score >=90 :
    print('A')
elif score >=80 :
    print('B')
elif score >=70 :
    print('C')
elif score >=60 :
    print('D')
else :
    print('F')


# Q14
year=input()
year=int(year)

if year%4==0 and year%100!=0 or year%400==0 :
    print(1)
else :
    print(0)

# 2884

H,M=input().split()
H=int(H)
M=int(M)-45

if M<0 and H==0: # 0:15 --> 23:30
    print(H+23, M+60)
elif M<0 and H>0: # 1:15 ---> 0:30
    print(H-1, M+60)
elif M>0 and H>0 : # 1:46 ---> 1:1
    print(H, M)


# 10817
A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)

if A>=B>=C :
    print(B)
elif A>=C>=B :
    print(C)
elif B>=A>=C :
    print(A)
elif B>=C>=A :
    print(C)
elif C>=B>=A :
    print(B)
elif C>=A>=B :
    print(A)



# for

# 2739
N=input()
N=int(N)
for M in range(1, 10) :
    result=N*M
    print(N,'*',M,'=',result)


# 10950
T=int(input())
for i in range(T) :
    A, B=input().split()
    print(int(A)+int(B))

# 15552
T=sys.stdin.readline()
for i in range(T) :
    A,B=map(int, sys.stdin.readline().split())
    print(A+B) # 실패

# 11021
T=int(sys.stdin.readline())

for i in range(T) :
    A,B=sys.stdin.readline().split()
    number=i+1
    print('Case #%d:'%number, int(A)+int(B))
# 실패

T = int(input())
for i in range(1, T + 1):
    a, b = map(int, input().split())
    print('Case #%d: %d' %(i, a + b))


# 11022
T = int(input())
for i in range(1, T + 1):
    a, b = map(int, input().split())
    print('Case #%d: %d + %d = %d' %(i, a, b, a+b))


# 10871
N,X=map(int, input().split())
k=list(map(int, input().split()))
for i in k:
    if i<X:
        print(i, end=' ')


# 8393
n=int(input())
m=0
for i in range(1,n+1) :
    m=m+i
print(m)


# 2741
N=int(input())
for i in range(1, N+1) :
    print(i)

# 2742
N=int(input())
for i in range(N, 0, -1) :
    print(i)


# 2438
N=int(input())
for i in range(1, N+1) :
    print(i*'*')

# 2439
N=int(input())
for i in range(1, N+1) :
    print(" "*(N-i)+i*'*')




# while

# 10952
repeat=int(input())
i=0
while i <= repeat :
    i=i+1
    A, B = map(int, input().split())
    print(A+B)
    if i== repeat:
        print(0,0) # 런타임 에러

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)


# 10951
repeat=int(input())-1
i=0
while i <= repeat :
    i=i+1
    A, B = map(int, input().split())
    print(A+B) # 런타임 에러

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break




# 1110
N=int(input()) # 26
n=N # 26

result=0
second=0
counter=1
while True :
    second= N%10 # 6
    N=N//10 # 2
    result=second+N # 2+6=8
    N=(second*10)+(result%10) # (6*10)+8=68

    if N==n:
        break
    else:
        counter=counter+1
print(counter)


# 10818
N=int(input())
if not (1<=N<=1000000):
    exit()

A=list(map(int, input().split()))
print(min(A), max(A))

# 2562
MAX=0
INDEX=0
for i in range(9):
    N=int(input())
    if N>MAX:
        MAX=N
        INDEX=i+1
print(MAX, INDEX, end=' ')


# 2920
c,d,e,f,g,a,b,C=1,2,3,4,5,6,7,8
code=list(map(int, input().split()))
acode=sorted(code)
dcode=sorted(code, reverse=True)

if code==acode :
    print('ascending')
elif code==dcode :
    print('descending')
else :
    print('mixed')


# 2577
A,B,C=map(int, input().split())
N=str(A*B*C)
c0,c1,c2,c3,c4,c5,c6,c7,c8,c9=0,0,0,0,0,0,0,0,0,0
for i in range(0,len(N)):
    if N[i] == '0':
        c0+=1
    elif N[i] == '1':
        c1+=1
    elif N[i] == '2':
        c2 += 1
    elif N[i] == '3':
        c3 += 1
    elif N[i] == '4':
        c4 += 1
    elif N[i] == '5':
        c5 += 1
    elif N[i] == '6':
        c6 += 1
    elif N[i] == '7':
        c7 += 1
    elif N[i] == '8':
        c8 += 1
    elif N[i] == '9':
        c9 += 1
print(c0,c1, c2, c3, c4, c5, c6, c7, c8, c9, sep='\n') # 런타임 에러


A,B,C=map(int, input().split())
N=str(A*B*C) # '17037300'
count=list()
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for j in range(0,len(N)):
        if N[j] == 'i': # N[0]='0'이면 count[0]=1, N[1]='0'이면 count[0]=2
            count[i]=i+1
        else :
            count[i]=0
print(count)

import sys
A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
C=int(sys.stdin.readline())

N=list(str(A*B*C))

for i in range(10) :
    print(N.count(str(i)))


# 3052
import sys
N=list()
K=list()
for i in range(0,10):
    N.append(int(sys.stdin.readline()))
    K.append(N[i]%42)
print(len(set(K)))


# 1546

import sys
N=int(sys.stdin.readline())
score=list(map(int, sys.stdin.readline().split()))
newscore=list()
for i in score :
    newscore.append((i/max(score))*100)
print(sum(newscore)/N)

# 8958
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
import sys
N=int(sys.stdin.readline())
result=list()
count=0
for i in range(N):
    result.append(sys.stdin.readline())
# print(result)
    for j in range(80) :
        if result[i][j]=='O' :
            count=count+1
        elif result[i][j]=='X':
            count=count+0
print(count)


# 4344
import sys
C=int(sys.stdin.readline())

upp=0
for i in range(C) :
    score=list()
    score=list(map(int, sys.stdin.readline().split()))
# print(score)
    mean=sum(score)/score[0]
    for j in range(len(score)):
        if score[j]>mean:
            upp+=1
    rate=upp/score[0]
print(rate) # 오류

# chr

# 11654
c=str(input())
print(ord(c))

# 11720
import sys
N=int(sys.stdin.readline())
result=sys.stdin.readline()
out=0
for i in range(N):
    out+=int(result[i])
print(out)

# 10809
import sys
s=sys.stdin.readline()
from string import ascii_lowercase
alpha=list(ascii_lowercase)

newalpha=list()
for i in alpha:
    if i in s : #'baekjoon' 안에 'a'가 있다면
        index=s.find(i) # 'baekjoon'에서 'a'의 위치
        newalpha.append(index)
    elif i not in s :
        newalpha.append(-1)
# print(newalpha) 리스트로 출력하면 안됨.
for j in range(len(newalpha)):
    print(newalpha[j], end=' ')


# 2675
import sys
T=int(sys.stdin.readline())

result=str()
for i in range(T) :
    A,B=sys.stdin.readline().split()
    A=int(A)
    for j in range(len(B)):
        result+=B[j]*A
print(result) # 각각 나와야됨

import sys
T=int(sys.stdin.readline()) # 2

for i in range(T) : # i에 0,1 대입, 두번 반복
    A,B=sys.stdin.readline().split() # 3 ABC, 5 /HTP
    A=int(A) # 3
    result = str()
    for j in range(len(B)): # j에 0,1,2 대입, 0,1,2,3 대입
        result+=str(B[j]*A) # AAABBBCCC+/////HHHHHTTTTTPPPPP
    print(result)






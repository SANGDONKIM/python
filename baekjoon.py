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
# 1110
N='26'
K=str(int(N[0])+int(N[-1]))
N[-1]+K[-1]

N='68'
K=str(int(N[0])+int(N[-1]))
N[-1]+K[-1]

N='84'
K=str(int(N[0])+int(N[-1]))
N[-1]+K[-1]

N='42'
K=str(int(N[0])+int(N[-1]))
N[-1]+K[-1] # 26

N=input()
while N!=new :
    K = str(int(N[0]) + int(N[-1]))
    N=N[-1] + K[-1]














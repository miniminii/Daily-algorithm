#1020 - 부호 대신 공백으로 이어붙여주기
a,b = input().split('-')
print(a,b, sep='')

#1021
s = input()
for i in s :
    print(i)

#1022
s = input()
print(s[0:2], s[2:4], s[4:])

#1023
h,m,s = input().split(':')
print(m)

#1024
w1, w2 = input.split()
print(w1 + w2)

#1025
a,b = map(int, input().split())
print(a+b)

#1026
f1 = float(input())
f2 = float(input())
print(f1 + f2)

#1027 - 10진수를 16진수로
n = int(input())
print('%x' % n)

#1028 - 10진수를 16진수로
n = int(input())
print('%X' % n)

#1029 - 16진수를 8진수로
n = int(input(), 16)
print('%o' % n)

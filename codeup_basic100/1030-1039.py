#1030 - 영문자를 10진수 유니코드값으로
n = ord(input())
print(n)

#1031 - 10진 정수를 유니코드 문자로
c = int(input())
print(chr(c))

#1032 - 양수를 음수로
n = int(input())
print(-n)

#1033 
n = ord(input())
print(chr(n+1))

#1034
a,b = map(int, input().split())
print(a - b)

#1035
a,b = map(int, input().split())
print(a*b)

#1036
word,n = input().split()
print(word * int(n))

#1037
n = int(input())
str = input()
print(str * n)

#1038 - 정수 거듭제곱 
a,b = map(int, input().split())
print(a ** b)

#1039 - 실수 거듭제곱
a,b = map(float, input().split())
print(a ** b)

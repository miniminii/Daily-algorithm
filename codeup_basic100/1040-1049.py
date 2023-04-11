#1040 - 나눈 몫 //
a,b = map(int, input().split())
print(a//b)

#1041 - 나눈 나머지 %
a,b = map(input().split())
print(a % b)

#1042 - 반올림하기
a = float(input())
print(format(a,".2f"))

#1043
a,b = map(float, input().split())
print(format(a/b, ".3f"))

#1044
a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a * b)
print(a // b)
print(a % b)
print("{:.2f}".format(a/b))

#1045
a,b,c = map(int, input().split())
print(a + b + c, "{:.2f}".format((a+b+c)/3))

#1046 - 비트시프트
n = int(input())
print(n << 1)

#1047
a,b = map(int, input().split())
print(a << b)

#1048
a, b = map(int, input().split())
print(bool(a < b))

#1049
a,b = map(int, input().split())
print(bool(a==b))

#1050
a,b = map(int, input().split())
print(bool(a <= b))

#1051
a, b = map(int, input().split())
print(bool(a != b))

#1052
n = int(input())
print(bool(n))

#1053 - 1이 false, 0이 true가 나오게
a = bool(int(input()))
print(not a)

#1054 - 둘다 true일 경우에만 true
a, b = map(int, input().split())
print(bool(a) and bool(b))

#1055 - 둘 중 하나가 true이면 true
a, b = map(int, input().split())
print(bool(a) or bool(b))

#1056 - 두값이 다를 경우에만 true
a, b = map(int, input().split())
c, d = bool(a), bool(b)
print((c and (not d)) or ((not c) and d))

#1057 - 두값이 같은 경우에만 true
a,b = map(int, input().split())
print(bool(a) == bool(b))

#1058 - 두 값 모두 False 일때 True
a, b = map(int, input().split())
c, d = bool(a), bool(b)
print(not c and not b)

#1059
a = int(input())
print(~a)

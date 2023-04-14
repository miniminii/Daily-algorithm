#1060
a,b = map(int, input().split())
print(a & b)

#1061
a, b = map(int, input().split())
print(a | b)

#1062
a, b = map(int, input().split())
print(a ^ b)

#1063
a, b = map(int, input().split())
print(a if (a>=b) else b)

#1064
a, b, c = map(int, input().split())
print(min(a, b, c))

#1065
s = map(int, input().split)
for i in s :
    if i % 2 == 0:
        print(i)

#1066
s = map(int, input().split())
for i in s :
    if i % 2 == 0 :
        print('even')
    else :
        print('odd')

#1067
s = map(int, input().split())
for i in s:
    if i % 2 == 0:
        if i < 0:
            print('A')
        else:
            print('C')
    else:
        if i < 0:
            print('B')
        else:
            print('D')

#1068
n = int(input())

if n >= 90:
    print('a')
elif n >= 70 :
    print('b')
elif n >= 40 :
    print('c')
else :
    print('d')

#1069
n = input()

if n == 'A':
    print("best!!!")
elif n == 'B':
    print("good!!")
elif n == 'C':
    print("run!")
elif n == 'D':
    print("slowly~")
else:
    print("what?")

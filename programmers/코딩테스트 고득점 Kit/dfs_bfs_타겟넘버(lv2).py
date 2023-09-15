def solution(numbers, target):
    temp = [0]              
    count = 0 
    for num in numbers : 
        temp2 = []
        for i in temp :
            temp2.append(i + num)    # 더하는 경우 
            temp2.append(i - num)    # 빼는 경우 
        temp = temp2
    
    return temp.count(target)

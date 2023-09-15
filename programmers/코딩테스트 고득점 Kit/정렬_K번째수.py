def solution(array, commands):
    answer = []
    for lst in commands :
        i = lst[0]
        j = lst[1]
        k = lst[2]
        temp = sorted(array[i-1: j])[k-1:k]
        answer.append(temp)
        
    word= []
    for i in answer :
        for j in i :
            word.append(j)
    
    return word

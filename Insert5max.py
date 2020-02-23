# Codility test
def solution(N):
    # write your code in Python 3.6
    if N >= 0:
        str1 = str(N)
        for n in str1:
            if int(n) < 5:
                index1 = str1.index(n)
                if index1==0:
                    str2 = '5'+str1
                    break
                else:
                    str2 = str1[:index1]+'5'+str1[index1:]
                    break
            else:  
                str2 = str1+'5'
        return str2
        
    if N < 0:
        str1 = str(abs(N))   
        for n in str1:
            if int(n) > 5:
                index1 = str1.index(n)
                if index1==0:
                   str2 = '5'+str1
                   break
                else:
                   str2 = str1[:index1]+'5'+str1[index1:]
                   break
            else: 
                str2 = str1+'5'
        return "-"+str2

print(solution(268))
print(solution(670))
print(solution(0))
print(solution(-999))

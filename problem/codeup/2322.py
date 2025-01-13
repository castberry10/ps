a, b = input().split()
answer = set() # set 혈액형 중복 방지
answer2 = set()
dicti = {'AA':'A', 'AO':'A', 'BB' : 'B', 'BO': 'B', 'AB': 'AB', 'OO': 'O'} # 맵핑
# 혈액형 조합 
for i in range(2):
    for j in range(2):
        temp = []
        temp.append(a[i])
        temp.append(b[j])
        temp.sort() # 혈액형 인자 모음
        strtemp = ''
        strtemp += temp[0] + temp[1]
        answer.add(strtemp)
        
for i in answer:
    answer2.add(dicti[i])
answer2 = list(answer2)
answer2.sort()
print(*answer2)
        
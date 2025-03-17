a, b = input().split()
answer = set() # set 혈액형 중복 방지 # AA
answer2 = set() # BB
dicti = {'AA':'A', 'AO':'A', 'BB' : 'B', 'BO': 'B', 'AB': 'AB', 'OO': 'O'} # 맵핑
# 혈액형 조합 
for i in range(2):
    for j in range(2):
        temp = []
        temp.append(a[i])
        temp.append(b[j])
        # temp = [A, B] [A, A]
        temp.sort() # 혈액형 인자 모음
        strtemp = ''
        strtemp += temp[0] + temp[1]
        # strtemp 'AB'  'AA'
        answer.add(strtemp)
        
for i in answer:
    answer2.add(dicti[i])
answer2 = list(answer2)
answer2.sort()
print(*answer2)
        
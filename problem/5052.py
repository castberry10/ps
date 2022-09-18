#트라이 자료구조
#node trie 구현 사용
import sys 

class Node:
    def __init__(self):
        self.state = False 
        self.childs = dict()
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, num):
        point = self.root
        for i in num:
            if i not in point.childs:
                point.childs[i] = Node()
            point = point.childs[i] #key로 value(Node()) 가져오기 
            if point.state == True:
            # if point.state is True:
                return False
        point.state = True
        return True
        
t = int(input())
datals = []
for i in range(t):#test case 개수만큼 반복 
    ck = True #체크 
    N = int(input()) # 한 테스트케이스동안 입력받는 전화번호수 만큼 
    for j in range(N):# 반복
        # datals += sys.stdin.readline().rstrip()
        datals.append(sys.stdin.readline().rstrip())
        
    # datals.sort(key = lambda x : len(x))
    datals.sort(key = len) # 길이로 정렬
    # datals.sort()
    trie = Trie() #새 트라이 생성  
    print('datals', datals)
    for i in datals:# 짧은 전화 번호부터 반복 
    	print('전화번호 i', i)
        ck = trie.insert(i)
        print('체크' , i)
        if ck == False: # 집어놓는 도중 트라이 state가 True였다면 나감
            break
    if ck: # 괜찮으면 yes 
        print('YES')
    else:# 안괜찮으면 no 
        print('NO')
    # print(datals)
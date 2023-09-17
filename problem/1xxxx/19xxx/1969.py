import sys
data = list()
# 첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다. N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.
input = sys.stdin.readline
n , m = map(int, input().split())

for _ in range(n):
    data.append(input().rstrip())

answer = ""


answerInt = 0
for i in range(m):
    tempdic = {'A':0,'C':0,'G':0,'T':0 } 
    for j in range(n):
        tempdic[data[j][i]] += 1
    
    maxDNA = max(tempdic, key=tempdic.get)
    
    for j in range(n):
        if maxDNA != data[j][i]:
            answerInt += 1 
    answer += maxDNA
    
print(answer)
print(answerInt)
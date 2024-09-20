s, p = map(int, input().split())
dna = input()
minA, minC, minG, minT = map(int, input().split())
start = 0
end = p - 1 
answer = 0
dict = {'A' : 0, 'C' : 0, 'G' : 0, 'T': 0}

for i in dna[start:end+1]:
    dict[i] += 1

# 혹은 while end < s?
for i in range(s - p + 1):
    if dict['A'] >= minA and dict['C'] >= minC and dict['G'] >= minG and dict['T'] >= minT:
        answer += 1
    if i != s - p: # 반복문의 마지막이 아니라면
        dict[dna[start + i]] -= 1
        dict[dna[end + 1 + i]] += 1
    
print(answer)
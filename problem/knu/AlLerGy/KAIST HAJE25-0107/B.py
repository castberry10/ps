import sys
input = sys.stdin.readline
n, s, k = map(float, input().split())
n, k = int(n), int(k)
answer = 0
data = {}
dataset = []
dataset.append(1)
data[1] = s
for i in range(k):
    mi, si = input().split()
    mi = int(mi)
    si = float(si)
    data[mi] = si
    dataset.append(mi)
dataset.append(n + 1)

# 만약 60bpm이면 1분에 60박자 
# 1마디가 4박자임
# 즉 60bpm이 오면 60bpm / 4- 15를 하면 1분의 15박자 
# print(data)
for i in range(len(dataset) - 1):
    s = data[dataset[i]]
    time = dataset[i+ 1] - dataset[i]
    bpm4 = s / 4
    nsto4bit = 60 / bpm4
    answer += float(time * nsto4bit)
    # print(time, float(time * nsto4bit))
       
print(f'{answer:.12f}')
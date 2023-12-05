n = int(input())
tof = False
answer = 1
dataset = set(['ChongChong'])
for _ in range(n):
    a, b = input().split()
    if a == 'ChongChong' or b == 'ChongChong':
        tof = True
    if tof:
        if a in dataset and b not in dataset:
            dataset.add(b)
        if b in dataset and a not in dataset:
            dataset.add(a)
        
if tof:
    print(len(dataset))
else:
    print(-1)
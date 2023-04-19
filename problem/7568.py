n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    
    data.append((x, y))
    
for x1, y1 in data:
    answer = 1 
    
    for x2, y2 in data:
        if x1 < x2 and y1 < y2:
            answer += 1 

    print(answer, end = ' ')
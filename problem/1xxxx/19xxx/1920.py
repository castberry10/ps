N = int(input())
data = list(map(int, input().split()))

n = int(input())

data.sort()

# 있다면 1 없다면 0 

def binSer(i):
    global N
    start = 0
    end = N - 1 
    point = end // 2
    while True:
        point = (start + end) // 2 
        if start == end:
            if data[end] == i:
                return 1
            else:
                return 0
        if start > end:
            return 0
        
        if data[point] == i:
            start = end = point
        elif data[point] > i:
            end = point - 1 
            
        else:
            start = point + 1
        
testdata = list(map(int, input().split()))

for i in testdata:
    print(binSer(i))
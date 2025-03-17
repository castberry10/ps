data = list()
scorelist = [10, 8,6,5,4,3,2,1,0] # 0 - 9 index 
R, B = 0, 0
for _ in range(8):
    su, t = input().split()
    su = list(su.split(":"))
    su = int(su[0]) * 100000 + int(su[1]) * 1000 + int(su[2])
    data.append([su, t])
data.sort( key=lambda x : x[0])

for i in range(8):
    if data[i][1] == "B":
        B += scorelist[i]
    else:
        R += scorelist[i]
    
if R > B:
    print("Red")
else:
    print("Blue")
    
# print(R, B)
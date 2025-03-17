text = input()

ak = "KOREA"
ay = "YONSEI"

k = ""
y = ""

for i in range(len(text)):
    if ak[len(k)] == text[i]:
        k += text[i]
    if ay[len(y)] == text[i]:
        y += text[i]
    
    
    
    if k == ak:
        print(ak)
        break
    elif y == ay:
        print(ay)
        break
    
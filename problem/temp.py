a, b = map(int, input().split())

def print280():
    print(280)

def print320():
    print(320)

if a < 12:
    print280()
    
elif a < 17:
    if b == 1:
        print280()
    else:
        print320()
else:
    print280()
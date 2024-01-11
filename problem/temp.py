import sys
vowel = {'a','e','i','o','u'}
input = sys.stdin.readline

while True:
    data = input()
    data.rstrip()
    print('data:', data)
    if data == 'end':
        break
    data1 = data[::]
    data = list(data1)
    flag = 0 
    vowelCnt = 0 
    consonantCnt = 0  
    tof = 0  
    for i in range(len(data)):
        if i >= 1:
            if data[i] == data[i - 1]:
                if data[i] != 'e' and data[i] != 'o':
                    tof = 1
                    break
        if data[i] in vowel:
            flag = 1
            consonantCnt = 0
            vowelCnt += 1
            if vowelCnt == 3:
                tof = 1
                break
        else:
            vowelCnt = 0
            consonantCnt += 1
            if consonantCnt == 3:
                tof = 1
                break
	
    if tof != 1 and vowelCnt == 1:
        print("<"+ data1 +"> is acceptable.")
    else:
        print("<" + data1 + "> is not acceptable.")
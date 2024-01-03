# 병합정렬

def marge(start, end, mid):
    global answer 
    ### 병합 부분 ### 
    for i in range(start, end + 1):
        temp[i] = datalist[i]
    
    k = start
    index1 = start # 그룹 1
    index2 = mid + 1 # 그룹 2
    
    while index1 <= mid and index2 <= end: # index1, 2가 자신 그룹에 속해있을때
        if temp[index1] > temp[index2]: # 2번그룹(뒤 그룹)이 더 크면  
            datalist[k] = temp[index2]
            answer += index2 - k
            k += 1
            index2 += 1
        else:
            datalist[k] = temp[index1]
            k += 1
            index1 += 1
    # 위 반복문에서 한쪽 그룹은 완전히 정리될텐데,
    # 남은 나머지 그룹정리
    while index1 <= mid: 
        datalist[k] = temp[index1]
        k += 1
        index1 += 1
    while index2 <= end:
        datalist[k] = temp[index2]
        k+=1
        index2 += 1
    ### 병합 부분 끝 ###
    
def merge_sort(start, end):
    if end - start < 1: # 요소 1개 이하로 분활되면 리턴
        return
    mid = start + ((end - start) // 2) # 중간(start <-> end) 정의 
    merge_sort(start, mid) #분활
    merge_sort(mid + 1, end) #분활
    marge(start, end, mid)
    
answer = 0
N = int(input())
datalist = list(map(int, input().split()))
temp = [0] * (N + 1)
datalist.insert(0, 0)
merge_sort(1, N)

print(answer)
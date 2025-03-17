
n, m = map(int, input().split())
ls = list(map(int, input().split()))

def bs(): # 이분 탐색 시간 복잡도 O(log N)
    global n, m
    
    start = 0
    end = max(ls)

    answer = end
    answer_tree = 10 ** 9

    while start <= end: # start가 end보다 커지면 종료
        mid = (start + end) // 2
        tree_slice_sum = 0
        for i in ls:
            tree_slice = i - mid
            if tree_slice < 0:
                tree_slice = 0 
            tree_slice_sum += tree_slice
        if tree_slice_sum == m: # 딱 맞게 잘랐다면 
            return mid
        if tree_slice_sum > m: # 과도하게 잘랐다면
            if tree_slice_sum < answer_tree:
                answer = mid
                answer_tree = tree_slice_sum
            start = mid + 1
        elif tree_slice_sum < m: # 부족하게 잘랐다면 
            end = mid - 1
    return answer
print(bs())
        


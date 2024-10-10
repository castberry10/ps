# 한 숲 속에 여러 나무가 있다. 각 나무의 높이가 주어지며, 용사는 나무를 자를 때 원하는 높이 H를 넘는 부분을 자르려고 한다. 
# 만약 나무의 높이가 H 이하라면, 나무는 자르지 않는다.

# 용사는 일정량의 목재 M이 필요하다. 나무들을 자르고 남은 부분에서 얻는 목재의 양을 계산할 수 있는데, 
# 이때 자른 나무의 남은 부분(나무의 높이 - H)의 합이 바로 얻은 목재 양이다.

# 목재 양 M을 만족하면서도 자른 나무의 높이가 가능한 한 높도록 설정한 높이 H를 찾아야 한다.
# 주어진 나무의 높이와 원하는 높이 H를 기준으로 최대 목재의 양을 구하는 프로그램을 작성하라.

# 입력
# 첫 번째 줄에 정수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ 1,000,000,000)이 주어진다.
# 두 번째 줄에는 N개의 정수가 주어지며, 각 정수는 나무의 높이를 나타낸다. 나무의 높이는 1 이상 1,000,000 이하이다.

# 출력
# 나무를 자르고 나서 얻는 최대 목재의 양을 출력한다.

# 4 7             15
# 20 15 10 17

n, m = map(int, input().split())
ls = list(map(int, input().split()))
def bs(): # 이분 탐색
    global n, m
    
    start = 0
    end = max(ls)

    answer = end
    answer_tree = 10 ** 9

    while start < end:
        mid = (start + end) // 2
        tree_slice_sum = 0
        for i in ls:
            tree_slice = i - mid
            if tree_slice < 0:
                tree_slice = 0 
            tree_slice_sum += tree_slice
        print(start, mid, end, tree_slice_sum)
        if tree_slice_sum == m: #
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
        


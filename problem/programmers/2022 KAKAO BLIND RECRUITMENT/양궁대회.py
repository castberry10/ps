def solution(n, info):
    def get_score_diff(ryan, apeach):
        sr, sa = 0, 0
        for i in range(11):
            if ryan[i] > apeach[i]:   
                sr += (10 - i)
            elif apeach[i] > 0:       
                sa += (10 - i)
        return sr - sa

    def is_low(new_arr, old_arr):
        for i in range(10, -1, -1):
            if new_arr[i] > old_arr[i]:
                return True
            elif new_arr[i] < old_arr[i]:
                return False
        return False  

    best_diff = 0
    best_arr = [-1]

    def dfs(index, arrows_left, ryan):
        nonlocal best_diff, best_arr
        
        if index == 11:
            diff = get_score_diff(ryan, info)
            if diff > best_diff:
                best_diff = diff
                best_arr = ryan[:]
            elif diff == best_diff and diff > 0:
                if is_low(ryan, best_arr):
                    best_arr = ryan[:]
            return
        
        for x in range(arrows_left + 1):
            ryan[index] = x
            dfs(index + 1, arrows_left - x, ryan)
            ryan[index] = 0  

    ryan_arr = [0]*11
    dfs(0, n, ryan_arr)

    if best_diff <= 0:
        return [-1]
    else:
        return best_arr
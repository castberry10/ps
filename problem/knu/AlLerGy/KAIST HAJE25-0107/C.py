# x, x, y, y, z, z
def solve():
    arrow = list(map(int, input().split()))
    target = list(map(int, input().split()))
    X_lo, X_hi, Y_lo, Y_hi, Z_lo, Z_hi = 0, 1, 2, 3, 4, 5

    if  (arrow[X_lo] >= target[X_hi] or arrow[X_hi] <= target[X_lo]):
        return -1
    if  (arrow[Y_lo] >= target[Y_hi] or arrow[Y_hi] <= target[Y_lo]):
        return -1
    
    return abs(arrow[Z_lo] - target[Z_hi]) + 1
    
print(solve())
n, m, k = map(int, input().split())
# ex input 3 4 6 
# 0  1  2  3 -> 4     0	
# 4  5  6  7 -> 8	  1
# 8  9  10 11 > 12	  2
#
# 0	1	2	3

print(k // m, k % m)
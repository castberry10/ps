# 6 4
# nmlkji       nm
# oxwvuh
# pqrstg
# abcdef 00 

n, m = map(int, input().split()) # x, y
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y = 0, 0
mapdata = [[0 for _ in range(n)] for _ in range(m)]
while True: # 반복 
    # 나중에 

# answern, answerm = 0, 0

# deletecnt = 0

# while True:
#     if n <= 2 or m <= 2:
#         break
#     else:
#         n, m = n - 2, m - 2
#         deletecnt += 1
# #
# #
# #
# #
# #
# if n == 1:
#     answern = 1
#     answerm = m
# ##
# ##
# ##
# elif n == 2:
#     if m == 1:
#         answern = 2
#         answerm = 1
#     else:
#         answern = 1
#         answerm = 2
# ######
# elif m == 1:
#     answern = 1
#     answerm = m

# ###
# ###
# elif m == 2:
#     if n == 1:
#         answern = 1
#         answerm = 2
#     else:
#         answern = 1
#         answerm = 2

# print(answern + deletecnt - 1, answerm + deletecnt - 1)
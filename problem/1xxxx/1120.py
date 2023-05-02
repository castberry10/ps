# 길이가 N으로 같은 문자열 X와 Y가 있을 때, 두 문자열 X와 Y의 차이는 X[i] ≠ Y[i]인 i의 개수이다. 예를 들어, X=”jimin”, Y=”minji”이면, 둘의 차이는 4이다.

# 두 문자열 A와 B가 주어진다. 이때, A의 길이는 B의 길이보다 작거나 같다. 이제 A의 길이가 B의 길이와 같아질 때 까지 다음과 같은 연산을 할 수 있다.

# A의 앞에 아무 알파벳이나 추가한다.
# A의 뒤에 아무 알파벳이나 추가한다.
# 이때, A와 B의 길이가 같으면서, A와 B의 차이를 최소로 하는 프로그램을 작성하시오.

A, B = input().split()
Al, Bl = len(A), len(B)

answer = 10000
# ex
#range 2 
#####
###
 ###
  ###
#[a:b] aaaaa 0: 4
# aaaaa 5 0 : 5 | if 3 >>> 0 : 3, 1 : 4, 2 : 5
# 
for i in range(Bl - Al + 1):
    tempb = B[i : Al + i]
    temp = 0 
    # print(A, tempb)
    for j in range(Al):
        if tempb[j] != A[j]:
            temp += 1
    answer = min((answer, temp))
print(answer)
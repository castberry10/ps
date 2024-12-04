# DPS는 Damage Per Second의 약자이다. DPS는 측정 시간 동안의 총 데미지 양을 전체 측정 시간으로 나눈 값이다. 유저는 
# $N$ 종류의 스킬을 사용하여 상대에게 데미지를 입힐 수 있는데, 그중 
# $i$번 스킬은 
# $R_i$의 시전 대기 시간 이후 
# $A_i$의 시전 시간동안 일정한 양으로 상대에게 총 
# $D_i$만큼의 데미지를 입힌다. 시전 대기 시간은 스킬을 시전하기까지 필요한 준비 시간이며, 서로 다른 스킬은 동시에 시전될 수 있다.
# 유저는 
# $0$초 시점부터 스킬 시전 대기 시간이 지난 직후에 스킬을 시전하는 것을 반복적으로 수행한다. 이런 방식으로 사냥을 하던 유저는 본인의 실력을 자랑하고자, 측정 시작 시간 
# $S$부터 측정 종료 시간 
# $E$까지의 DPS를 계산하고자 한다. 유저를 위해 
# $S$부터 
# $E$까지의 DPS를 구해주자.
# 아직 안품

n, s1, e = map(int, input().split())
answer = 0
for i in range(n):
    s = s1
    r, a, d = map(int, input().split())
    if s != 0:
        s -= (s // r + a)
        


    s_cnt = (e - s)//(r + a) # 시전 가능 횟수 
    s_time = (e - s) - (s_cnt * (r + a))
    s_time -= r
    answer += s_cnt * d
    if s_time > 0:
        answer += (s_time / a) * d

    print(i, s_cnt * d)
print(answer / (e - s1))
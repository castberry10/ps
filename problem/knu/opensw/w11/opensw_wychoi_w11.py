n = int(input())
queue = []
for i in range(n):
    tokens = input().split(' ')
    start_time = int(tokens[0])
    duration = int(tokens[1])
    queue.append([start_time, duration])
current_time = 1
current_job = 0
cnt = 0
while queue or current_job != 0:
    if current_job == 0:
        if current_time >= queue[0][0]:
            # current_job = queue.pop(0)[1]
            temp = queue.pop(0)
            current_job = temp[1]
            current_start = temp[0]
            cnt += current_time - current_start
    if current_job != 0:
        current_job = current_job - 1
    current_time = current_time + 1
# print(current_time)
print(round(cnt / float(n), 2))
data = input()
idx = 0
while True:
    if idx == 15:
        break
    if idx == len(data) - 1:
        break
    if data[idx] == '(' and data[idx + 1] == ')':
        data = data[:idx+1] + '1' + data[idx+1:]

    if data[idx] == ')' and data[idx + 1] == '(':
        data = data[:idx+1] + '+' + data[idx+1:]

    idx += 1

print(data)
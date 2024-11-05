def auction(peoples, price):
    answer = []
    for name, money in peoples.items():
        if money >= price:
            answer.append(name)
    return answer

print(auction({'현수': 40, '경우': 25, '수진': 30}, 30))
print(auction({'현수': 40, '경우': 25, '수진': 30}, 45))
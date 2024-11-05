def cardsum(cards, n):
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            if cards[i] + cards[j] == n:
                return (i, j)
    return (-1, -1)
print(cardsum([1, 2, 3, 4, 5], 8))  # 12
print(cardsum([1, 2, 3, 1, 2, 3], 2))
print(cardsum([1, 2, 3], 6)) 
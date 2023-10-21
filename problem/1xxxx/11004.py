n, k = map(int, input().split())

list_ = list(map(int, input().split()))

list_.sort()

print(list_[k - 1])
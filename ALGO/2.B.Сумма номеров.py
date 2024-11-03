n, k = map(int, input().split())  # кол-во машин, нужное число
a = list(map(int, input().split()))
count = 0
temp_list = []
total = []

for i in range(n):
    for j in range(i, n):
        count += a[j]
        temp_list.append(a[j])
        if count == k:
            total.append(i)
            count = 0
            temp_list.clear()
            break

print(len(total))
print(total)
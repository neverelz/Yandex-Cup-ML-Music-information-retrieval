n = int(input())
a = list(map(int, input().split()))
count = 0
total_list = []


for i in range(n):
    count = count + a[i]
    total_list.append(count)
print(" ".join(map(str, total_list)))


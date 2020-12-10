nk = input().split()
n = int(nk[0])
k = int(nk[1])
flag = 0
res = []
for i in range (n - k + 2):
    if flag:
        res.append(2)
    else:
        res.append(1)
    flag = ~flag
for i in range (n - k + 2,n):
    res.append(i - n + k + 1)
for i in res:
    print(i, end = ' ')

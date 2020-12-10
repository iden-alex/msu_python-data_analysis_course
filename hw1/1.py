def check(x, arr):
    for i in arr:
        if (i == x):
            return False
    return True

n = int(input())
arr = []
for i in input().split():
    if check(int(i), arr):
        arr.append(int(i))
for i in arr:
    print (i, end=' ')
print()
print(n - len(arr))

import sys

def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)

a = 0
b = 100000
for i in range (4, -1, -1):
    numbers = range(a, b + 1, 10**i)
    for n in range(1, 11):
        print('?', numbers[n], flush=True)
    print('+')
    k = 0
    tmp = 0
    while k < 10:
        tmp = int(safe_input())
        k += 1
        if (tmp):
            a = numbers[k - 1];
            b = numbers[k]
            break
    while k < 10:
        safe_input()
        k += 1
    if (tmp == 0):
        a = 100000
        break
print('!', a)
        

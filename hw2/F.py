def brackets(n):
    for i in f(2*n, 0):
        yield i
    
def f(n, sum):
    if not n:
        yield ""
    if sum < n:
        for i in f(n - 1, sum + 1):
            yield "(" + i
    if sum:
        for i in f(n - 1, sum - 1):
            yield ")" + i

if __name__ == "__main__":
    for i in brackets(int(input())):
        print(i)

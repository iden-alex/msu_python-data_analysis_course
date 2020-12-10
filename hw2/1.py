import math

def solution1(arg):
    return [c * 4 for c in arg]

def solution2(arg):
    return [c * (k + 1) for k, c in enumerate(arg)]
 
def solution3(arg):
    return [k for k in arg if k%3 == 0 or k%5 == 0]

def solution4(arg):
    return [a[i] for a in arg for i in range(len(a))]

def solution4(arg):
    return [a[i] for a in arg for i in range(len(a))]

def solution5(arg):
    return [(a, b, c) for c in range (1, arg + 1)for b in range(1, c) 
    for a in range(1, b) if a*a + b*b == c*c]

def solution6(arg):
    return [[x+i for x in arg[1]] for i in arg[0]]

def solution7(arg):
    return [[arg[j][i] for j in range(len(arg))] for i in range(len(arg[0]))]

def solution8(arg):
    return [list(map((lambda c: int(c)), str.split(s))) for s in arg]

def solution9(arg):
    return {chr(ord('a') + i): i*i for i in arg}

def solution10(arg):
    return {str.title(k) for k in arg if len(k) > 3}

solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}

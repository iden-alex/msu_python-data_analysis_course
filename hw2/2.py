from functools import reduce
from itertools import islice
import re
import operator
import copy

def solution1(arg):
    return [int(reduce(lambda a,b: a+b, filter(str.isdigit, s[::-1]))) for s in arg]

def solution2(arg):
    return list(map(lambda x: x[0]*x[1], arg))

def solution3(arg):
    return list(filter(lambda x: x%6 == 0 or x%6 == 2 or  x%6 == 5, arg))

def solution4(arg):
    return list(filter(lambda x: bool(x), arg))

def solution5(arg):
    [operator.setitem(x, 'square', x['width']*x['length']) for x in arg]
    return arg

def solution6(arg):
    return [dict(x, square=x['width']*x['length']) for x in arg]

def solution7(arg):
    return reduce(lambda x,y: x.intersection(y),arg)

def solution8(arg):
    s = dict.fromkeys(set(arg), 0)
    [operator.setitem(s, x, s[x] + 1) for x in arg]
    return s

def solution9(arg):
    return [x['name'] for x in arg if x['gpa'] > 4.5]

def solution10(arg):
    return [x for x in arg if sum(map(int,islice(list(x),0, len(x),2))) == sum(map(int, islice(list(x), 1, len(x),2)))]
    
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

import math
def reorder_list(v, cols):
    res = [0]*len(v)
    k = 0
    for j in range (cols):
        for i in range (math.ceil(len(v)/cols)):
            if (cols*i + j < len(v)):
                res[cols*i + j] = v[k]
                k += 1
    return res

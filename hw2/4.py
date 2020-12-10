import functools 

def counter(func):
    @functools.wraps(func)
    def func_new(*args, **argv):
        flag = 0
        if not("count_calls" in func_new.__dict__):
            func_new.count_calls = 0
            func_new.count_depth = 0
            func_new.rdepth = 0
            flag = 1
        func_new.count_calls += 1;
        func_new.count_depth += 1
        cur_depth = func_new.count_depth
        result = func(*args, **argv)
        if func_new.count_depth > func_new.rdepth:
                func_new.rdepth = func_new.count_depth
                func_new.count_depth = cur_depth
        func_new.count_depth -= 1
        if flag:
            func_new.ncalls = func_new.count_calls
            delattr(func_new, "count_calls")
            delattr(func_new, "count_depth")
        return result
    return func_new

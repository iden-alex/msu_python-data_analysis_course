import random
import time
import functools
def timeout(rps):
    def decorate(func):
        @functools.wraps(func)
        def func_new(*args, **argv):
            t_start = time.time()
            result = func(*args, **argv)
            t_delta = time.time() - t_start
            if t_delta*rps < 1:
                time.sleep(1/rps - t_delta)
            return result
        return func_new
    return decorate

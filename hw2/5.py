def product(arg):
    if arg:
        for x in arg[0]:
            for y in product(arg[1:len(arg)]):
                yield (x, ) + y
    else:
        yield ()

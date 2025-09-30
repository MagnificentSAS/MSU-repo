def gen_adders(n):
    adders = []
    for i in range(n):
        def fun(x, y=i):
            return x + y
        adders.append(fun)
    return adders

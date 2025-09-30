def MINF(*args):
    def g(x):
        return min([f(x) for f in args])
    return g

def isint(f):
    def decor(*args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError("Not int in arguments")
        return f(*args)
    return decor

def istype(t):
    def mcdecor(f):
        def decor(*args):
            for i in args:
                if not isinstance(i, t):
                    raise TypeError(f"Not {t} in args")
            return f(*args)
        return decor
    return mcdecor

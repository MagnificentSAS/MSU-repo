class istype:
    def __init__(self, type):
        class mcdecor:
            def __init__(self, f):
                self.f = f

            def __call__(self, *args):
                for i in args:
                    if not isinstance(i, type):
                        raise TypeError(f"Args are not all {type}!")
                return self.f(*args)

        self.type = type
        self.mcdecor = mcdecor

    def __call__(self, f):
        return self.mcdecor(f)

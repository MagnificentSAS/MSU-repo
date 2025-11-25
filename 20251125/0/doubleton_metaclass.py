class Doubleton(type):
    _obj1 = None
    _obj2 = None
    def __call__(cls, *args, **kw):
        if cls._obj2 is None:
             cls._obj2 = super().__call__(*args, **kw)
        cls._obj1, cls._obj2 = cls._obj2, cls._obj1
        return cls._obj1

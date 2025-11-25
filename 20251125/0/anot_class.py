import inspect

class sev:
    _a : int
    def __init__(self, val):
        if isinstance(val, inspect.get_annotations(self.__class__)["_a"]):
            self._a = val
        else:
            raise TypeError("wrong val type")

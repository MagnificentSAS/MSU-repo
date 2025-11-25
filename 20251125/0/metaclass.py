#!/usr/bin/env python3

class ctype(type):
    @classmethod
    def __prepare__(metacls, name, parents, **kwds):
        print("PREPARE", name, parents, kwds)
        return super().__prepare__(name, parents, **kwds)

    def __new__(metacls, name, parents, ns, **kwds):
        print("new", metacls, name, parents, ns, kwds)
        return super().__new__(metacls, name, parents, ns)

    def __init__(cls, name, parents, namespace, **kwd):
        print("INIT", name, parents, namespace, kwd)
        return super().__init__(name, parents, namespace)

    def __call__(cls, *args, **kwargs):
        print("CALL", cls, args, kwargs)
        return super().__call__(*args, **kwargs)

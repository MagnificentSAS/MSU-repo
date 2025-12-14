import sys

class objcount:
    def __init__(self, cls):
        self.cls = cls
        self.cls.counter = 0

    def __call__(self, *args, **kwargs):
        instance = self.cls.__new__(self.cls, *args, **kwargs)
        self.cls.counter += 1

        if hasattr(self.cls, '__init__'):
            self.cls.__init__(instance, *args, **kwargs)

        return _objcountProxy(instance, self.cls)

    def __getattr__(self, name):
        return getattr(self.cls, name)


class _objcountProxy:
    def __init__(self, instance, cls):
        self._instance = instance
        self._cls = cls

    def __getattr__(self, name):
        return getattr(self._instance, name)

    def __del__(self):
        self._cls.counter -= 1

exec(sys.stdin.read())

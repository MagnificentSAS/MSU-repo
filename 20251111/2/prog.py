import sys

class Num:
    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__.get(self._name, 0)

    def __set__(self, instance, value):
        if hasattr(value, 'real'):
            instance.__dict__[self._name] = value.real
        elif hasattr(value, '__len__'):
            instance.__dict__[self._name] = len(value)
        else:
            instance.__dict__[self._name] = value


exec(sys.stdin.read())

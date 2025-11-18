import pickle

class SerCls:
    def __init__(self, l=None, d=None, n=None, s=None):
        if l:
            self.lst = l
        else:
            self.lst = []
        if d:
            self.dct = d
        else:
            self.dct = {}
        if n:
            self.num = n
        else:
            self.num = 0
        if s:
            self.st = s
        else:
            st = ""


ser = SerCls([21,2,4], {'a': 1, 'b': 2, 'c': 3}, 100500, "Fish with electrolits")
ser_str = pickle.dumps(ser)
del ser
ser1 = pickle.loads(ser_str)
print(ser1.__dict__)

ser1_str = pickle.dumps(ser1)
del SerCls

class SerCls:
    pass

ser2 = pickle.loads(ser1_str)

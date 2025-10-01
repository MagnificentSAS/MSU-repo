def sub(a, b):
    if type(a) != type(b):
        return None
    if hasattr(a, '__sub__'):
        return a - b
    if type(a) == list:
        res = []
        for obj_a in a:
            if obj_a not in b:
                res.append(obj_a)
        return res
    if type(a) == tuple:
        res = ()
        for obj_a in a:
            if obj_a not in b:
                res += (obj_a,)
        return res

    return None

a, b = eval(input())
print(sub(a, b))

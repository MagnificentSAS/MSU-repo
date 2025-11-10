def itemget(collection, index):
    return collection[index]

def safeindex(function, *args):
    try:
        res = function(*args)
    except IndexError:
        return None
    else:
        return res

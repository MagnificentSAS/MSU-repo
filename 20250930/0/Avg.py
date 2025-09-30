def average(a, *args):
    sum = a
    for i in args:
        sum += i
    sum /= len(args) + 1
    return sum

def average_ful(*args):
    if len(args) == 0:
        return "No args"
    sum = 0
    for i in args:
        sum += i
    sum /= len(args)
    return sum

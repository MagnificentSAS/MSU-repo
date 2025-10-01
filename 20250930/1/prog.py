def Pareto(*pairs):
    res = ()
    for pair1 in pairs:
        for pair2 in pairs:
            if pair1[0] <= pair2[0] and pair1[1] <= pair2[1] and (pair1[0] < pair2[0] or pair1[1] < pair2[1]):
                break
        else:
            res += (pair1,)

    return res

inp = eval(input())
print(Pareto(*inp))

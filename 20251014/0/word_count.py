def f(str):
    words = str.split()
    dict = {}
    for word in str.split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    return dict

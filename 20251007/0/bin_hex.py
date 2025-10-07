def f(s, e):

    for i in range(s, e + 1):
        print(f"{bin(i):>{len(bin(e))}} = {hex(i):<{len(hex(e))}}")

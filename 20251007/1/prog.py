from fractions import Fraction as frac

def root_check(x, w, pow_a, a_coef, pow_b, b_coef):
    curr_x = 1
    b_sum = 0
    for i in range(pow_b, -1, -1):
        b = b_coef[i]
        b_sum += b * curr_x
        curr_x *= x
    if b_sum == 0:
        return False
    curr_x = 1
    a_sum = 0
    for i in range(pow_a, -1, -1):
        a = a_coef[i]
        a_sum += a * curr_x
        curr_x *= x
    if a_sum / b_sum == w:
        return True
    return False

inp_arr = input().split(',')
for i in range(len(inp_arr)):
    inp_arr[i] = inp_arr[i].strip()

s = frac(inp_arr[0])
w = frac(inp_arr[1])
pow_a = int(inp_arr[2])
pow_b = int(inp_arr[4 + pow_a])
a_coef = []
b_coef = []
for i in inp_arr[3 : 4 + pow_a]:
    a_coef.append(frac(i))
for i in inp_arr[5 + pow_a : 6 + pow_a + pow_b]:
    b_coef.append(frac(i))

print(root_check(s, w, pow_a, a_coef, pow_b, b_coef))

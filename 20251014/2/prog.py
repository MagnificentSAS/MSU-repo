import sys
import math

MATH_ENV = {name: getattr(math, name) for name in dir(math)}

def run_interpreter(lines):
    functions = {}
    def quit_func(fmt, form, stats):
        l = form[0].split("{}")

        defined_cnt, line_cnt = stats
        print(l[0][1:], defined_cnt, l[1], line_cnt, l[2][:-1], sep='')
        return "__QUIT__"

    functions['quit'] = (['fmt'], None)
    defined_count = 1
    processed_lines = 0

    for raw_line in lines:
        line = raw_line.rstrip('\n')
        if not line:
            continue
        processed_lines += 1

        if line.startswith(':'):
            tokens = line[1:].split()
            func_name = tokens[0]
            params = tokens[1:-1]
            expr = tokens[-1]
            functions[func_name] = (params, expr)
            defined_count += 1
        else:
            name, *rest = line.split(maxsplit=1)
            if name not in functions:
                raise NameError(f"Undefined function: {name}")

            params, expr = functions[name]

            if len(params) == 0:
                args = []
            elif len(params) == 1:
                arg_str = rest[0] if rest else ''
                args = [arg_str]
            else:
                if not rest:
                    args = []
                else:
                    args = rest[0].split()

            if len(args) != len(params):
                raise TypeError(f"{name} expects {len(params)} args, got {len(args)}")

            if name == 'quit':
                result = quit_func(args[0], args, stats=(defined_count, processed_lines))
                if result == "__QUIT__":
                    break
            else:
                local_env = dict(MATH_ENV)
                for p, a in zip(params, args):
                    value = eval(a, {}, {})

                    local_env[p] = value
                value = eval(expr, {}, local_env)
                print(value)

commands = []
while command := input():
    commands.append(command)

run_interpreter(commands)

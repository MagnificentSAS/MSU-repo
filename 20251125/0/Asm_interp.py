while t := input():
    match t.split():
        case ["mov", r1, r2]:
            print(f"moving <{r2}> to <{r1}>")
        case ["push" | "pop" as cmd, *tail]:
            print(f"{cmd}ing", *tail)
        case [cmd, r1]:
            print(f"making {cmd} with {r1}")
        case _:
            print("ERROR")

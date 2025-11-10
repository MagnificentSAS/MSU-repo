print("write a number")

while c := input():
    try:
        c = int(c)
        break
    except Exception:
        print("write a number")

print(f"your number is {c}")

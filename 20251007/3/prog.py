l = input()
width = len(l) - 2
height = 0
water = 0

while True:
    l = input()
    if '.' not in l and '~' not in l:
        break
    height += 1
    water += l.count('~')

air = width * height - water

if height == 0:
    water_layers = 0
else:
    water_layers = water // height if water % height == 0 else water // height + 1

width, height = height, width

print("#" * (width + 2))

for i in range(height - water_layers):
    print(f"#{"." * width}#")
for i in range(water_layers):
    print(f"#{"~" * width}#")

print("#" * (width + 2))

if air == 0:
    air_strlen = 0
    if water == 0:
        full_strlen = 1
        water_strlen = 0
    else:
        full_strlen = len(str(water))
        water_strlen = 20
elif water == 0:
    full_strlen = len(str(air))
    water_strlen = 0
    air_strlen = 20
elif air > water:
    full_strlen = len(str(air))
    air_strlen = 20
    water_strlen = round(water / air * 20)
else:
    full_strlen = len(str(water))
    water_strlen = 20
    air_strlen = round(air / water * 20)

print("." * air_strlen, " " * (20 - air_strlen + 1), f"{air:{full_strlen}}/{width * height}", sep ="")
print("~" * water_strlen, " " * (20 - water_strlen + 1), f"{water:{full_strlen}}/{width * height}", sep ="")


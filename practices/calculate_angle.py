from math import degrees, acos, floor


def checkio(a, b, c):
    tri = []

    tri.append(a)
    tri.append(b)
    tri.append(c)
    tri.sort(reverse=True)


    x = tri[0]
    y = tri[1]
    z = tri[2]

    if x > y + z:
        print([0, 0, 0])

    if x == y == z:
        print([60, 60, 60])

    if x != y != z:
        angle_c = round(degrees(acos((y ** 2 + z ** 2 - x ** 2) / (2 * y * z))))
        angle_b = round(degrees(acos((z ** 2 + x ** 2 - y ** 2) / (2 * x * z))))
        angle_a = 180 - (angle_b + angle_c)

        result = [angle_c, angle_b, angle_a]

        print(result)



checkio(11,20,30)
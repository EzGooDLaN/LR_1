def is_obtuse(x1, y1, x2, y2, x3, y3):
    a = (x2-x1)**2 + (y2-y1)**2
    b = (x3-x2)**2 + (y3-y2)**2
    c = (x1-x3)**2 + (y1-y3)**2
    a, b, c = sorted([a, b, c])
    return a + b < c

print("Введите координаты трёх точек:")
x1, y1 = map(float, input("Точка 1 (x y): ").split())
x2, y2 = map(float, input("Точка 2 (x y): ").split())
x3, y3 = map(float, input("Точка 3 (x y): ").split())

if is_obtuse(x1, y1, x2, y2, x3, y3):
    print("Треугольник тупоугольный")
else:
    print("Треугольник не тупоугольный")

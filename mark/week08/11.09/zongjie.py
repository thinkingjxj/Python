from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
p = p[0] + p[1]
print(p)

t = [12, 15]
print(Point._make(t))

p = Point(x=13, y=16)
print(p._asdict())

p = Point(x=11, y=22)
print(p._replace(x=33))

print(p._fields)

Color = namedtuple('Coler', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
print(Pixel(11, 22, 128, 255, 0))

print(getattr(p, 'x'))

d = {'x': 2, 'y': 5}
print(Point(**d))

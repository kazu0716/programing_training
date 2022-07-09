from math import cos, radians, sin

a, b, d = map(int, input().split())
sin_d, cos_d = sin(radians(d)), cos(radians(d))
print(a * cos_d - b * sin_d, b * cos_d + a * sin_d)

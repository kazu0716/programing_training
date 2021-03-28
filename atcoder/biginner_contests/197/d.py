from math import atan2, cos, pi, sin, sqrt

N = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

ox, oy = (x0+xn2)/2, (y0+yn2)/2
r = sqrt((x0-xn2)**2 + (y0-yn2)**2)/2
theta = atan2(y0-oy, x0-ox) + 2*pi/N
x1, y1 = r*cos(theta), r*sin(theta)

print(x1+ox, y1+oy)

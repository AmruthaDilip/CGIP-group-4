import math

def rotate_point(point, angle):
    rad = math.radians(angle)
    x = point[0] * math.cos(rad) - point[1] * math.sin(rad)
    y = point[0] * math.sin(rad) + point[1] * math.cos(rad)
    return (x, y)

point = (2, 3)
angle = 45

new_point = rotate_point(point, angle)

print("Original point:", point)
print("New point after rotation:", new_point)


import math


def get_angle_a(a, b, c):
    angle_a = ((pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c))
    angle_a = math.degrees(math.acos(angle_a))
    return round(angle_a, 2)


def get_angle_b(a, b, c):
    angle_b = ((pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c))
    angle_b = math.degrees(math.acos(angle_b))
    return round(angle_b, 2)


def get_angle_c(a, b, c):
    angle_c = ((pow(a, 2) + pow(b, 2)) - pow(c, 2)) / (2 * a * b)
    angle_c = math.degrees(math.acos(angle_c))
    return round(angle_c, 2)


first_angle_a = get_angle_a(3, 7, 9)
second_angle_b = get_angle_b(3, 7, 9)
third_angle_c = get_angle_c(3, 7, 9)
# Output angles in degrees
print("\nAngles of a triangle in degrees(deg)")
print("Angle A: " + str(first_angle_a) + " deg")
print("Angle B: " + str(second_angle_b) + " deg")
print("Angle C: " + str(third_angle_c) + " deg")

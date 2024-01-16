def is_rightangled_triangle(hypotenuse, perpendicular, base):
    hypotenuse_squared = hypotenuse**2
    sum_of_squares = perpendicular**2 + base**2

    if hypotenuse_squared == sum_of_squares:
        return True
    else:
        return False
hypotenuse = float(input("Enter the length of the hypotenuse: "))
perpendicular = float(input("Enter the length of the perpendicular side: "))
base = float(input("Enter the length of the base side: "))


if is_rightangled_triangle(hypotenuse, perpendicular, base):
    print("The given sides form a right-angled triangle.")
else:
    print("The given sides do not form a right-angled triangle.")

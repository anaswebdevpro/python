from math import pi


def calculate(rad):

    area = pi * rad ** 2
    circum = 2 * pi * rad
    return area, circum

ar,cir = calculate(5)
print(f"Area: {ar}, Circumference: {cir}") 

rouned_ar = round(ar, 2)
rouned_cir = round(cir, 2)
print(f"Rounded Area: {rouned_ar}, Rounded Circumference: {rouned_cir}")
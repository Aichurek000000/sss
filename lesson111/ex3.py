import math
radius = float(input("Eneter a radius: "))
if radius > 0:
    area = math.pi * (radius ** 2)
    print(f"area: "{area}")
else:
      print(" Radius have to be a positive number")
import calculus
import os

os.system("cls")

expr = calculus.Expression(input("Enter the expression: "))  

cp = expr.check_point()  # Find critical points

print("\nCritical Points:", cp)

for point in cp:  # Pass each critical point separately
    nature = expr.check_extrema(point)  
    if nature == -1:
        print(f"At point {point}: Local Minimum")
    elif nature == 1:
        print(f"At point {point}: Local Maximum")
    elif nature == 0:
        print(f"At point {point}: Saddle Point")
    else:
        print(f"At point {point}: Inconclusive")

print(" ")

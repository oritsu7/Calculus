from sympy import *

x, y = symbols('x y')

class Expression:
    def __init__(self, func):
        self.func = func

    def check_extrema(self, point):
        diff_x = diff(self.func, x)
        diff_y = diff(self.func, y)

        R = diff(diff_x, x) #fxx
        T = diff(diff_y, y) #fyy
        S = diff(diff_x, y) #fxy

        D = (R * T - S**2).subs({x: point[0], y: point[1]}) # Hessian determinant
        R_value = R.subs({x: point[0], y: point[1]})

        if D > 0 and R_value > 0:
            return -1  # Minima
        elif D > 0 and R_value < 0:
            return 1  # Maxima
        elif D < 0:
           return 0  # Saddle point
        else:
            return "Inconclusive"
        

    def check_point(self):
        diff_x = diff(self.func, x)
        diff_y = diff(self.func, y)

        cp = solve([diff_x, diff_y], (x, y)) 

        # Handling different cases of outputs...
        if isinstance(cp, dict):  # one critical point 
            return [tuple(cp.values())]
        elif isinstance(cp, list):  # Multiple critical points...
            return [tuple(point.values()) for point in cp]
        else:
            return []  # No critical points


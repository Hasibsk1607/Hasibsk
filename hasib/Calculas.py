import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the expression
expr = sp.exp(x) * sp.cos(x)

# Simplify or differentiate/integrate if needed
simplified_expr = sp.simplify(expr)
print("Simplified Expression:", simplified_expr)

# If you want to differentiate or integrate
derivative = sp.diff(expr, x)
integral = sp.integrate(expr, x)

print("Derivative of e^x * cos(x):", derivative)
print("Integral of e^x * cos(x):", integral)

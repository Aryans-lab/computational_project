"""
Root Finding Methods

This module covers methods to find the "roots" of a function.
A root is a value 'x' where f(x) = 0.
In physics, this is incredibly common. For example:
- Finding when a projectile hits the ground (height y = 0)
- Finding equilibrium points (where net force F = 0)

We will implement two fundamental methods:
1. Bisection Method: A slow but extremely reliable "bracketing" method.
2. Newton-Raphson Method: A very fast method that uses the derivative,
   but can sometimes fail to converge if the initial guess is bad.
"""

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of the function using the Bisection Method.

    Logic:
    This relies on the Intermediate Value Theorem.
    If you have two points, 'a' and 'b', and f(a) and f(b) have OPPOSITE signs
    (one is positive, one is negative), then the function must cross zero
    somewhere between them!

    We find the midpoint 'c'. We check the sign of f(c).
    If f(c) has the same sign as f(a), the root must be between 'c' and 'b'.
    If f(c) has the same sign as f(b), the root must be between 'a' and 'c'.
    We replace 'a' or 'b' with 'c', cutting the interval in half, and repeat.

    Args:
        func (callable): The function to find the root of.
        a (float): Lower bound of the initial bracket.
        b (float): Upper bound of the initial bracket.
        tol (float): The tolerance. We stop when |f(c)| < tol.
        max_iter (int): Maximum number of iterations to prevent infinite loops.

    Returns:
        float: The approximate x value where f(x) = 0.
    """
    # Check if the initial bounds actually bracket a root
    if func(a) * func(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs. No root bracketed!")

    for i in range(max_iter):
        # Calculate the midpoint
        c = (a + b) / 2.0

        # Check if we are close enough to zero
        if abs(func(c)) < tol:
            return c

        # Determine which half the root is in
        if func(a) * func(c) < 0:
            # Root is between 'a' and 'c'
            b = c
        else:
            # Root is between 'c' and 'b'
            a = c

    print("Warning: Max iterations reached before convergence.")
    return (a + b) / 2.0


def newton_raphson_method(func, dfunc, x0, tol=1e-6, max_iter=100):
    """
    Finds a root of the function using the Newton-Raphson Method.

    Logic:
    We start with a single guess 'x0'.
    We evaluate the function and its derivative (the slope) at x0.
    We draw a tangent line to the curve at x0, and find where that tangent line
    hits the x-axis (y=0).
    That intersection point becomes our new, better guess: 'x1'.

    Formula:
    x_{n+1} = x_n - f(x_n) / f'(x_n)

    This method is blazingly fast compared to bisection, but it requires
    you to know the derivative, and it can go crazy if the slope is near zero
    (division by zero!).

    Args:
        func (callable): The function to find the root of.
        dfunc (callable): The derivative of the function.
        x0 (float): Initial guess.
        tol (float): Tolerance. Stop when |f(x)| < tol.
        max_iter (int): Maximum number of iterations.

    Returns:
        float: The approximate x value where f(x) = 0.
    """
    x = x0

    for i in range(max_iter):
        fx = func(x)

        # Check if we are close enough
        if abs(fx) < tol:
            return x

        dfx = dfunc(x)
        if dfx == 0.0:
            raise ValueError("Derivative is zero. Newton-Raphson fails.")

        # The update rule
        x = x - fx / dfx

    print("Warning: Max iterations reached before convergence.")
    return x


# ==========================================
# Examples
# ==========================================
if __name__ == "__main__":
    print("--- Root Finding Examples ---")

    # Example: Find the square root of 2.
    # We can frame this as finding the root of f(x) = x^2 - 2 = 0
    # The true answer is roughly 1.41421356

    def f(x):
        return x**2 - 2.0

    def df(x):
        # The derivative of x^2 - 2 is 2x
        return 2.0 * x

    print("Finding root of f(x) = x^2 - 2")

    # Using Bisection
    # We know the root is between 1 (where f is -1) and 2 (where f is 2)
    a, b = 1.0, 2.0
    root_bisection = bisection_method(f, a, b)
    print(f"\nBisection Method (bracket [1, 2]):")
    print(f"  Result: {root_bisection:.8f}")

    # Using Newton-Raphson
    # We just need a single guess. Let's start at x = 2.0
    x0 = 2.0
    root_newton = newton_raphson_method(f, df, x0)
    print(f"\nNewton-Raphson Method (guess x=2):")
    print(f"  Result: {root_newton:.8f}")

    print("\n(Both methods correctly find the square root of 2!)")

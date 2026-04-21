"""
Numerical Integration

This module covers numerical methods for computing definite integrals.
In physics, calculating an integral analytically is often impossible,
so we estimate the area under the curve computationally.

We will implement:
1. Trapezoidal Rule: Approximates the area under the curve by summing trapezoids.
2. Simpson's 1/3 Rule: Approximates the curve using parabolas, which is much more
   accurate for smooth functions.
"""

def trapezoidal_rule(func, a, b, n):
    """
    Computes the definite integral of a function using the Trapezoidal Rule.

    Logic:
    We divide the interval [a, b] into 'n' small sub-intervals of width 'h'.
    Instead of drawing rectangles (like a basic Riemann sum), we draw a straight
    line between (x_i, f(x_i)) and (x_i+1, f(x_i+1)), forming a trapezoid.

    The area of one trapezoid is: (h / 2) * (f(x_i) + f(x_i+1))
    When we sum them all up, the interior points get counted twice.

    Final formula:
    Integral approx = (h / 2) * [ f(a) + 2*f(x_1) + 2*f(x_2) + ... + 2*f(x_n-1) + f(b) ]

    Args:
        func (callable): The mathematical function to integrate (e.g., lambda x: x**2)
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        n (int): Number of sub-intervals (more means higher accuracy).

    Returns:
        float: The approximate value of the integral.
    """
    if n <= 0:
        raise ValueError("Number of intervals 'n' must be > 0.")

    # Width of each sub-interval
    h = (b - a) / n

    # Start the sum with the first and last terms: f(a) + f(b)
    integral = func(a) + func(b)

    # Now add 2 * f(x_i) for all the interior points
    for i in range(1, n):
        # Calculate the x-coordinate for this point
        x_i = a + i * h
        integral += 2 * func(x_i)

    # Multiply by h/2 as per the formula
    integral *= (h / 2.0)

    return integral


def simpsons_rule(func, a, b, n):
    """
    Computes the definite integral of a function using Simpson's 1/3 Rule.

    Logic:
    While the Trapezoidal Rule connects points with straight lines, Simpson's Rule
    connects groups of THREE points with a parabola (a polynomial of degree 2).
    Because many physical functions are smooth curves, parabolas fit them much
    better than straight lines, leading to highly accurate results.

    Because we need 3 points for a parabola, the number of intervals 'n' MUST be even!

    Final formula:
    Integral approx = (h / 3) * [ f(a) + 4*f(x_1) + 2*f(x_2) + 4*f(x_3) + ... + f(b) ]
    Notice the alternating 4, 2, 4, 2 pattern for the interior points.

    Args:
        func (callable): The mathematical function to integrate.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        n (int): Number of sub-intervals (MUST BE EVEN).

    Returns:
        float: The approximate value of the integral.
    """
    if n <= 0:
        raise ValueError("Number of intervals 'n' must be > 0.")
    if n % 2 != 0:
        raise ValueError("Simpson's Rule requires an EVEN number of intervals 'n'.")

    h = (b - a) / n

    # Start the sum with the first and last terms
    integral = func(a) + func(b)

    # Add the interior points with alternating weights of 4 and 2
    for i in range(1, n):
        x_i = a + i * h

        if i % 2 == 1:
            # Odd index: weight is 4
            integral += 4 * func(x_i)
        else:
            # Even index: weight is 2
            integral += 2 * func(x_i)

    # Multiply by h/3 as per the formula
    integral *= (h / 3.0)

    return integral


# ==========================================
# Examples
# ==========================================
if __name__ == "__main__":
    import math # Only used for the math.sin function and math.pi in the test

    print("--- Integration Examples ---")

    # Example 1: Integrating f(x) = x^2 from 0 to 3
    # The true analytical answer is (x^3)/3 evaluated from 0 to 3 = 27/3 = 9.0
    def f1(x):
        return x**2

    a1, b1 = 0.0, 3.0
    n1 = 6 # Use 6 intervals

    print(f"Integrating f(x) = x^2 from {a1} to {b1} (True value: 9.0)")

    trap_result = trapezoidal_rule(f1, a1, b1, n1)
    print(f"  Trapezoidal Rule (n={n1}): {trap_result}")

    simp_result = simpsons_rule(f1, a1, b1, n1)
    print(f"  Simpson's Rule   (n={n1}): {simp_result}")
    print("  (Notice Simpson's Rule gives exactly 9.0! This is because it fits parabolas,")
    print("   and our function IS a parabola, so the fit is perfect.)")


    # Example 2: Integrating a sine wave from 0 to Pi
    # The integral of sin(x) from 0 to Pi is -cos(Pi) - (-cos(0)) = 1 - (-1) = 2.0
    print(f"\nIntegrating f(x) = sin(x) from 0 to Pi (True value: 2.0)")

    n2_list = [4, 10, 50]

    for n2 in n2_list:
        trap = trapezoidal_rule(math.sin, 0.0, math.pi, n2)
        simp = simpsons_rule(math.sin, 0.0, math.pi, n2)
        print(f"  n={n2:<2}: Trapezoidal = {trap:.6f}, Simpson's = {simp:.6f}")

    print("  (Notice how Simpson's Rule converges to 2.0 much faster than Trapezoidal!)")

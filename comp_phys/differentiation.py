"""
Numerical Differentiation

This module covers numerical methods for computing the derivative of a function.
The derivative represents the rate of change (e.g., velocity is the derivative
of position).

The formal definition of a derivative is the limit as h approaches 0 of:
[f(x + h) - f(x)] / h

In numerical physics, we can't take the limit to absolute zero, so we use a very
small, finite value for 'h'. This is called a "Finite Difference".

We will implement three methods:
1. Forward Difference: Uses points x and (x + h).
2. Backward Difference: Uses points x and (x - h).
3. Central Difference: Uses points (x + h) and (x - h), skipping x itself.
   (This is usually the most accurate of the three!)
"""

def forward_difference(func, x, h=1e-5):
    """
    Computes the derivative using the Forward Difference method.

    Logic:
    We approximate the tangent line at x by drawing a line between the point
    (x, f(x)) and a point slightly ahead of it, (x+h, f(x+h)).

    Formula: f'(x) approx = [f(x + h) - f(x)] / h

    Error: The error is proportional to 'h' (we call this First-Order accuracy, O(h)).

    Args:
        func (callable): The function to differentiate.
        x (float): The point at which to evaluate the derivative.
        h (float): The small step size. Default is 1e-5.

    Returns:
        float: The approximate derivative.
    """
    return (func(x + h) - func(x)) / h


def backward_difference(func, x, h=1e-5):
    """
    Computes the derivative using the Backward Difference method.

    Logic:
    Similar to forward difference, but we look backward. We draw a line between
    (x-h, f(x-h)) and (x, f(x)).

    Formula: f'(x) approx = [f(x) - f(x - h)] / h

    Error: Also First-Order accuracy, O(h).

    Args:
        func (callable): The function to differentiate.
        x (float): The point at which to evaluate the derivative.
        h (float): The small step size.

    Returns:
        float: The approximate derivative.
    """
    return (func(x) - func(x - h)) / h


def central_difference(func, x, h=1e-5):
    """
    Computes the derivative using the Central Difference method.

    Logic:
    Instead of using the point 'x' and a point on one side, we straddle 'x' and
    use the points slightly ahead and slightly behind it: (x-h) and (x+h).

    Because we are taking a step 'h' forward AND a step 'h' backward, the total
    horizontal distance is 2h.

    Formula: f'(x) approx = [f(x + h) - f(x - h)] / (2h)

    Error: The errors from the forward and backward parts cancel out beautifully,
    leaving an error proportional to h squared! (Second-Order accuracy, O(h^2)).
    This means if you halve 'h', the error goes down by a factor of 4.

    Args:
        func (callable): The function to differentiate.
        x (float): The point at which to evaluate the derivative.
        h (float): The small step size.

    Returns:
        float: The approximate derivative.
    """
    return (func(x + h) - func(x - h)) / (2.0 * h)


# ==========================================
# Examples
# ==========================================
if __name__ == "__main__":
    import math

    print("--- Differentiation Examples ---")

    # Example: Differentiate f(x) = x^3 at x = 2.0
    # True analytical derivative is f'(x) = 3*x^2. At x=2, f'(2) = 3*(4) = 12.0
    def f(x):
        return x**3

    x_val = 2.0
    true_val = 12.0
    print(f"Differentiating f(x) = x^3 at x = {x_val} (True value: {true_val})")

    # Let's test a relatively large 'h' to clearly see the differences in accuracy
    h_test = 0.1
    print(f"\nUsing step size h = {h_test}:")

    fd = forward_difference(f, x_val, h_test)
    bd = backward_difference(f, x_val, h_test)
    cd = central_difference(f, x_val, h_test)

    print(f"  Forward  Difference: {fd:.6f}  (Error: {abs(fd - true_val):.6f})")
    print(f"  Backward Difference: {bd:.6f}  (Error: {abs(bd - true_val):.6f})")
    print(f"  Central  Difference: {cd:.6f}  (Error: {abs(cd - true_val):.6f})")

    print("\nNotice how Central Difference is drastically closer to 12.0 than the others!")

    # Now let's try a much smaller 'h'
    h_small = 0.001
    print(f"\nUsing smaller step size h = {h_small}:")
    print(f"  Central Difference: {central_difference(f, x_val, h_small):.6f}")

    # NOTE ON CHOOSING 'h':
    # You might think "I should just make 'h' equal to 1e-15 to get a perfect answer."
    # In computer science, doing that causes "Floating Point Roundoff Error".
    # Because a computer only stores ~15-17 decimal digits of precision,
    # f(x+h) and f(x) will look identical to the computer if h is too small,
    # resulting in 0.0 divided by a tiny number.
    # Usually, h = 1e-5 or 1e-6 is a safe "sweet spot" for 64-bit floats.

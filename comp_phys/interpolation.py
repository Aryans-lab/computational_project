"""
Interpolation and Extrapolation

This module covers basic methods for interpolation (finding a value between
known data points) and extrapolation (finding a value outside the known range).

In physics, you often have discrete data points (e.g., from an experiment or
a simulation) and you need to estimate the value of your function at a point
you didn't explicitly measure.

We will implement two fundamental methods:
1. Linear Interpolation: The simplest approach, drawing a straight line between two adjacent points.
2. Lagrange Interpolation: A method that fits a single polynomial of degree (N-1) through exactly N points.
"""

def linear_interpolate(x_data, y_data, x_target):
    """
    Performs linear interpolation to estimate the y-value at x_target.

    Logic:
    We have a list of x values and corresponding y values. We want to find
    the y value at some x_target. Linear interpolation assumes the function
    is a straight line between any two adjacent data points.

    The equation for a line between (x0, y0) and (x1, y1) is:
    y = y0 + (x_target - x0) * (y1 - y0) / (x1 - x0)

    Args:
        x_data (list): List of x coordinates (independent variable). Must be sorted.
        y_data (list): List of y coordinates (dependent variable).
        x_target (float): The x value where we want to estimate y.

    Returns:
        float: The estimated y value at x_target.
    """
    n = len(x_data)

    # Handle cases where x_target is outside the bounds (Extrapolation)
    # Extrapolation uses the closest two points to extend the line outward.
    if x_target <= x_data[0]:
        x0, y0 = x_data[0], y_data[0]
        x1, y1 = x_data[1], y_data[1]
    elif x_target >= x_data[-1]:
        x0, y0 = x_data[-2], y_data[-2]
        x1, y1 = x_data[-1], y_data[-1]
    else:
        # Find the two points that x_target falls between
        for i in range(n - 1):
            if x_data[i] <= x_target <= x_data[i+1]:
                x0, y0 = x_data[i], y_data[i]
                x1, y1 = x_data[i+1], y_data[i+1]
                break

    # Apply the linear interpolation formula
    # slope = (y1 - y0) / (x1 - x0)
    # y = y0 + slope * (x_target - x0)
    return y0 + (x_target - x0) * (y1 - y0) / (x1 - x0)


def lagrange_interpolate(x_data, y_data, x_target):
    """
    Performs Lagrange polynomial interpolation to estimate the y-value at x_target.

    Logic:
    Instead of drawing straight lines between adjacent points, Lagrange interpolation
    finds a single smooth polynomial curve that passes through *all* the given data points.
    If you give it N points, it constructs a polynomial of degree N-1.

    The formula is a sum of terms: P(x) = sum( y_i * L_i(x) ) for all points i.
    L_i(x) is a "basis polynomial" which equals 1 at x = x_i and 0 at all other x_j.

    L_i(x) = product( (x - x_j) / (x_i - x_j) ) for all j != i.

    This guarantees that P(x_i) = y_i, meaning the curve perfectly hits your data points!

    Args:
        x_data (list): List of x coordinates.
        y_data (list): List of y coordinates.
        x_target (float): The x value where we want to estimate y.

    Returns:
        float: The estimated y value at x_target.
    """
    n = len(x_data)
    interpolated_value = 0.0

    # Loop over every point to calculate the sum
    for i in range(n):
        # Calculate the basis polynomial L_i(x)
        L_i = 1.0
        for j in range(n):
            if i != j:
                # The term is (x - x_j) / (x_i - x_j)
                # Note: We must avoid division by zero, which happens if x_i == x_j
                L_i *= (x_target - x_data[j]) / (x_data[i] - x_data[j])

        # Add the contribution of this point to the final value
        # y_i * L_i(x_target)
        interpolated_value += y_data[i] * L_i

    return interpolated_value

# ==========================================
# Examples
# ==========================================
if __name__ == "__main__":
    print("--- Interpolation & Extrapolation Examples ---")

    # Let's say we measured the position of a particle at certain times.
    # Time (seconds)
    t_data = [0.0, 1.0, 2.0, 3.0, 4.0]
    # Position (meters) - let's assume it roughly follows y = x^2
    pos_data = [0.0, 1.0, 4.0, 9.0, 16.0]

    print(f"Data points: Times = {t_data}, Positions = {pos_data}")

    # Example 1: Interpolate at t = 1.5 seconds
    t_target = 1.5

    lin_val = linear_interpolate(t_data, pos_data, t_target)
    print(f"\nLinear Interpolation at t = {t_target}:")
    print(f"  Result: {lin_val} m")
    print("  (Note: Linear interpolation draws a line between (1.0, 1.0) and (2.0, 4.0).")
    print("   The true value of 1.5^2 is 2.25, so linear under-estimates a curve!)")

    lag_val = lagrange_interpolate(t_data, pos_data, t_target)
    print(f"\nLagrange Interpolation at t = {t_target}:")
    print(f"  Result: {lag_val} m")
    print("  (Note: Lagrange uses all points to fit a polynomial. Since our data is perfectly")
    print("   x^2, it fits the parabola perfectly and gives exactly 2.25!)")

    # Example 2: Extrapolation at t = 5.0 seconds
    t_extra = 5.0

    lin_extra = linear_interpolate(t_data, pos_data, t_extra)
    print(f"\nLinear Extrapolation at t = {t_extra}:")
    print(f"  Result: {lin_extra} m")
    print("  (It takes the line from the last two points (3.0, 9.0) and (4.0, 16.0) and extends it)")

    lag_extra = lagrange_interpolate(t_data, pos_data, t_extra)
    print(f"\nLagrange Extrapolation at t = {t_extra}:")
    print(f"  Result: {lag_extra} m")
    print("  (Because it learned the true x^2 polynomial, it correctly predicts 5^2 = 25.0!)")

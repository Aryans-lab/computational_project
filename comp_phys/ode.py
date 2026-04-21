"""
Ordinary Differential Equations (ODEs)

This module covers numerical methods for solving Initial Value Problems (IVPs).
Almost all of classical mechanics, circuits, and quantum mechanics rely on ODEs!

We have a differential equation of the form: dy/dt = f(t, y)
And we know the starting state: y(t_0) = y_0
We want to find y(t) at some future time.

We will implement two methods:
1. Euler's Method: The simplest approach. It assumes the slope stays constant
   over a small time step 'dt'. It is easy to code but highly inaccurate (O(dt)).
2. Runge-Kutta 4th Order (RK4): The "gold standard" for basic physics engines.
   It evaluates the slope at 4 different places within the time step to get a
   highly accurate weighted average (O(dt^4)).
"""

def euler_method(deriv_func, y0, t0, t_end, dt):
    """
    Solves an ODE using the Euler method.

    Logic:
    We know the current position 'y' and time 't'.
    We evaluate the slope dy/dt = f(t, y).
    We assume the object moves with that exact slope for the entire step 'dt'.
    New position: y_new = y_old + slope * dt

    Args:
        deriv_func (callable): The function f(t, y) returning the derivative dy/dt.
        y0 (float): Initial condition y(t0).
        t0 (float): Initial time.
        t_end (float): Final time to simulate up to.
        dt (float): Time step size.

    Returns:
        tuple: (list of time points, list of y values)
    """
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    # Keep stepping forward in time until we reach t_end
    # (using t + dt/2 to avoid floating point issues skipping the last step)
    while t < t_end - (dt / 2.0):
        # Calculate the slope at the current point
        slope = deriv_func(t, y)

        # Step forward
        y = y + slope * dt
        t = t + dt

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


def runge_kutta_4(deriv_func, y0, t0, t_end, dt):
    """
    Solves an ODE using the 4th-Order Runge-Kutta (RK4) method.

    Logic:
    Instead of just blindly following the slope at the start of the interval (like Euler),
    RK4 takes 4 "test" slopes:
    k1: The slope at the beginning of the interval.
    k2: The slope at the midpoint, using k1 to guess the midpoint y.
    k3: The slope at the midpoint again, using k2 to guess the midpoint y.
    k4: The slope at the end of the interval, using k3 to guess the end y.

    The final step uses a weighted average of these 4 slopes:
    y_new = y_old + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

    This is incredibly stable and accurate compared to Euler!

    Args:
        deriv_func (callable): The function f(t, y) returning dy/dt.
        y0 (float): Initial condition y(t0).
        t0 (float): Initial time.
        t_end (float): Final time.
        dt (float): Time step size.

    Returns:
        tuple: (list of time points, list of y values)
    """
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end - (dt / 2.0):
        # Calculate the 4 test slopes (the k's)
        k1 = deriv_func(t, y)
        k2 = deriv_func(t + dt/2.0, y + k1 * dt/2.0)
        k3 = deriv_func(t + dt/2.0, y + k2 * dt/2.0)
        k4 = deriv_func(t + dt, y + k3 * dt)

        # Calculate the weighted average slope and update y
        y = y + (dt / 6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)
        t = t + dt

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# ==========================================
# Examples
# ==========================================
if __name__ == "__main__":
    import math

    print("--- ODE Solver Examples ---")

    # Example: Radioactive Decay (or a cooling cup of coffee)
    # The rate of decay is proportional to the amount of substance left.
    # dy/dt = -k * y
    # Let's say k = 0.5, and we start with y(0) = 100.
    # The true analytical solution is y(t) = 100 * exp(-0.5 * t)

    def decay_deriv(t, y):
        k = 0.5
        return -k * y

    y0 = 100.0
    t0 = 0.0
    t_end = 2.0

    # Using a deliberately large time step to see the errors
    dt = 0.5

    print(f"Solving dy/dt = -0.5*y from t=0 to t={t_end} with dt={dt}")

    t_euler, y_euler = euler_method(decay_deriv, y0, t0, t_end, dt)
    t_rk4, y_rk4 = runge_kutta_4(decay_deriv, y0, t0, t_end, dt)

    # Print the final result at t=2.0
    true_final_y = 100.0 * math.exp(-0.5 * 2.0) # True answer is ~36.7879

    print(f"\nFinal values at t = 2.0 (True value: {true_final_y:.4f}):")
    print(f"  Euler Method: {y_euler[-1]:.4f}")
    print(f"  RK4 Method:   {y_rk4[-1]:.4f}")

    print("\n(Notice how Euler method drastically underestimates the curve because)")
    print("(the slope changes rapidly, but Euler assumes it's constant for 0.5 sec!)")
    print("(RK4, on the other hand, is nearly perfect even with a large time step!)")

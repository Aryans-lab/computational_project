# Computational Physics from Scratch

This repository contains a collection of Python scripts that implement fundamental numerical methods for computational physics completely from scratch.

It is designed as an educational resource, loosely inspired by the classic textbook *"Numerical Recipes"*. The goal is to strip away the "black box" of modern scientific libraries (like `numpy` or `scipy`) and show the underlying mathematical logic and algorithms using pure Python.

## Features
Every script is thoroughly commented in a tutorial-style format. The comments explain the logic, the mathematical formulas, and the potential pitfalls of each method (e.g., floating point errors, time step choices).

No external libraries are used for the mathematical algorithms—only Python's built-in `math` and `cmath` modules.

## Topics Covered

The scripts are organized into a `comp_phys/` directory and cover the following topics:

1. **Interpolation & Extrapolation** (`interpolation.py`)
   - Linear Interpolation
   - Lagrange Polynomial Interpolation
2. **Numerical Integration** (`integration.py`)
   - Trapezoidal Rule
   - Simpson's 1/3 Rule
3. **Numerical Differentiation** (`differentiation.py`)
   - Forward, Backward, and Central Finite Difference
4. **Random Number Generation** (`random_gen.py`)
   - Linear Congruential Generator (LCG)
5. **Root Finding** (`root_finding.py`)
   - Bisection Method
   - Newton-Raphson Method
6. **Ordinary Differential Equations (ODEs)** (`ode.py`)
   - Euler Method
   - 4th-Order Runge-Kutta (RK4) Method
7. **Fast Fourier Transform (FFT)** (`fft.py`)
   - Cooley-Tukey Recursive Algorithm (FFT and IFFT)

## How to Run

Each file is written as a standalone script. When you run a script directly, it executes an `if __name__ == "__main__":` block at the bottom of the file that demonstrates the methods with classic physics/math examples.

For example, to see the ODE solvers in action, run:

```bash
python comp_phys/ode.py
```

You can read the source code of any file to learn how the algorithm works, and then run it to see the numerical output.

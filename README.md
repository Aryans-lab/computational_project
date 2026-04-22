# Computational Physics from Scratch

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen.svg)]()

Welcome to **Computational Physics from Scratch**, an educational repository designed to teach the fundamental numerical methods used in physics and engineering.

Inspired by classic literature such as *"Numerical Recipes"*, this project takes a pedagogical approach by implementing essential algorithms using **pure Python**. We strictly avoid "black box" scientific libraries like `numpy`, `scipy`, or `matplotlib` to ensure that every loop, memory allocation, and mathematical operation is explicit and visible.

## 🎯 Motivation

As a physics student or self-taught developer, using library functions like `scipy.integrate.quad` is excellent for productivity, but it obscures the underlying mechanics.
How does a computer actually estimate an integral? How can a deterministic machine generate random numbers? How do physics engines compute planetary orbits?

This repository answers these questions by showing you the raw math translated into raw code. Every script acts as a mini-textbook, featuring heavy, tutorial-style comments detailing the logic, mathematical formulas, and computational limitations (like floating-point errors) of each algorithm.

---

## 📚 Table of Contents / Implemented Methods

All implementations are located in the `comp_phys/` directory.

### 1. Interpolation & Extrapolation (`interpolation.py`)
Finding values between (or outside) known discrete data points.
*   **Linear Interpolation:** Connects points with straight lines (1st-order).
*   **Lagrange Polynomial Interpolation:** Fits a single smooth polynomial of degree N-1 through exactly N points.

### 2. Numerical Integration (`integration.py`)
Estimating the area under a curve.
*   **Trapezoidal Rule:** Approximates the integral using trapezoids.
*   **Simpson's 1/3 Rule:** Approximates the integral by fitting parabolas (2nd-order polynomials) to groups of three points, offering much higher accuracy for smooth functions.

### 3. Numerical Differentiation (`differentiation.py`)
Calculating the rate of change using finite, discrete steps.
*   **Forward & Backward Difference:** First-order methods ($O(h)$ accuracy).
*   **Central Difference:** A much more accurate second-order method ($O(h^2)$) that straddles the point of interest.

### 4. Random Number Generation (`random_gen.py`)
Simulating stochastic processes (e.g., for Monte Carlo simulations).
*   **Linear Congruential Generator (LCG):** A classic pseudo-random number generator utilizing a modulus, multiplier, and increment to produce statistically random distributions.

### 5. Root Finding (`root_finding.py`)
Locating the point $x$ where $f(x) = 0$ (e.g., finding equilibrium points).
*   **Bisection Method:** A slow, steady, and guaranteed "bracketing" approach based on the Intermediate Value Theorem.
*   **Newton-Raphson Method:** A blazingly fast method that utilizes the derivative to follow tangent lines down to the root.

### 6. Ordinary Differential Equations (`ode.py`)
Solving Initial Value Problems (IVPs), the backbone of classical mechanics.
*   **Euler Method:** The simplest, most intuitive approach—assuming constant slope over a time step.
*   **4th-Order Runge-Kutta (RK4):** The "gold standard" for basic physics simulations, evaluating the slope at four points per time step for incredible accuracy.

### 7. Fast Fourier Transform (`fft.py`)
Converting signals from the Time Domain to the Frequency Domain.
*   **Cooley-Tukey Recursive Algorithm:** The legendary $O(N \log N)$ algorithm that revolutionalized digital signal processing. Includes both the Forward FFT and the Inverse FFT (IFFT).

---

## 🚀 Getting Started

### Prerequisites
You only need a working installation of **Python 3.x**. No virtual environments, `pip installs`, or heavy package management required.

### Usage

Every file in the `comp_phys` directory is written as a standalone script. At the bottom of each file, there is an `if __name__ == "__main__":` block containing executable examples relevant to physics and mathematics.

To run the examples and see the output of the algorithms, simply execute the script from your terminal:

```bash
# Example: Run the Ordinary Differential Equation solvers
python comp_phys/ode.py

# Example: Run the Fast Fourier Transform algorithm
python comp_phys/fft.py
```

### Learning Pathway
I recommend reading the source code in the order listed above. Start with the simpler concepts like Interpolation, and work your way up to the recursive Fast Fourier Transform.

Happy computing!

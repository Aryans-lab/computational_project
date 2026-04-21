"""
Random Number Generation

This module implements a basic Pseudo-Random Number Generator (PRNG).
In physics (e.g., Monte Carlo simulations, statistical mechanics), we rely
heavily on random numbers.

However, computers are deterministic; they can't do things "randomly".
Instead, we use mathematical formulas that produce a sequence of numbers
that *looks* random and passes statistical tests for randomness.

We will implement the Linear Congruential Generator (LCG).
It is one of the oldest and simplest PRNG algorithms. While modern physics
simulations often use the Mersenne Twister, LCG is the standard starting
point for learning.
"""

class LCG:
    """
    Linear Congruential Generator

    Logic:
    The formula is a simple recurrence relation:
    X_{n+1} = (a * X_n + c) mod m

    Where:
    - X is the sequence of pseudo-random numbers
    - m is the "modulus" (maximum possible number)
    - a is the "multiplier"
    - c is the "increment"
    - X_0 is the "seed" (the starting value)

    The choice of a, c, and m is CRITICAL. If chosen poorly, your numbers
    might just alternate (e.g., 1, 2, 1, 2...).
    We will use the classic parameters from Numerical Recipes.
    """

    def __init__(self, seed=12345):
        """
        Initializes the generator with a seed and standard parameters.

        Args:
            seed (int): The starting value. If you use the same seed,
                        you get the exact same sequence of "random" numbers!
        """
        self.state = seed

        # Parameters from "Numerical Recipes" (for a 32-bit generator)
        self.m = 2**32
        self.a = 1664525
        self.c = 1013904223

    def random_int(self):
        """
        Generates the next random integer in the sequence.

        Returns:
            int: A pseudo-random integer between 0 and (m-1).
        """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random_float(self):
        """
        Generates a random floating-point number between 0.0 and 1.0.

        Logic:
        We take the random integer (which is between 0 and m-1)
        and divide it by m. This normalizes it to the [0.0, 1.0) range.

        Returns:
            float: A pseudo-random float between 0.0 (inclusive) and 1.0 (exclusive).
        """
        return self.random_int() / self.m


# ==========================================
# Examples
# ==========================================
if __name__ == "__main__":
    print("--- Random Number Generation Examples ---")

    # Initialize our generator with a seed
    rng = LCG(seed=42)

    print("\nGenerating 5 random floats between 0 and 1:")
    for _ in range(5):
        print(f"  {rng.random_float():.6f}")

    # Example: Generating random numbers in a specific range [A, B)
    # Formula: value = A + (B - A) * random_float
    def random_in_range(rng, A, B):
        return A + (B - A) * rng.random_float()

    print("\nGenerating 5 random numbers between -10.0 and 10.0:")
    for _ in range(5):
        val = random_in_range(rng, -10.0, 10.0)
        print(f"  {val:.6f}")

    # The Power of the Seed:
    # If we create a new generator with the same seed, we get the same numbers!
    print("\nCreating a NEW generator with the exact same seed (42)...")
    rng2 = LCG(seed=42)
    print("First 3 floats from the new generator:")
    for _ in range(3):
        print(f"  {rng2.random_float():.6f}")
    print("(Notice these match the first 3 floats we generated initially! This is)")
    print("(an incredible feature for physics: it means you can perfectly recreate)")
    print("(a complex simulation to debug it if you know the seed!)")

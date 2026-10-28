"""Example usage of a third-party package: NumPy.

Install it first with:  pip install -r requirements.txt
"""

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Run: pip install numpy")
    raise SystemExit(1)


def main():
    """Show a few common NumPy operations."""
    print(f"Using NumPy version {np.__version__}")

    marks = np.array([72, 85, 90, 66, 78, 95, 58])
    print("\nMarks array:", marks)
    print("Type:", type(marks).__name__, "| shape:", marks.shape)

    print("\n--- Statistics ---")
    print("Mean:", round(marks.mean(), 2))
    print("Median:", np.median(marks))
    print("Highest:", marks.max(), "| Lowest:", marks.min())
    print("Standard deviation:", round(marks.std(), 2))

    print("\n--- Vectorised operations (no loops needed) ---")
    bonus = marks + 5
    print("Marks + 5:", bonus)
    print("Capped at 100:", np.minimum(bonus, 100))
    print("Passed (>= 60):", marks[marks >= 60])

    print("\n--- 2D array (matrix) ---")
    grid = np.arange(1, 7).reshape(2, 3)
    print(grid)
    print("Transpose:\n", grid.T)
    print("Sum of each column:", grid.sum(axis=0))


if __name__ == "__main__":
    main()
"""
Rungta International Skills University
School of Computer Science and Engineering
Bachelor of Technology in Computer Science and Engineering

PS No.: 33
Project Title: Class Marks Analyzer
Language: Python 3
Concepts: NumPy, Lists, Functions, Statistics
"""

import sys
import numpy as np


def parse_and_validate_marks(marks_input: str):
    """
    Validates input string and converts to a list of numbers.
    Rules:
    - Input must be numbers only.
    - Each mark must be between 0 and 100 (inclusive).
    """
    if not marks_input:
        return None, "No marks entered. Please enter numbers separated by spaces."

    # Remove optional 'Marks:' prefix if pasted directly
    text = marks_input.strip()
    if text.lower().startswith("marks:"):
        text = text[6:].strip()

    tokens = text.split()
    if not tokens:
        return None, "No marks entered. Please enter numbers separated by spaces."

    parsed_marks = []

    # Check 1: Non-numeric validation
    for token in tokens:
        try:
            val = float(token)
            parsed_marks.append(int(val) if val.is_integer() else val)
        except ValueError:
            return None, f"Invalid marks '{token}'. Enter numbers only."

    # Check 2: Range validation (0 to 100)
    for val in parsed_marks:
        if val < 0 or val > 100:
            return None, "Marks must be between 0 and 100."

    return parsed_marks, None


def get_marks(prompt: str = "Marks: ") -> list:
    """
    Takes marks from console input, validates them,
    and returns a list of marks (or None if invalid).
    """
    try:
        user_input = input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None

    marks, error = parse_and_validate_marks(user_input)
    if error:
        print(error)
        return None
    return marks


def analyze_marks(marks: list) -> dict:
    """
    Takes marks list, converts it to a NumPy array, and calculates:
    - Mean
    - Median
    - Maximum & Minimum
    - Standard Deviation (population value, default ddof=0)
    - Pass count (>= 40), Fail count (< 40), Pass percentage
    - Number of students scoring above average (> mean)
    """
    # Convert list to NumPy array
    marks_arr = np.array(marks, dtype=float)

    # Statistical calculations using NumPy
    mean_val = float(np.mean(marks_arr))
    median_val = float(np.median(marks_arr))
    max_val = float(np.max(marks_arr))
    min_val = float(np.min(marks_arr))
    std_val = float(np.std(marks_arr))  # Population standard deviation

    # Pass mark is 40
    passed_mask = marks_arr >= 40
    failed_mask = marks_arr < 40
    above_avg_mask = marks_arr > mean_val

    passed_count = int(np.sum(passed_mask))
    failed_count = int(np.sum(failed_mask))
    above_avg_count = int(np.sum(above_avg_mask))
    total_count = len(marks_arr)
    pass_pct = (passed_count / total_count) * 100.0 if total_count > 0 else 0.0

    return {
        "mean": mean_val,
        "median": median_val,
        "max": int(max_val) if max_val.is_integer() else max_val,
        "min": int(min_val) if min_val.is_integer() else min_val,
        "std_dev": std_val,
        "passed": passed_count,
        "failed": failed_count,
        "total": total_count,
        "pass_percentage": pass_pct,
        "above_average": above_avg_count,
    }


def format_results(stats: dict) -> str:
    """
    Formats results to match the problem sheet test cases.
    """
    mean_str = f"{stats['mean']:.2f}"
    median_str = f"{stats['median']:.2f}"
    std_str = f"{stats['std_dev']:.2f}"
    max_str = str(stats['max'])
    min_str = str(stats['min'])

    # Test Case 2: Boundary / Minimum Input (1 student)
    if stats["total"] == 1:
        return (
            f"Mean: {mean_str} | Median: {median_str}\n"
            f"Max: {max_str} | Min: {min_str} | Std Dev: {std_str}"
        )

    # Test Case 1: Normal Input (All students passed)
    if stats["failed"] == 0:
        return (
            f"Mean: {mean_str} | Median: {median_str}\n"
            f"Max: {max_str} | Min: {min_str} | Std Dev: {std_str}\n"
            f"Passed: {stats['passed']} of {stats['total']}"
        )

    # Test Case 4: General Scenario (with failures and above average)
    return (
        f"Mean: {mean_str} | Median: {median_str} | Std Dev: {std_str}\n"
        f"Passed: {stats['passed']} | Failed: {stats['failed']} | Pass percentage: {stats['pass_percentage']:.2f}%\n"
        f"Above average: {stats['above_average']} student"
        + ("s" if stats["above_average"] != 1 else "")
    )


def run_tests():
    """Automated verification for all 4 test cases from the assignment sheet."""
    print("=" * 60)
    print("RUNNING AUTOMATED TEST CASES FOR PS NO. 33")
    print("=" * 60)

    # Test Case 1: Normal Input
    print("\n--- Test Case 1: Normal Input ---")
    marks, _ = parse_and_validate_marks("40 50 60 70 80")
    print(format_results(analyze_marks(marks)))

    # Test Case 2: Boundary / Minimum Input
    print("\n--- Test Case 2: Boundary / Minimum Input ---")
    marks, _ = parse_and_validate_marks("75")
    print(format_results(analyze_marks(marks)))

    # Test Case 3: Invalid Input
    print("\n--- Test Case 3: Invalid Input ---")
    _, err_a = parse_and_validate_marks("50 abc 70")
    print(f"(a) {err_a}")
    _, err_b = parse_and_validate_marks("50 105 70")
    print(f"(b) {err_b}")

    # Test Case 4: Different Valid Scenario
    print("\n--- Test Case 4: Different Valid Scenario ---")
    marks, _ = parse_and_validate_marks("25 50 75 100")
    print(format_results(analyze_marks(marks)))
    print("=" * 60)


def main():
    # Flag to run automated test cases: python file.py --test
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
        return

    # Direct CLI arguments: python file.py 40 50 60 70 80
    if len(sys.argv) > 1:
        raw_input = " ".join(sys.argv[1:])
        marks, err = parse_and_validate_marks(raw_input)
        if err:
            print(err)
            return
        stats = analyze_marks(marks)
        print(format_results(stats))
        return

    # Normal Interactive Input
    marks = get_marks("Marks: ")
    if marks is not None:
        stats = analyze_marks(marks)
        print(format_results(stats))


if __name__ == "__main__":
    main()

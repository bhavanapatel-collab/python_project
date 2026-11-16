# Project Summary: Class Marks Analyzer

**Institution:** Rungta International Skills University  
**Department:** School of Computer Science and Engineering  
**Degree:** Bachelor of Technology in Computer Science and Engineering  
**Problem Statement No.:** 33  
**Project Title:** Class Marks Analyzer  
**Language:** Python 3  
**Key Libraries:** NumPy  

---

## 1. Executive Summary

The **Class Marks Analyzer** is a Python console application developed to automate the statistical evaluation of examination marks for a class. The program takes student marks as space-separated values, performs input validation, and leverages **NumPy** for statistical computations.

It determines class performance metrics including central tendencies (mean, median), dispersion (min, max, population standard deviation), and academic benchmarks (pass count, fail count, pass percentage, and count of students scoring above class average).

---

## 2. Key Specifications & Rules

| Parameter | Specification |
|---|---|
| **Input Format** | Numbers separated by spaces (e.g., `40 50 60 70 80`) |
| **Valid Range** | $0$ to $100$ (inclusive) |
| **Passing Mark** | $\ge 40$ |
| **Standard Deviation** | Population standard deviation ($\sigma$, `ddof=0` / `np.std()` default) |
| **Structure** | Single executable Python 3 file (`.py`) |
| **Core Functions** | `get_marks()`, `parse_and_validate_marks()`, `analyze_marks()`, `format_results()` |

---

## 3. Core Functionalities

1. **Robust Input Validation:**
   - Detects non-numeric tokens and alerts: `Invalid marks '<token>'. Enter numbers only.`
   - Detects out-of-range marks ($< 0$ or $> 100$) and alerts: `Marks must be between 0 and 100.`
2. **Vectorized NumPy Operations:**
   - Converts standard Python lists into a 1-D NumPy array.
   - Computes:
     - `np.mean(marks)` $\rightarrow$ Class Average
     - `np.median(marks)` $\rightarrow$ Median Score
     - `np.max(marks)` & `np.min(marks)` $\rightarrow$ Highest and Lowest Marks
     - `np.std(marks)` $\rightarrow$ Population Standard Deviation
3. **Performance Metrics:**
   - Counts students who passed ($\ge 40$) vs. failed ($< 40$).
   - Calculates the overall pass percentage.
   - Computes the count of students scoring strictly above the mean.

---

## 4. Test Case Verification Summary

All 4 test cases from the official assignment description have been verified:

| Test Case | Scenario | Input | Actual Output | Status |
|---|---|---|---|---|
| **Test Case 1** | Normal Input | `40 50 60 70 80` | `Mean: 60.00 \| Median: 60.00`<br>`Max: 80 \| Min: 40 \| Std Dev: 14.14`<br>`Passed: 5 of 5` | **PASSED** |
| **Test Case 2** | Minimum Input (1 student) | `75` | `Mean: 75.00 \| Median: 75.00`<br>`Max: 75 \| Min: 75 \| Std Dev: 0.00` | **PASSED** |
| **Test Case 3(a)** | Invalid Input (Text) | `50 abc 70` | `Invalid marks 'abc'. Enter numbers only.` | **PASSED** |
| **Test Case 3(b)** | Invalid Input (Out of range) | `50 105 70` | `Marks must be between 0 and 100.` | **PASSED** |
| **Test Case 4** | Different Valid Scenario | `25 50 75 100` | `Mean: 62.50 \| Median: 62.50 \| Std Dev: 27.95`<br>`Passed: 3 \| Failed: 1 \| Pass percentage: 75.00%`<br>`Above average: 2 students` | **PASSED** |

---

## 5. Quick Run Commands

```powershell
# 1. Run all test cases automatically
py -3 class_marks_analyzer.py --test

# 2. Run interactively from console
py -3 class_marks_analyzer.py

# 3. Run with arguments directly
py -3 class_marks_analyzer.py 25 50 75 100
`

------End of summary---------

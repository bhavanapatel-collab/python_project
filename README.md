# PS-33: Class Marks Analyzer

**Institution:** Rungta International Skills University  
**Department:** School of Computer Science and Engineering  
**Program:** Bachelor of Technology in Computer Science and Engineering  
**Problem Statement No.:** 33  
**Project Title:** Class Marks Analyzer  
**Language:** Python 3  
**Concepts Used:** NumPy, Lists, Functions, Statistics  

---

## 📌 Problem Statement

Create a Python program that takes the marks of a class as a list, validates them, and uses NumPy to calculate the:
- **Mean**
- **Median**
- **Highest (Max)**
- **Lowest (Min)**
- **Standard Deviation** (Population value, `np.std` default)
- **Pass Count** (Pass mark: 40)
- **Fail Count**
- **Pass Percentage**
- **Number of students scoring above average**

Marks are entered as numbers separated by spaces and must be strictly between 0 and 100.

---

## 🚀 Features & Implementation

1. **Input Validation:**
   - Detects non-numeric inputs and displays: `Invalid marks '<token>'. Enter numbers only.`
   - Validates marks range $[0, 100]$. If any mark is outside this range: `Marks must be between 0 and 100.`
2. **NumPy Statistical Computation:**
   - Vectorized data processing using `np.array`.
   - Accurate calculation of mean, median, max, min, and population standard deviation.
3. **Pass / Fail & Performance Metrics:**
   - Pass mark benchmark set at 40.
   - Evaluates count of students scoring strictly greater than class average.
4. **Multiple Execution Modes:**
   - **Interactive Console Mode:** Run without arguments to enter marks interactively.
   - **CLI Argument Mode:** Pass marks directly via command line arguments.
   - **Automated Test Suite:** Run with `--test` to execute verification against all project test cases.

---

## 📋 Project Structure

```
class_marks_analyzer/
│
├── class_marks_analyzer.py    # Main single-file Python 3 solution
├── README.md                  # Project overview and usage guide
├── PROJECT_REPORT.md          # Comprehensive technical report
└── .gitignore                 # Standard Python gitignore
```

---

## 💻 How to Run

### Prerequisites
Make sure Python 3 and NumPy are installed:
```bash
pip install numpy
```

### 1. Run Automated Test Cases (Recommended for grading)
```bash
python class_marks_analyzer.py --test
```
*(On Windows with Python Launcher, you can use `py -3 class_marks_analyzer.py --test`)*

### 2. Run Interactively
```bash
python class_marks_analyzer.py
```
**Example:**
```text
Marks: 40 50 60 70 80
Mean: 60.00 | Median: 60.00
Max: 80 | Min: 40 | Std Dev: 14.14
Passed: 5 of 5
```

### 3. Run with Command-Line Arguments
```bash
python class_marks_analyzer.py 25 50 75 100
```
**Output:**
```text
Mean: 62.50 | Median: 62.50 | Std Dev: 27.95
Passed: 3 | Failed: 1 | Pass percentage: 75.00%
Above average: 2 students
```

---

## 🧪 Test Cases & Expected Output

| Test Case | Scenario | Input | Expected Output | Status |
|---|---|---|---|---|
| **Test Case 1** | Normal Input | `40 50 60 70 80` | `Mean: 60.00 \| Median: 60.00`<br>`Max: 80 \| Min: 40 \| Std Dev: 14.14`<br>`Passed: 5 of 5` | **Passed** |
| **Test Case 2** | Boundary / Minimum Input (1 student) | `75` | `Mean: 75.00 \| Median: 75.00`<br>`Max: 75 \| Min: 75 \| Std Dev: 0.00` | **Passed** |
| **Test Case 3(a)** | Invalid Input (Non-numeric) | `50 abc 70` | `Invalid marks 'abc'. Enter numbers only.` | **Passed** |
| **Test Case 3(b)** | Invalid Input (Out of range) | `50 105 70` | `Marks must be between 0 and 100.` | **Passed** |
| **Test Case 4** | Different Valid Scenario | `25 50 75 100` | `Mean: 62.50 \| Median: 62.50 \| Std Dev: 27.95`<br>`Passed: 3 \| Failed: 1 \| Pass percentage: 75.00%`<br>`Above average: 2 students` | **Passed** |


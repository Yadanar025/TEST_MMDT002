# Project 7 Report: Automated Testing with Pytest

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Pytest Version & Framework:**`, `**GitHub Repository URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information
- **Name:** Khin Yadanar Aung
- **MMDT ID:** MMDT002

---

## Section 1: Test Suite Configuration
- **Pytest Version & Framework:** Pytest 8.4.2 
- **Total Test Cases Written:** 136
- **Measured Code Coverage (%):**  98%
- **Key Fixtures Implemented:**  empty_manager, sample_student, populated_manager, conftest.py (valid registration data)

---

## Section 2: Test Case Design & Boundary Analysis
- **Calculator Boundary & Edge Cases:**  empty lists, single items, negative numbers, boolean number, 0 and 1 prime edge cases, 0 to 100 score, negative value error
- **Validator Exception Scenarios:**  missing fields, weak passwords, invalid domains, out-of-range ages, non string, float,boolean

- **Student Manager State Transitions:** student addition, duplicate ID rejection, grade updates, GPA rank and filter, student deletion

---

## Section 3: Local Verification & Feature Checklist
*Check the test modules and features you successfully implemented and verified locally by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Module 1: Calculator Unit Tests with Boundary & Type Assertions (`test_calculator.py`)
- [x] Parameterized Testing with `@pytest.mark.parametrize` for Multiple Input Scenarios
- [x] Module 2: Data Validator Tests with Custom Exception Assertions (`pytest.raises`)
- [x] Module 3: Student Management System Tests with State Mutation & CRUD Verification
- [x] Reusable Pytest Fixtures in `conftest.py` for Modular Test Setup
- [x] Mutation Testing & Bug Detection Verification (Catching Hidden Mutants)
- [x] Code Coverage Analysis with `pytest-cov` (>= 85% Coverage)

---

## Section 4: Deployed and Presentation Information
- **GitHub Repository URL:** https://github.com/Yadanar025/TEST_MMDT002
- **Video Presentation Link:** https://drive.google.com/file/d/1dEZhGuI3Hn8ceLb2yLhLOR_NXblA3Ig0/view?usp=drive_link

---

## Section 5: Discussion
*Provide your written analysis for each point by replacing the bracket placeholders below:*
- **Explain why a test suite that passes 100% does not guarantee code correctness, and how mutation testing or evaluating tests against buggy code verifies test suite effectiveness.**
    A test suite that pass 100% only shows that the test don't fail again the code. It doesn't prove whether the test could catch the incorrect code and there can be a chance that the a code can still pass even the oupt was silently wong. 
- **Compare classical unit and integration testing in software engineering with modern AI engineering evaluation (e.g., LLM benchmarks, unit testing AI agents/tool calls, and Process Reward Models / LLM-as-a-judge).**
    Classical unit testing check whether individual functions or components work correctly including of correctness, while integrating tesing checks whether different components work together as expected. The AI evaluaion expecially LLMs and AI agent could produce the different outputs for the same input and consider accuracy, reasoning and consistency.

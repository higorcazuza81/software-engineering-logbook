# Chapter 2: Variables and Simple Data Types

## Chapter Objective

Apply fundamental concepts of data representation and manipulation in Python, covering primitive data types (strings and numbers) and best practices for writing clean code.

## Technical Summary and Applied Skills

- **Variable Declaration:** Practice using variables as **labels** to store and reference data in memory. Understand `NameError` diagnostics when using an undefined label.

- **String Manipulation:**
  - **Formatting:** Use of `f-strings` to create dynamic and readable strings.
  - **Case Methods:** Application of `.lower()`, `.upper()`, and `.title()` for text normalization.
  - **Data Cleaning (Stripping):** Use of `.strip()`, `.lstrip()`, and `.rstrip()` to remove whitespace from input data—an essential sanitization technique.
  - **Inspection:** Use of the `repr()` function as a debugging tool to visualize the actual representation of a string, including escape characters.
  - **Suffix Manipulation:** Use of the `.removesuffix()` method to extract data from strings.

- **Working with Numbers:**
  - Use of `int` and `float` types and basic arithmetic operations.
  - Understand the crucial difference between floating-point division (`/`), which always returns a `float`, and integer division (`//`), which discards the remainder.

- **Professional Coding Practices:**
  - **Constants:** Adopt the `ALL_CAPS` naming convention for values that should not change.
  - **Comments:** Add comments to explain the *why* behind the code, not just the *what*.

## File Structure

```plaintext
.
├── ex01_simple_message.py
├── ex02_simple_messages.py
├── ex03_personal_message.py
├── ex04_name_cases.py
├── ex05_famous_quote.py
├── ex06_famous_quote_2.py
├── ex07_stripping_names.py
├── ex08_file_extensions.py
├── ex09_number_eight.py
├── ex10_favorite_number.py
└── README.md
```

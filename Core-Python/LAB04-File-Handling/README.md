# LAB04 - File Handling in Python

Reading from and writing to files is a fundamental skill for any Python developer or DevOps engineer. In this lab, you'll learn how to handle files effectively - a critical capability for processing logs, managing configuration data, manipulating text files, and automating data workflows.

---

## 🎯 Objectives

By the end of this lab, you will:
- Open, read, and process text files using multiple techniques
- Create new files and write data to them
- Append content to existing files
- Use `with` blocks to safely manage file resources
- Handle common file errors with try-except blocks
- Process files line by line for efficient memory usage
- Work with structured data formats like CSV

---

## 🧰 Prerequisites

- Completion of LAB03 (Functions and Modules)
- Python 3.8+ installed on your system
- Basic understanding of Python syntax, data types, and control flow
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB04-File-Handling/
├── main.py                # Python script with TODOs to implement
├── input.txt              # Sample input file for reading operations
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB04-File-Handling/
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open `main.py` in your code editor and follow the TODO comments.

---

## ✍️ Your Task

Open the `main.py` file and complete all the TODOs to learn about file handling:

1. Reading from a file:
   - Use a `with` block to safely open `input.txt` in read mode
   - Read the entire content of the file
   - Print the content with a descriptive header

2. Writing to a new file:
   - Use a `with` block to open `output.txt` in write mode (`'w'`)
   - Write several lines of text to the file
   - Note that this will create a new file or overwrite an existing one

3. Appending to a file:
   - Use a `with` block to open `output.txt` in append mode (`'a'`)
   - Add additional lines of text to the file
   - Verify that the original content is preserved

4. Handling file errors:
   - Implement a try-except block to catch `FileNotFoundError`
   - Attempt to open a non-existent file
   - Display a user-friendly error message when the file isn't found

5. Bonus - Reading a file line by line:
   - Open `input.txt` and read it line by line (not all at once)
   - Print each line with its line number
   - Use efficient file iteration techniques

6. Extra Challenge - Working with CSV data:
   - Create a simple CSV file with headers and several rows of data
   - Read the CSV file and process its structured content
   - Try both manual parsing and the `csv` module

---

## 🧪 Validation Checklist

✅ You've successfully read from `input.txt` using a `with` block  
✅ You've created and written to `output.txt` in write mode  
✅ You've appended additional content to `output.txt`  
✅ You've implemented error handling for file operations  
✅ You've processed a file line by line with line numbers  
✅ You've created and read a structured CSV file (bonus)  
✅ All file operations use the `with` statement for proper resource management  
✅ Your script runs without errors  

Run your script with:
```bash
python main.py
```

After running, check the contents of `output.txt` to verify your write and append operations worked correctly.

---

## 📚 File Handling Concepts

- **File Modes**:
  - **`'r'`**: Read mode (default) - for reading files
  - **`'w'`**: Write mode - creates new file or overwrites existing file
  - **`'a'`**: Append mode - adds to the end of an existing file
  - **`'r+'`**: Read/write mode - for both reading and writing
  - **`'b'`**: Binary mode (add to other modes, e.g., `'rb'`) - for non-text files

- **File Operations**:
  - **Opening**: `open(filename, mode)` - creates a file object
  - **Reading**: `file.read()`, `file.readline()`, `file.readlines()`
  - **Writing**: `file.write(string)`, `file.writelines(list_of_strings)`
  - **Closing**: `file.close()` (automatically called in `with` blocks)
  - **Position**: `file.tell()`, `file.seek(position)`

- **The `with` Statement**:
  - Automatically manages resources (closes files even if errors occur)
  - Recommended pattern for all file operations
  - Syntax: `with open(filename, mode) as file:`

- **Error Handling**:
  - `FileNotFoundError`: When opening a non-existent file in read mode
  - `PermissionError`: When lacking permissions for the operation
  - `IsADirectoryError`: When trying to open a directory as a file
  - `UnicodeDecodeError`: When reading a file with incorrect encoding

- **CSV Handling**:
  - Basic: Split lines by comma using `line.split(',')`
  - Advanced: Use the `csv` module for robust handling
  - `csv.reader()`, `csv.writer()` for row-based operations
  - `csv.DictReader()`, `csv.DictWriter()` for header-based operations

---

## 🚀 Extension Tasks

After completing the main tasks, try these additional challenges:
1. Read and write binary files (like images) using binary modes (`'rb'`, `'wb'`)
2. Use the `json` module to read and write JSON data
3. Create a function that counts words or specific patterns in a text file
4. Implement a simple log parser that extracts information from a log file
5. Create a file backup utility that copies files with a timestamp in the filename
6. Use the `pathlib` module for more modern file path handling

---

## 💬 What's Next?

Next: [LAB05 - Error Handling and Logging](../LAB05-Error-Handling-and-Logging/) to learn how to make your scripts more robust and maintainable with proper error handling and logging techniques.

---

## 🙏 Acknowledgments

File handling is a cornerstone of practical Python programming. Whether you're processing configuration files, analyzing logs, generating reports, or managing data pipelines, the skills you've learned in this lab will be essential for your journey as a Python developer or DevOps engineer.

Happy coding! 📁🐍


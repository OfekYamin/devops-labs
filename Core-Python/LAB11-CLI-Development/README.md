# LAB11 - CLI Tool Development

Command-line tools are the backbone of DevOps automation. In this lab, you'll learn how to build professional CLI applications using Python - essential for creating maintainable, user-friendly tools that can be integrated into your automation workflows.

---

## 🎯 Objectives

By the end of this lab, you will:
- Design intuitive command-line interfaces
- Use `argparse` to build robust CLI tools
- Implement subcommands for complex functionality
- Add proper help documentation and examples
- Create colorful, user-friendly terminal output
- Handle user input and validation
- Set appropriate exit codes for automation
- Package your CLI tool for distribution
- Follow CLI design best practices

---

## 🧰 Prerequisites

- Completion of LAB10 (API Interaction)
- Python 3.8+ installed on your system
- Basic understanding of command-line concepts
- A code editor (Visual Studio Code, PyCharm, etc.)

---

## 📁 Lab Files

```
Core-Python/LAB11-CLI-Development/
├── cli_tool/              # Package directory for the CLI tool
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # CLI argument handling
│   └── commands/          # Implementation of various commands
│       ├── __init__.py
│       ├── monitor.py     # System monitoring commands
│       ├── server.py      # Server management commands
│       └── utils.py       # Utility functions for commands
├── main.py                # Entry point script
├── README.md              # This file with instructions
└── solutions.md           # Reference solutions (consult after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB11-CLI-Development/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install colorama psutil
```

4. Explore the project structure to understand the code organization:
```bash
ls -la cli_tool/
ls -la cli_tool/commands/
```

5. Open `main.py` and follow the TODOs to implement the CLI tool.

---

## ✍️ Your Task

You need to implement several components to build a complete CLI tool:

1. **Command Parser (`cli_tool/cli.py`)**:
   - Create an argument parser using `argparse`
   - Set up subparsers for different command groups
   - Add global options (verbosity, output format, etc.)
   - Implement argument validation and help messages

2. **Server Management Commands (`cli_tool/commands/server.py`)**:
   - Implement `status`, `start`, and `stop` commands
   - Add appropriate arguments for each command
   - Format output to be user-friendly
   - Use proper exit codes for success/failure

3. **Monitoring Commands (`cli_tool/commands/monitor.py`)**:
   - Implement `cpu`, `memory`, `disk`, and `all` commands
   - Use `psutil` to gather system information
   - Format output based on user preferences
   - Add filtering and sorting options

4. **Utility Functions (`cli_tool/commands/utils.py`)**:
   - Implement colorful output formatting
   - Create helpers for data formatting (bytes, dates, etc.)
   - Add confirmation prompts for destructive actions
   - Implement error handling helpers

5. **Main Entry Point (`main.py`)**:
   - Connect the CLI components
   - Handle top-level exceptions
   - Return appropriate exit codes

The CLI tool should follow a structure similar to popular DevOps tools like `aws`, `kubectl`, or `docker`, with a main command and subcommands (e.g., `mytool server start` or `mytool monitor cpu`).

Follow the TODOs and function docstrings in each file for detailed implementation guidance.

---

## 🧪 Validation Checklist

✅ The CLI tool has proper help documentation (`--help`)  
✅ All commands have appropriate subcommands and arguments  
✅ Output is formatted clearly and with color when appropriate  
✅ Error handling provides helpful messages to the user  
✅ Commands return appropriate exit codes (0 for success, non-zero for failure)  
✅ The tool follows CLI design best practices  
✅ Code is well-structured with clear separation of concerns  
✅ Command handlers have proper validation of inputs  

---

## 🧹 Cleanup

No special cleanup is required for this lab.

---

## 💬 What's Next?

Next: [LAB12 - Async Programming](../LAB12-Async-Programming/) to learn about asynchronous programming in Python - a powerful approach for handling concurrent operations in DevOps automation. 
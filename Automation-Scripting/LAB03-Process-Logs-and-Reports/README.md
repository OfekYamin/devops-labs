# LAB03 - Process Logs and Generate Reports with Python

Log files contain valuable operational data. In this lab, you'll write Python code to parse a sample log file, extract meaningful information, and generate a summary report - an essential skill for DevOps automation.

---

## 🎯 Objectives

By the end of this lab, you will:
- Open and read a text-based log file
- Parse log entries using string operations or regular expressions
- Analyze logs to identify patterns and extract metrics
- Generate a formatted report summarizing your findings
- Handle different log levels (ERROR, WARNING, INFO, DEBUG)
- (Bonus) Identify trends and notable events in the logs

---

## 🧰 Prerequisites

- Completion of LAB02 (Automate File Downloads)
- Python 3.8+ installed
- Basic understanding of file I/O and string manipulation

---

## 📁 Lab Files

```
Automation-Scripting/LAB03-Process-Logs-and-Reports/
├── logs.txt           # Sample input log file for analysis
├── parser.py          # Skeleton file with TODOs for you to implement
├── README.md          # This file with instructions
└── solutions.md       # Reference solutions (only check after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB03-Process-Logs-and-Reports/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Open `parser.py` and follow the TODOs to implement your log parser and report generator

---

## ✍️ Your Task

You need to implement a log analysis tool that:

1. Reads the provided `logs.txt` file
2. Analyzes the log entries to extract:
   - Counts of each log level (ERROR, WARNING, INFO, DEBUG)
   - Time range of the logs (first and last timestamp)
   - Types of errors that occurred
   - Any notable events or patterns
3. Generates a report file (`report.txt`) with a summary of your findings

The log file format is:
```
[YYYY-MM-DD HH:MM:SS] LEVEL: Message
```

The skeleton code with TODOs is provided in `parser.py`. Follow the TODOs to complete the implementation.

### Expected Report Format:

A sample report format is provided at the bottom of `parser.py` to guide your implementation.

---

## 🧪 Validation Checklist

✅ Script successfully reads and parses the log file  
✅ Log levels are correctly counted and percentages calculated  
✅ Time range is correctly identified from timestamps  
✅ Error types are categorized and counted  
✅ Notable events are identified and reported  
✅ Report is generated with clear, well-formatted output  

---

## 🧹 Cleanup
You may delete any generated `report.txt` file after completing the lab.

---

## 💬 What's Next?
Move on to [LAB04 - System Monitoring Scripts](../LAB04-System-Monitoring-Scripts/) to collect and display live system metrics.

---

## 🙏 Acknowledgments
Log analysis is a critical skill for DevOps engineers. Automating this process with Python can save hours of manual work and provide valuable insights.

Happy analyzing! 📊🐍
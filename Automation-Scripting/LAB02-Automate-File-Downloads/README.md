# LAB02 - Automate File Downloads with Python

In this lab, you will write a script to download files from the internet. This type of automation is useful for fetching logs, backups, or even binary artifacts in DevOps workflows.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use the `requests` module to download files via HTTP
- Save files to disk using Python
- Handle response status and error conditions
- Add command-line arguments for better usability (bonus)
- Implement progress indicators for larger files (bonus)

---

## 🧰 Prerequisites

- Completion of LAB01 (Simple CLI Tool)
- Python 3.8+ installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB02-Automate-File-Downloads/
├── downloader.py        # Skeleton file with TODOs for you to implement
├── requirements.txt     # Required dependencies
├── README.md            # This file with instructions
└── solutions.md         # Reference solutions (only check after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB02-Automate-File-Downloads/
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Open `downloader.py` and follow the TODOs to implement your file downloader

---

## ✍️ Your Task

You need to implement a file downloader that:

1. Uses the `requests` library to download files from URLs
2. Saves the downloaded content to a file on disk
3. Handles potential errors gracefully:
   - HTTP error status codes
   - Network connection issues
   - File system errors
4. (Bonus) Accepts command-line arguments for URL and filename
5. (Bonus) Shows a progress indicator for larger files

The skeleton code with TODOs is provided in `downloader.py`. Follow the TODOs to complete the implementation.

### Example URLs for Testing:

- Text file: `https://raw.githubusercontent.com/python/cpython/master/README.rst`
- Small image: `https://www.python.org/static/img/python-logo.png`

---

## 🧪 Validation Checklist

✅ Script successfully downloads files from URLs  
✅ Downloaded files are saved correctly to disk  
✅ HTTP status codes are checked and handled  
✅ Error handling for network and file system issues  
✅ (Bonus) Command-line arguments work correctly  
✅ (Bonus) Progress indicator shows download status  

---

## 🧹 Cleanup
You may delete any downloaded files after the lab.

---

## 💬 What's Next?
Explore [LAB03 - Process Logs and Reports](../LAB03-Process-Logs-and-Reports/) to practice parsing and summarizing data from downloaded files.

---

## 🙏 Acknowledgments
Automation isn't just about infrastructure — data fetching and scripting are just as essential.

Happy downloading! 📥🐍
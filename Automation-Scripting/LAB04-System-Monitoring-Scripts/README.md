# LAB04 - System Monitoring Scripts with Python

System monitoring helps keep your infrastructure healthy and responsive. In this lab, you'll create a Python script that collects and displays key system metrics using the `psutil` library - an essential skill for DevOps engineers.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use the `psutil` library to gather system metrics (CPU, memory, disk, network)
- Format and display metrics in a user-friendly way
- Implement real-time monitoring with periodic updates
- (Bonus) Create visual representations of system usage
- (Bonus) Add command-line arguments for customization

---

## 🧰 Prerequisites

- Completion of LAB03 (Process Logs and Reports)
- Python 3.8+ installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB04-System-Monitoring-Scripts/
├── monitor.py          # Skeleton file with TODOs for you to implement
├── requirements.txt    # Required dependencies
├── README.md           # This file with instructions
└── solutions.md        # Reference solutions (only check after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB04-System-Monitoring-Scripts/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Open `monitor.py` and follow the TODOs to implement your system monitoring tool

---

## ✍️ Your Task

You need to implement a system monitoring tool that:

1. Collects system metrics using the `psutil` library:
   - CPU usage percentage
   - Memory usage (total, used, available, percentage)
   - Disk usage (total, used, free, percentage)
   - (Bonus) Network I/O statistics

2. Displays these metrics in a clear, readable format:
   - Use formatting to align values and add units
   - (Bonus) Add visual elements like progress bars

3. (Bonus) Updates the display at regular intervals:
   - Implement a monitoring loop with a sleep interval
   - Allow for clean termination with Ctrl+C

The skeleton code with TODOs is provided in `monitor.py`. Follow the TODOs to complete the implementation.

### Metrics to Collect:

The `psutil` library provides easy access to system information:
- `psutil.cpu_percent()` - CPU usage percentage
- `psutil.virtual_memory()` - Memory information
- `psutil.disk_usage('/')` - Disk information
- `psutil.net_io_counters()` - Network I/O statistics

---

## 🧪 Validation Checklist

✅ Script collects and displays CPU usage  
✅ Memory metrics (total, used, available) are shown  
✅ Disk usage information is properly formatted  
✅ (Bonus) Network statistics are included  
✅ (Bonus) Display updates periodically in a loop  
✅ Output is clear, well-formatted and easy to read  

---

## 🧹 Cleanup
You can terminate the script with `Ctrl+C` if it's running in a loop.

---

## 💬 What's Next?
Continue to [LAB05 - API Integration Tool](../LAB05-API-Integration-Tool/) to learn how to interact with web APIs for automation tasks.

---

## 🙏 Acknowledgments
System monitoring scripts are essential tools in a DevOps engineer's toolkit. They provide immediate visibility into your infrastructure's health and can help identify potential issues before they become critical.

Happy monitoring! 📊🐍
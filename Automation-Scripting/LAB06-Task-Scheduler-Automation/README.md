# LAB06 - Task Scheduler Automation with Python

Automating recurring tasks is a core DevOps responsibility. In this lab, you'll create a Python script that can schedule and manage automated tasks without relying on external tools like cron or Windows Task Scheduler - a valuable skill for cross-platform automation.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a Python-based task scheduler using the `schedule` library
- Implement different scheduling patterns (intervals, daily, specific times)
- Define reusable task functions with proper logging
- Run multiple tasks on independent schedules
- Handle graceful termination of long-running processes
- (Bonus) Implement more complex tasks with dependencies

---

## 🧰 Prerequisites

- Completion of LAB05 (API Integration Tool)
- Python 3.8+ installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB06-Task-Scheduler-Automation/
├── scheduler.py          # Skeleton file with TODOs for implementing the scheduler
├── tasks.py              # Skeleton file with TODOs for implementing task functions
├── requirements.txt      # Required dependencies
├── README.md             # This file with instructions
└── solutions.md          # Reference solutions (only check after completing)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB06-Task-Scheduler-Automation/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Open and explore the provided files:
   - `tasks.py` contains skeleton code for defining your automated tasks
   - `scheduler.py` contains skeleton code for setting up and running the scheduler

---

## ✍️ Your Task

You need to implement a task scheduler system that:

1. Defines task functions in `tasks.py`:
   - A logging function to record task execution with timestamps
   - A system check task to monitor resources (simulated)
   - A backup task to demonstrate a data backup process (simulated)
   - A cleanup task to remove old files (simulated)
   - (Bonus) Additional task of your choice

2. Creates a scheduler in `scheduler.py` that:
   - Sets up multiple tasks with different schedules
   - Runs tasks at specified intervals
   - Handles clean shutdown when interrupted
   - Logs activity for monitoring purposes

The skeleton code with TODOs is provided in both Python files. Follow the TODOs to complete the implementation.

### Example Scheduling Patterns:

The `schedule` library provides various scheduling options:
- `schedule.every(10).minutes.do(some_task)` - Run every 10 minutes
- `schedule.every().hour.do(some_task)` - Run every hour
- `schedule.every().day.at("10:30").do(some_task)` - Run every day at 10:30
- `schedule.every().monday.do(some_task)` - Run every Monday

For testing purposes, you can use shorter intervals like seconds:
- `schedule.every(5).seconds.do(some_task)` - Run every 5 seconds

---

## 🧪 Validation Checklist

✅ Task functions are implemented with proper logging  
✅ Scheduler correctly sets up tasks with different schedules  
✅ Main loop runs and executes tasks at the right times  
✅ Script handles keyboard interrupts gracefully  
✅ Task execution is properly logged  
✅ (Bonus) At least one complex/realistic task is implemented  
✅ (Bonus) Script maintains a log file of all activities  

---

## 🧹 Cleanup
Press Ctrl+C to stop the scheduler when done testing. You may also want to remove any log files or data created during testing.

---

## 💬 What's Next?
Ready to explore cloud automation? Head to the Cloud Automation section to begin working with AWS, Azure, or GCP via Python SDKs.

---

## 🙏 Acknowledgments
Task automation and scheduling are foundational DevOps skills. While many environments provide built-in schedulers like cron, having a Python-based solution gives you flexibility, portability, and the ability to implement complex logic in your scheduled tasks.

Happy scheduling! ⏰🐍 
#  Simple Keylogger (Educational Project)

## Overview

This project is a **basic keylogger** developed in Python as part of my internship. It demonstrates how keyboard inputs can be captured and logged into a file using event listeners.

The main goal of this project is to understand how low-level input handling works in operating systems and to highlight the importance of **ethical considerations in cybersecurity**.

---

## Features

* Captures keyboard input in real-time
* Logs keystrokes into a text file (`key_log.txt`)
* Handles both normal and special keys (e.g., Space, Enter)
* Stops safely when the **ESC key** is pressed
* Lightweight and easy to understand (beginner-friendly)

---

## Technologies Used

* Python
* `pynput` library

---

## Project Structure

```
simple-keylogger/
│── keylogger.py       # Main script
│── key_log.txt        # Output file (generated automatically)
│── README.md          # Documentation
```

---

## Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/simple-keylogger.git
cd simple-keylogger
```

### 2. Install dependencies

```
pip install pynput
```

### 3. Run the program

```
python keylogger.py
```

---

## Usage

* Run the script
* Start typing on your keyboard
* All keystrokes will be saved in `key_log.txt`
* Press **ESC** to stop the program

---

## How It Works

* The program uses `pynput.keyboard.Listener` to monitor key presses
* Each key press is captured and processed
* Characters are written into a file
* Special keys are formatted for readability

---

## Ethical Considerations

This project is strictly for **educational purposes only**.

* It does **not run in the background**
* It requires **user execution and awareness**
* It should **never be used for unauthorized monitoring**

> Always obtain proper consent before monitoring any user activity.

---

## Learning Outcomes

Through this project, I learned:

* Event-driven programming in Python
* Keyboard input handling
* File handling and logging
* The importance of ethical responsibility in cybersecurity

---

## Author

**Apomah John Elike**
Aspiring System Administrator | Cybersecurity Enthusiast

---

## 📌 Acknowledgment

This project was completed as part of my internship program.


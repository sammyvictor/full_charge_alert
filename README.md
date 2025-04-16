# 🔋 Battery Alert - Python Background Notifier

A simple Python script that notifies you with a sound when your laptop battery is fully charged. Useful for preserving battery health by reminding you to unplug the charger when the battery hits a specified level (default is 100%).

---

## 📦 Features

- Monitors battery status using `psutil`.
- Plays an audio alert when the battery is full.
- Can run silently in the background on startup.
- Customizable battery percentage threshold.
- Easily convert to a `.exe` for Windows systems.

---

## ⚙️ Requirements

- **Python 3.11**
- [pip](https://pip.pypa.io/en/stable/)
- Virtual Environment (recommended)
- Dependencies:
  - `psutil`
  - `pygame`
  - `pyinstaller`(optional)

---

## 💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/battery_alert.git
cd battery_alert
```

### 2. Create and Activate a Virtual Environment

#### Windows:

```bash
py -3.11 -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install psutil pygame
```

---

## 🔄 Customize Battery Alert Level

Open `battery_alert.py` and change this line:

```python
if battery and battery.percent >= 100 and battery.power_plugged:
```

Change `100` to `80` or your desired level to trigger the alert sooner.

---

---

## 🔄 Change alert sound

Open `battery_alert.py` and change this line:

```python
pygame.mixer.music.load("charge_complete.mp3")
```

Change `charge_complete.mp3` to `battery_alert.mp3` or any other audio of choice.

---

## 🛠 Convert Script to EXE (Windows only)

Install PyInstaller:

```bash
pip install pyinstaller
```

Convert your script to an executable:

```bash
pyinstaller --onefile --noconsole battery_alert.py
```

✅ `--noconsole` ensures the app runs silently in the background without opening a command prompt window.

The executable will be created in the `dist` folder.

---

## 🚀 Run on Startup (Windows)

1. Press `Win + R`, type: `shell:startup`, and hit Enter.
2. Paste a **shortcut** of the `.exe` file from the `dist` folder into the Startup folder.

Now the script will run automatically every time you start your computer — silently in the background.

---

## 🔄 Updating the Script?

If you change the script (like modifying the battery percentage threshold), **you must rebuild the executable** using:

```bash
pyinstaller --onefile --noconsole battery_alert.py
```

> The `.exe` does **not** automatically update from the `.py` file.

---

## 🧠 Background Execution

- When built with `--noconsole`, the program will not show any window.
- Only the audio alert plays when the condition is met.
- It continues running silently in the background after boot.

---

# 💚 GRAYBYTE-REAPER-X 💚

**A Simple Tool for Lazy Hackers with Potato PCs**
<br><br>
<p align="center">
  <img src="https://raw.githubusercontent.com/Graybyt3/Graybyte-Reaper-X/refs/heads/main/GRAY-REAPER-X.png" alt="header banner" />
</p>
<br><br>

**GRAYBYTE-REAPER-X**, is a Python script for lazy people like me who don’t want to work hard. Got a weak PC that can’t handle big jobs? No problem—this splits them into small tasks so you can run it and sleep. Made by GRAYBYTE for slackers who hack smart, not hard.

---

## 🤔 Purpose

This script helps you:
- Take `.txt` files from one folder.
- Run them with your own `x.py` script.
- Move finished files to another folder.
- Save logs so you don’t need to check much.

It’s for lazy hackers with slow PCs who want easy wins—security stuff, server work, whatever.

---

# 🥷🏽 For Whom This Script Is

This is for hackers who want to start a job, walk away, and not care about their weak PC or server dying. Here’s how it works for you:

- **Work While You’re Gone**: Got 10,000 URLs to hack? Split them into small `.txt` files (like 100 URLs each). Start `GRAYBYTE-REAPER-X`, leave, and it runs each file one by one with your `x.py`. Come back later—job’s done, no babysitting.
- **No Resource Worries**: Slow PC or cheap server? No stress. It does one small task at a time, so it won’t crash your system. Your potato rig keeps chugging along, even if it’s old or weak.
- **Hacker Freedom**: Blackhat hitting targets, grayhat testing sites, whitehat checking servers—all set it up, go eat or sleep, and check `ChaosLogger/` later. No need to watch or tweak while it runs.

Example: A hacker wants to scan 5,000 sites. Splits them into 50 files, runs it, and leaves. `GRAYBYTE-REAPER-X` grinds through, logs everything, and moves files. They return to results—easy, no sweat.

---

## 🔥 Features

- **Colorful Text**: Looks cool on your screen with `colorama`.
- **Fancy ASCII Art**: Because boring text sucks.
- **Works on Linux/Windows**: Paths like `/home/user/` or `C:\\Users\\`. macOS? Nope, too fancy.
- **Category Based Logs**:
  - `byte-error-log.txt`: Shows mistakes.
  - `byte-stream.txt`: Tells what’s running.
  - `byte-archive.txt`: Saves what’s done.
- **Handles Errors**: Breaks? It shouts but keeps going.
- **Moves Files**: Keeps things clean for you.
- **Tracks Time**: Logs how long it takes.

---

# 👾 Technical Overview: How This Script Works


- **Python Tools It Uses**:
  - **`subprocess`**: Runs your `x.py` like a separate helper. It’s like telling Python, “Ei, ei script ta onno file diye start koro," ar tarpor shesh hobar jonno wait koro.


- **How It Runs**:
  1. Sets up your folders (`input_directory`, `output_directory`, `ChaosLogger`).
  2. Finds all `.txt` files in `input_directory`. None? It yells and logs it.
  3. Checks if `x.py` is there. No? Stops and complains.
  5. Adds tiny breaks (0.5 seconds) between steps so your slow PC stays happy.

- **Why It’s Good**: It’s simple—one file at a time, no big memory use, no crash. You set it up, it runs alone, and logs everything. Perfect for lazy hackers with weak gear.

---

## 🤔 Requirements

- **Python 3**: Makes it run.
- **x.py**: Your own script (you make it).
- **System**: Linux or Windows. macOS? No way.
- **Permissions**: Let it read/write your folders.

---

## 🏃‍➡️ How to Use

### 1. Get It Ready
Grab it and go inside:

``git clone https://github.com/Graybyt3/Graybyte-Reaper-X.git``  
``cd GRAYBYTE-REAPER-X``  
``python graybyte-reaper-x.py``  

## __🎥 Video demonstration and use : [https://www.youtube.com/watch?v=UdjatH8mwR4](https://www.youtube.com/watch?v=qKHUhMRcPVo)__



# 👨🏻‍💻 FOR MORE INFORMATION AND SUPPORT 👨🏻‍💻

[TELEGRAM](https://t.me/rex_cc) | 
[FACEBOOK](https://www.facebook.com/graybyt3) | 
[X](https://x.com/gray_byte) | 
[INSTAGRAM](https://www.instagram.com/gray_byte)



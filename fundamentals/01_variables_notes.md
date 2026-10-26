# Lesson 1 Notes: Variables and Printing

Companion notes for `01_variables.py`. A variable is a labeled box that holds a value. Every script you write starts here.

The code from the lesson:

```python
ip = "203.0.113.45"
hostname = "WORKSTATION-07"
event_id = 4625
failed_attempts = 7

print("Source IP:", ip)
print("Host:", hostname)
print("Event ID:", event_id)
print("Failed attempts:", failed_attempts)

print(f"ALERT: {failed_attempts} failed logins from {ip} on {hostname}")
```

---

## Core terms

| Term | Plain-English meaning | Example |
|---|---|---|
| **Variable** | A labeled box that holds a value. | `ip`, `hostname` |
| **Assignment** | Putting a value into a variable using `=`. | `failed_attempts = 7` |
| **Value** | The actual data stored in a variable. | `"203.0.113.45"`, `7` |
| **String** | Text. Anything inside quotes. | `"WORKSTATION-07"` |
| **Integer** | A whole number, with no quotes. | `4625`, `7` |
| **Data type** | The kind of value: text, number, and so on. | string, integer |
| **Function** | A built-in action you call with parentheses. | `print(...)` |
| **Argument** | The input you hand to a function. | `ip` in `print(ip)` |
| **Output** | What a script displays when it runs. | The lines printed in Terminal |
| **f-string** | A string starting with `f` that inserts variables inside `{}`. | `f"from {ip}"` |
| **Script** | A file of Python instructions that runs top to bottom. | `01_variables.py` |

---

## What each part of the lesson does

### 1. Creating variables

```python
ip = "203.0.113.45"
event_id = 4625
```

- The name goes on the left, the value on the right, and `=` connects them.
- `=` here means "store this," not "is equal to."
- Python reads from top to bottom, so a variable has to exist **before** you use it.
- Variable names can use letters, numbers, and underscores, but cannot start with a number or contain spaces. `failed_attempts` is valid and `failed attempts` is not.

### 2. Strings vs integers

```python
hostname = "WORKSTATION-07"   # string (in quotes)
failed_attempts = 7           # integer (no quotes)
```

- **Quotes make it text.** `"7"` and `7` look similar but are different things.
- You can do math on integers (`failed_attempts + 1` gives `8`) but not on text.
- An IP address is a string, even though it's made of numbers, because it has dots and you wouldn't do math on it.
- Event IDs like `4625` are stored as integers here, but are sometimes strings when they come out of a log file. Watch for that in later lessons.

### 3. `print()`

```python
print("Source IP:", ip)
```

- `print()` displays something on screen.
- Anything in quotes prints exactly as typed. A variable name without quotes prints the **value** stored inside it.
- Commas between items add a space between them automatically.
- Compare `print("ip")` (shows the word `ip`) with `print(ip)` (shows `203.0.113.45`).

### 4. f-strings

```python
print(f"ALERT: {failed_attempts} failed logins from {ip} on {hostname}")
```

- The `f` before the opening quote turns on variable insertion.
- Inside `{}` goes the **name of a variable**, not the value itself. Python looks up the name and swaps in the value.
- Wrong: `{203.0.113.45}` causes a `SyntaxError`. Right: `{ip}`.
- This is the cleanest way to build alert messages, because the text and the data live in one line.

### 5. Changing a value

- To change what the script reports, edit the value on one line (for example `failed_attempts = 12`), save, and run again.
- Every `print` that uses that variable updates automatically. This is why variables beat typing values directly into many places.

---

## Running a script

```bash
python3 01_variables.py
```

- `python3` is the program, and `01_variables.py` is the file you hand it.
- You must be in the folder that contains the file, or give the full path.
- Save the file (Cmd+S) before each run, or you'll be running the old version.

---

## Errors and what they mean

| Error | Cause | Fix |
|---|---|---|
| `NameError: name 'ip' is not defined` | Used a variable before creating it, or misspelled it | Define it above the line that uses it, and check spelling |
| `SyntaxError: f-string: invalid syntax` | A value was typed inside `{}` instead of a variable name | Put variable names inside `{}` |
| `SyntaxError: unterminated string literal` | A quote was opened but never closed | Add the missing closing quote |
| `can't open file ... No such file or directory` | Wrong folder or filename | Run `ls` to see the files, then `cd` to the right folder |

How to read any Python error: look at the **last line** for the error type, and the **line number** above it for where to look.

---

## Interview-style explanation

> "A variable stores a piece of data under a name so I can reuse it. In my scripts I store things like the source IP, hostname, event ID, and failure count, then print or compare them. I use f-strings to build alert messages, so the text stays readable and updates automatically when the data changes."

---

## Self-check questions

1. What is the difference between `print("ip")` and `print(ip)`?
2. Why is `"7"` different from `7`?
3. Why is an IP address stored as a string instead of a number?
4. What happens if you use a variable on a line above where you created it?
5. Why does `{203.0.113.45}` fail inside an f-string?

Answers: the first shows the word `ip`, the second shows the value stored in `ip`; `"7"` is text and `7` is a number you can do math on; it contains dots and you never do math on it; Python raises a `NameError`, because it reads top to bottom; braces expect a variable name, not a raw value.

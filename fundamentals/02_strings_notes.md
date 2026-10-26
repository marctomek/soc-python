# Lesson 2 Notes: Strings

Companion notes for `02_strings.py`. Every term used in the lesson, explained in plain English with a SOC example.

The sample log line used throughout:

```python
line = "Oct 16 09:14:02 server sshd[1234]: Failed password for admin from 203.0.113.45 port 51234 ssh2"
```

---

## Core terms

| Term | Plain-English meaning | Example |
|---|---|---|
| **String** | Text. Anything inside quotes. | `"admin"`, `"203.0.113.45"` |
| **Variable** | A labeled box that holds a value. | `line = "Oct 16 ..."` |
| **List** | An ordered collection of items in square brackets. | `['Oct', '16', 'server']` |
| **Index** | The position number of an item in a list. Counting starts at **0**. | `parts[0]` is the first item |
| **Negative index** | Counts from the end. `-1` is last, `-2` is second to last. | `parts[-1]` is `ssh2` |
| **Boolean** | A value that is either `True` or `False`. | `"Failed password" in line` gives `True` |
| **Function** | A built-in action you call with parentheses and give input to. | `print(...)`, `len(...)` |
| **Method** | An action that belongs to a value, written with a dot after it. | `line.split()`, `line.upper()` |
| **Comment** | A note for humans. Python ignores anything after `#`. | `# Count from the end` |
| **Whitespace** | Invisible characters: spaces, tabs, newlines. | The stray space before `Oct` |
| **f-string** | A string starting with `f` that inserts variables inside `{}`. | `f"User {username}"` |

---

## What each part of the lesson does

### 1. `in` (checking if text is inside a string)

```python
print("Failed password" in line)
```

- `in` asks: "does this text appear anywhere in that string?"
- It returns a **boolean**: `True` or `False`.
- This is the filter from Lesson 1. It is how a script decides whether a log line is worth looking at.
- It is case-sensitive. `"failed password"` would return `False` on this line.

### 2. `.split()` (breaking a string into a list)

```python
parts = line.split()
```

- Cuts the string at every space and returns a **list** of the pieces.
- Result: `['Oct', '16', '09:14:02', 'server', 'sshd[1234]:', 'Failed', ...]`
- You can split on something other than a space by putting it in the parentheses: `line.split(":")`.
- SPL equivalent: roughly what `rex` or `split` does to pull fields out of raw text.

### 3. Indexing with `parts[number]`

```python
print(parts[0])   # Oct
print(parts[5])   # Failed
```

- Square brackets after a list grab one item by position.
- **Counting starts at 0**, so the first item is `[0]`, not `[1]`.
- Asking for a position that doesn't exist (like `parts[99]`) causes an `IndexError`.

Position map for the sample line:

```
0: Oct            7: for
1: 16             8: admin
2: 09:14:02       9: from
3: server        10: 203.0.113.45
4: sshd[1234]:   11: port
5: Failed        12: 51234
6: password      13: ssh2
```

### 4. Negative indexing

```python
print(parts[-1])   # ssh2
print(parts[-4])   # 203.0.113.45
```

- Counts backward from the end of the list.
- Useful when the **end** of a line has a consistent format but the start varies.
- Weakness: if the log format changes, the position changes and your script silently grabs the wrong piece. Regex (Lesson 9) fixes this.

### 5. `.upper()`, `.lower()`, `.replace()`

```python
print(line.upper())
print(line.lower())
print(line.replace("Failed", "FAILED"))
```

- `.upper()` returns an all-capitals copy. `.lower()` returns an all-lowercase copy.
- `.replace(old, new)` returns a copy with every `old` swapped for `new`.
- **Important:** these return a *new* string. The original `line` does not change unless you save the result: `line = line.lower()`.
- SOC use: lowercase before comparing so `Admin`, `ADMIN`, and `admin` all match.

### 6. `len()` (length)

```python
print(len(line))
```

- Returns the number of characters in a string (or the number of items in a list).
- `len(parts)` would give `14`, the number of words.

### 7. `.strip()` (removing stray whitespace)

```python
print(len(line.strip()))
```

- Removes spaces, tabs, and newlines from the **start and end** of a string.
- Log lines read from files usually end with a hidden newline character, so `.strip()` shows up in almost every log-parsing script.
- Without it you get "why isn't this matching?" bugs caused by invisible characters.

### 8. f-strings

```python
print(f"User {username} tried to log in from {ip} on port {port}")
```

- The `f` before the opening quote turns on variable insertion.
- Inside `{}` goes the **name of a variable**, not the value itself.
- Wrong: `{203.0.113.45}` causes a `SyntaxError`. Right: `{ip}`.

---

## Errors you hit and what they mean

| Error | Cause | Fix |
|---|---|---|
| `SyntaxError: f-string: invalid syntax` | A value (like an IP) was typed inside `{}` instead of a variable name | Use variable names inside `{}` |
| `IndexError: list index out of range` | Asked for a position the list doesn't have | Check `len(parts)` and your position number |
| `NameError: name 'x' is not defined` | Used a variable before creating it, or misspelled it | Define it above the line that uses it |

How to read any Python error: look at the **last line** for the error type, and the **line number** above it for where to look.

---

## Interview-style explanation

> "Logs are text, so I treat each line as a string. I use `in` to filter for the events I care about, then `.split()` to break the line into a list of fields. I pull out the username, IP, and port by index. Positional parsing is quick, but it's fragile if the log format changes, so for production I'd use regex."

---

## Self-check questions

1. What does `parts[1]` print for the sample line, and why isn't it `Oct`?
2. What is the difference between `parts[-1]` and `parts[13]` on this line? When would they differ?
3. Why does `line.upper()` not change `line` itself?
4. Why does `{203.0.113.45}` fail inside an f-string?
5. Why would you call `.strip()` on a line read from a file?

Answers: `16` (counting starts at 0); nothing differs here, but they'd differ if the line had a different number of words; `.upper()` returns a new copy; the braces expect a variable name, not a value; files add hidden newline characters.

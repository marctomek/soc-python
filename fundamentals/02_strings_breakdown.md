# 02_strings.py: Line-by-Line Breakdown

Read this alongside `02_strings_notes.md` (terms and concepts). This file walks through the script itself, one line at a time, with the output each line produces.

---

## The script, step by step

### Line 1: store the log line

```python
line = "Oct 16 09:14:02 server sshd[1234]: Failed password for admin from 203.0.113.45 port 51234 ssh2"
```

- Creates a variable called `line` and puts the whole log entry inside it as a string.
- Nothing prints yet. This line only stores data.

### Check if text is inside the line

```python
print("Failed password" in line)
```

- `in` asks whether `"Failed password"` appears anywhere in `line`.
- **Output:** `True`
- This is the same filter you used in Lesson 1's log counter.

### Split the line into a list

```python
parts = line.split()
print(parts)
```

- `.split()` cuts the line at every space and returns a list of words, saved in `parts`.
- **Output:**

```
['Oct', '16', '09:14:02', 'server', 'sshd[1234]:', 'Failed', 'password', 'for', 'admin', 'from', '203.0.113.45', 'port', '51234', 'ssh2']
```

- Every later line uses this list, so it has to exist first.

### Grab items by position

```python
print(parts[0])
print(parts[5])
```

- Square brackets pick one item by its position. Counting starts at **0**.
- **Output:**

```
Oct
Failed
```

- `parts[0]` is the first item, and `parts[5]` is the sixth.

### Grab items from the end

```python
print(parts[-1])
print(parts[-4])
```

- Negative numbers count backward from the end. `-1` is last.
- **Output:**

```
ssh2
203.0.113.45
```

- `parts[-4]` lands on the IP because it is four items from the end: `ssh2` (-1), `51234` (-2), `port` (-3), IP (-4).

### Change the text

```python
print(line.upper())
print(line.lower())
print(line.replace("Failed", "FAILED"))
```

- `.upper()` makes everything capitals, `.lower()` makes everything lowercase, and `.replace(old, new)` swaps one piece of text for another.
- **Output:**

```
OCT 16 09:14:02 SERVER SSHD[1234]: FAILED PASSWORD FOR ADMIN FROM 203.0.113.45 PORT 51234 SSH2
oct 16 09:14:02 server sshd[1234]: failed password for admin from 203.0.113.45 port 51234 ssh2
Oct 16 09:14:02 server sshd[1234]: FAILED password for admin from 203.0.113.45 port 51234 ssh2
```

- Each one prints a **changed copy**. The variable `line` itself is unchanged.

### Measure the line

```python
print(len(line))
```

- `len()` counts the characters in the string.
- **Output:** `94`
- If you see `95`, there is a stray space inside your quotes. `.strip()` removes spaces at the ends.

---

## Your exercise code

### Pull out the three values

```python
username = parts[8]
ip = parts[10]
port = parts[12]
```

- Each line creates a variable from one item in the list.
- Positions come from the numbered list: `8` is `admin`, `10` is the IP, `12` is the port.
- These must come **before** the `print` that uses them, because Python reads top to bottom.

### Print the combined message

```python
print(f"User {username} tried to log in from {ip} on port {port}")
```

- The `f` turns on variable insertion, and `{}` holds variable **names**.
- **Output:**

```
User admin tried to log in from 203.0.113.45 on port 51234
```

---

## Full expected output

```
True
['Oct', '16', '09:14:02', 'server', 'sshd[1234]:', 'Failed', 'password', 'for', 'admin', 'from', '203.0.113.45', 'port', '51234', 'ssh2']
Oct
Failed
ssh2
203.0.113.45
OCT 16 09:14:02 SERVER SSHD[1234]: FAILED PASSWORD FOR ADMIN FROM 203.0.113.45 PORT 51234 SSH2
oct 16 09:14:02 server sshd[1234]: failed password for admin from 203.0.113.45 port 51234 ssh2
Oct 16 09:14:02 server sshd[1234]: FAILED password for admin from 203.0.113.45 port 51234 ssh2
94
admin
203.0.113.45
51234
User admin tried to log in from 203.0.113.45 on port 51234
```

---

## What the script does overall

1. Stores a raw log line as a string.
2. Confirms it is a failed login with `in`.
3. Breaks it into fields with `.split()`.
4. Extracts the username, source IP, and port by position.
5. Reports them in one readable sentence.

That is the basic shape of log parsing: **raw text in, structured fields out.**

---

## Limitation to remember

Position numbers only work while the log format stays the same. If a line has a different number of words (for example `Failed password for invalid user admin from ...`), `parts[8]` grabs the wrong word. Regex (Lesson 9) solves this by matching patterns instead of positions.

---

## Try it yourself

1. Change the log line to `... Failed password for invalid user test from 198.51.100.7 port 40022 ssh2`. Run the script. Which values are now wrong, and why?
2. Print how many items are in `parts` with `len(parts)`.
3. Print the hour only (`09`) by splitting `parts[2]` on the colon: `parts[2].split(":")[0]`.

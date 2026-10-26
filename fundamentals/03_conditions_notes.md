# Lesson 3 Notes: Conditions

Companion notes for `03_conditions.py`. Conditions let a script make decisions: do this if something is true, otherwise do that. This is the core of all detection logic.

Variables used throughout:

```python
failed_attempts = 7
threshold = 5
event_id = 4625
username = "admin"
```

---

## Core terms

| Term | Plain-English meaning | Example |
|---|---|---|
| **Condition** | A question Python answers with `True` or `False`. | `failed_attempts > threshold` |
| **Boolean** | A value that is either `True` or `False`. | `7 > 5` gives `True` |
| **Comparison operator** | A symbol that compares two values. | `>`, `<`, `==`, `!=` |
| **Logical operator** | A word that combines conditions. | `and`, `or` |
| **Block** | The group of indented lines that belong to an `if`. | The lines under `if ...:` |
| **Indentation** | Spaces at the start of a line. Python uses them to define blocks. | 4 spaces |
| **Threshold** | The number at which something becomes worth alerting on. | `threshold = 5` |
| **Severity** | A label for how serious something is. | LOW, MEDIUM, HIGH, CRITICAL |

---

## Comparison operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal to | `event_id == 4625` | `True` |
| `!=` | not equal to | `event_id != 4624` | `True` |
| `>` | greater than | `7 > 5` | `True` |
| `<` | less than | `7 < 5` | `False` |
| `>=` | greater than or equal to | `5 >= 5` | `True` |
| `<=` | less than or equal to | `7 <= 5` | `False` |

### `=` vs `==` (the most common beginner bug)

```python
event_id = 4625      # one equals sign STORES a value
event_id == 4625     # two equals signs COMPARE two values
```

- `=` is assignment: "put this value in this box."
- `==` is comparison: "are these two things equal?" It returns `True` or `False`.
- Using `=` inside an `if` (like `if event_id = 4625:`) causes a `SyntaxError`.

---

## What each part of the lesson does

### 1. `if` / `else`

```python
if failed_attempts > threshold:
    print("ALERT: possible brute force")
else:
    print("OK: below threshold")
```

- `if` checks the condition. If it is `True`, the indented lines under it run.
- `else` runs only when the `if` was `False`.
- The colon `:` at the end of the `if` and `else` lines is required.
- With `failed_attempts = 7` and `threshold = 5`, the condition is `True`, so it prints the ALERT line.
- SPL equivalent: `| where failed_attempts > 5`.

### 2. Indentation

- The indented lines (4 spaces) are the **block** that belongs to the `if`.
- Lines that are not indented run no matter what.
- Use the spacebar, not Tab, in TextEdit. Mixed spaces and tabs cause an `IndentationError`.

### 3. `elif` (checking several cases)

```python
if event_id == 4624:
    print("Successful logon")
elif event_id == 4625:
    print("Failed logon")
elif event_id == 4720:
    print("User account created")
else:
    print("Unknown event")
```

- `elif` means "else if." It checks the next condition only if the ones above were `False`.
- Python goes top to bottom and **stops at the first match**.
- `else` at the end is the catch-all for anything that matched nothing.
- Event IDs: 4624 is a successful logon, 4625 is a failed logon, 4720 is a user account created.
- SPL equivalent: `case()` inside `eval`.

### 4. `and` / `or`

```python
if failed_attempts > threshold and username == "admin":
    print("HIGH: brute force against admin account")

if username == "root" or username == "admin":
    print("Privileged account targeted")
```

- `and` needs **both** conditions to be true.
- `or` needs **at least one** to be true.
- Each side of `and` / `or` must be a full condition. `username == "root" or "admin"` looks right but is a bug. Write `username == "root" or username == "admin"`.
- `not` flips a condition: `not (username == "admin")` is the same as `username != "admin"`.

---

## Order matters in an elif chain

```python
failed_attempts = 25

if failed_attempts > 20:
    print("CRITICAL")
elif failed_attempts > 10:
    print("HIGH")
elif failed_attempts > 5:
    print("MEDIUM")
else:
    print("LOW")
```

- Check the **biggest** threshold first.
- If you start with `> 5`, then 25 matches immediately, prints MEDIUM, and Python never reaches CRITICAL.
- Test values on both sides of each boundary: 3, 8, 15, 25 for the ladder above.

---

## Errors and what they mean

| Error | Cause | Fix |
|---|---|---|
| `SyntaxError: invalid syntax` on an `if` line | Missing colon, or `=` used instead of `==` | Add `:` and use `==` to compare |
| `IndentationError: expected an indented block` | Nothing indented under the `if` | Indent the next line by 4 spaces |
| `IndentationError: unindent does not match` | Mixed spaces and tabs | Use spaces only |
| Wrong branch runs, no error | Conditions in the wrong order | Put the most specific or largest check first |

---

## Interview-style explanation

> "A detection is really just a condition. I count events, compare the count to a threshold with `if`, and use `elif` to assign severity levels, checking the highest first so a critical count isn't labeled medium. I combine conditions with `and` when I need context, like many failures against a privileged account. Choosing the threshold is the real work: too low causes false positives, too high misses attacks."

---

## Self-check questions

1. What is the difference between `=` and `==`?
2. In the `elif` chain with `event_id = 4625`, which branch prints, and why do the others not run?
3. With `failed_attempts = 7` and `username = "guest"`, does `failed_attempts > threshold and username == "admin"` print? Why or why not?
4. Why must the CRITICAL check come before the MEDIUM check?
5. What is wrong with `if username == "root" or "admin":`?

Answers: `=` stores, `==` compares; "Failed logon" prints because Python stops at the first match; no, because `and` needs both sides true and the username isn't admin; otherwise a high count would match the lower threshold first; `"admin"` on its own is always treated as true, so the condition is always true. Each side of `or` needs a full comparison.

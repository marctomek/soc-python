# 03_conditions.py: Line-by-Line Breakdown

Read this alongside `03_conditions_notes.md` (terms and concepts). This file walks through the script itself, one block at a time, with the output each block produces.

The starting values are `failed_attempts = 7`, `threshold = 5`, `event_id = 4625`, `username = "admin"`, and `country = "RU"`.

---

## Block 1: the first decision

```python
failed_attempts = 7
threshold = 5

if failed_attempts > threshold:
    print("ALERT: possible brute force")
else:
    print("OK: below threshold")
```

- `failed_attempts = 7` and `threshold = 5` store two integers.
- `if failed_attempts > threshold:` asks "is 7 greater than 5?" The answer is `True`.
- Because it is `True`, the indented `print` under the `if` runs. The `else` block is skipped.
- The colon at the end of `if` and `else` is required, and the 4-space indentation marks which lines belong to each branch.
- **Output:** `ALERT: possible brute force`
- If you set `failed_attempts = 3`, the condition is `False` and the `else` runs, so the output is `OK: below threshold`.

---

## Block 2: the elif chain

```python
event_id = 4625

if event_id == 4624:
    print("Successful logon")
elif event_id == 4625:
    print("Failed logon")
elif event_id == 4720:
    print("User account created")
else:
    print("Unknown event")
```

- `event_id = 4625` stores a number. It has **no quotes**, which matters: `"4625"` as text would never equal the number `4625`.
- Python checks the conditions **top to bottom** and stops at the first `True` one.
- `4625 == 4624` is `False`, so it moves on. `4625 == 4625` is `True`, so it prints and skips everything below.
- `else` catches anything that matched none of the cases.
- **Output:** `Failed logon`
- Try `event_id = 9999`. All three comparisons are `False`, so `else` runs and prints `Unknown event`.

---

## Block 3: combining conditions

```python
username = "admin"

if failed_attempts > threshold and username == "admin":
    print("HIGH: brute force against admin account")

if username == "root" or username == "admin":
    print("Privileged account targeted")
```

**First `if` (with `and`):**
- Both sides must be `True`: `7 > 5` is `True`, and `username == "admin"` is `True`.
- Both are `True`, so it prints `HIGH: brute force against admin account`.

**Second `if` (with `or`):**
- At least one side must be `True`. `username == "root"` is `False`, but `username == "admin"` is `True`.
- One side is enough, so it prints `Privileged account targeted`.

These are two separate `if` statements, not one chain, so **both** are checked and both can print.

- **Output:**

```
HIGH: brute force against admin account
Privileged account targeted
```

- Change `username` to `"guest"` and neither line prints.

---

## Block 4: the watchlist check (your exercise)

```python
country = "RU"

if country == "RU" or country == "CN":
    print("Review: login from watchlist country")
else:
    print("Normal")
```

- `country = "RU"` stores text, so it needs quotes.
- Each side of `or` is a full comparison. `country == "RU" or "CN"` would look right but is a bug, because `"CN"` alone is always treated as true.
- `"RU" == "RU"` is `True`, so the first `print` runs.
- **Output:** `Review: login from watchlist country`
- Change `country` to `"US"` and both comparisons are `False`, so it prints `Normal`.

---

## Block 5: the severity ladder (your exercise)

```python
if failed_attempts > 20:
    print("CRITICAL")
elif failed_attempts > 10:
    print("HIGH")
elif failed_attempts > 5:
    print("MEDIUM")
else:
    print("LOW")
```

- Python walks down the ladder and stops at the first `True` check.
- With `failed_attempts = 7`: `7 > 20` is `False`, `7 > 10` is `False`, `7 > 5` is `True`, so it prints `MEDIUM`.
- The biggest threshold goes first. If `> 5` came first, then 25 would match it immediately and print `MEDIUM`, and CRITICAL would never be reached.

Results you tested:

| `failed_attempts` | Label |
|---|---|
| 3 | LOW |
| 7 | MEDIUM |
| 8 | MEDIUM |
| 15 | HIGH |
| 25 | CRITICAL |

Note that 5 itself gives `LOW`, because `5 > 5` is `False`. Use `>=` if you want 5 to count.

---

## Full expected output (with the starting values)

```
ALERT: possible brute force
Failed logon
HIGH: brute force against admin account
Privileged account targeted
Review: login from watchlist country
MEDIUM
```

With `failed_attempts = 3` you saw:

```
OK: below threshold
Failed logon
Privileged account targeted
Review: login from watchlist country
LOW
```

The HIGH line disappeared because `3 > 5` is `False`, so the `and` check failed.

---

## What the script does overall

1. Compares a count to a threshold and decides whether to alert.
2. Translates an event ID into a human-readable meaning.
3. Combines conditions to add context (many failures **and** a privileged account).
4. Flags a country from a watchlist.
5. Assigns a severity level from a count.

Together, that is a small detection engine: **data in, decision out.**

---

## Bugs you ran into and what they taught

| Problem | Cause | Lesson |
|---|---|---|
| `SyntaxError` on `If` | Capital `I` (TextEdit auto-capitalized it) | Python keywords are lowercase and case-sensitive |
| `Unknown event` instead of `Failed logon` | The event ID had quotes, making it a string | `"4625"` and `4625` are different, so match your types |

---

## Limitation to remember

This script only checks **one** set of values. Real logs have thousands of lines, each with a different IP and count. Loops (Lesson 4) let you run these same decisions over a whole list automatically.

---

## Try it yourself

1. Change the ladder so that exactly 5 failures counts as MEDIUM. Which symbol changes?
2. Add a second watchlist country of your choice. Where does it go?
3. Add an `elif` to Block 2 for event ID `4672` (special privileges assigned) that prints `"Privileged logon"`.

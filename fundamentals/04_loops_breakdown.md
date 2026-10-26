# 04_loops.py: Line-by-Line Breakdown

Read this alongside `04_loops_notes.md` (terms and concepts). This file walks through the script itself, one block at a time, with the output each block produces.

---

## Block 1: your first loop

```python
ips = ["203.0.113.45", "198.51.100.7", "192.0.2.10"]

for ip in ips:
    print("Checking", ip)
```

- `ips` is a **list**: three strings in square brackets, separated by commas.
- `for ip in ips:` runs the indented line once per item. On each pass, `ip` holds the current address.
- The list has to be created **above** the loop, because Python reads top to bottom. A missing or misspelled list gives `NameError: name 'attempts' is not defined`, the error you hit.
- **Output:**

```
Checking 203.0.113.45
Checking 198.51.100.7
Checking 192.0.2.10
```

---

## Block 2: a loop with a decision inside

```python
attempts = [3, 8, 15, 25]

for count in attempts:
    if count > 20:
        print(count, "CRITICAL")
    elif count > 10:
        print(count, "HIGH")
    elif count > 5:
        print(count, "MEDIUM")
    else:
        print(count, "LOW")
```

- The list holds **integers** (no quotes), so comparisons like `count > 20` work.
- The `if/elif/else` ladder from Lesson 3 now runs once per number.
- Indentation has two levels: 4 spaces under `for`, and 8 spaces under each `if`, `elif`, and `else`.
- **Output:**

```
3 LOW
8 MEDIUM
15 HIGH
25 CRITICAL
```

- Trace one pass: for `15`, `15 > 20` is `False`, `15 > 10` is `True`, so it prints `15 HIGH` and skips the rest.

---

## Block 3: counting log lines

```python
log_lines = [
    "Failed password for admin from 203.0.113.45",
    "Accepted password for bob from 198.51.100.7",
    "Failed password for root from 203.0.113.45",
    "Accepted password for admin from 192.0.2.10",
]

failed_count = 0
accepted_count = 0

for line in log_lines:
    if "Failed password" in line:
        failed_count = failed_count + 1
    elif "Accepted password" in line:
        accepted_count = accepted_count + 1

print("Total failed logins:", failed_count)
print("Total accepted logins:", accepted_count)
```

- Each item in `log_lines` is a string, with a comma after it. A missing comma would join two lines into one string.
- Both counters start at **0** before the loop. If they were created inside it, they would reset on every pass.
- `if "Failed password" in line:` is true when that exact text appears in the line.
- `elif` only checks lines that **weren't** failures, which is correct because each line is one kind of event.
- `failed_count = failed_count + 1` reads the current value, adds 1, and stores it back.
- The two `print` lines have **no indentation**, so they run once, after the loop finishes.

Trace of the loop:

| Pass | `line` starts with | Matches | Counters after |
|---|---|---|---|
| 1 | Failed password for admin | `if` | failed 1, accepted 0 |
| 2 | Accepted password for bob | `elif` | failed 1, accepted 1 |
| 3 | Failed password for root | `if` | failed 2, accepted 1 |
| 4 | Accepted password for admin | `elif` | failed 2, accepted 2 |

- **Output:**

```
Total failed logins: 2
Total accepted logins: 2
```

### The bugs you found here

| Bug | What happened | Lesson |
|---|---|---|
| `"Failed pasword"` in the data | Only one failure matched, so the total was 1 | A typo in the data or the search text causes a wrong count, not an error |
| `"accepted password"` in the check | Never matched `Accepted`, so the accepted total was 0 | `in` is case-sensitive, so match the case or use `line.lower()` |

---

## Block 4: `range`

```python
for number in range(1, 6):
    print(number)
```

- `range(1, 6)` starts at 1 and stops **before** 6.
- `number` holds each value in turn.
- **Output:**

```
1
2
3
4
5
```

- Earlier, `range(3)` printed `0 1 2`. With one number, counting starts at 0.

---

## Block 5: loop over usernames

```python
usernames = ["admin", "root", "guest", "bob"]

for name in usernames:
    if name == "admin" or name == "root":
        print(name, "Privileged account")
    else:
        print(name, "Standard account")
```

- A list of four strings, looped one at a time.
- `or` joins two full comparisons. Either match makes the `if` true.
- Anything that isn't `admin` or `root` falls through to the `else`.
- **Output:**

```
admin Privileged account
root Privileged account
guest Standard account
bob Standard account
```

- The earlier bug here was `name == "bob"` where `"root"` belonged. The output showed the wrong labels, and working back from them led to the line.

---

## Full expected output

```
Checking 203.0.113.45
Checking 198.51.100.7
Checking 192.0.2.10
3 LOW
8 MEDIUM
15 HIGH
25 CRITICAL
Total failed logins: 2
Total accepted logins: 2
1
2
3
4
5
admin Privileged account
root Privileged account
guest Standard account
bob Standard account
```

---

## What the script does overall

1. Repeats an action for every item in a list.
2. Applies the severity ladder to many values at once.
3. Counts two kinds of log events in a single pass.
4. Generates number sequences with `range`.
5. Classifies a list of accounts.

That is the core of log analysis: **many events in, a small summary out.**

---

## Limitation to remember

The data is typed into the script. Real logs live in files and have thousands of lines. Lesson 7 reads a file line by line with the same loop. Before that, Lesson 5 covers lists properly, and Lesson 6 adds dictionaries, so you can count events **per IP** instead of just in total.

---

## Try it yourself

1. Add a third counter for lines that are neither failed nor accepted, using `else`. Add a line like `"Connection closed by 192.0.2.10"` to test it.
2. Print the position of each log line (1, 2, 3, 4) next to the line itself. Hint: use `range(len(log_lines))` and `log_lines[number]`.
3. Make the checks case-insensitive with `line.lower()`, and test with a line that says `"FAILED PASSWORD for test from 192.0.2.99"`.

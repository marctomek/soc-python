# Lesson 4 Notes: Loops

Companion notes for `04_loops.py`. A loop repeats the same block of code once for each item in a collection. This is how a script handles a log with thousands of lines.

---

## Core terms

| Term | Plain-English meaning | Example |
|---|---|---|
| **Loop** | Code that repeats. | `for ip in ips:` |
| **`for` loop** | Runs a block once per item in a collection. | `for line in log_lines:` |
| **Iteration** | One pass through the loop. | The first pass handles the first item |
| **Loop variable** | The stand-in that holds the current item. You choose its name. | `ip`, `count`, `line`, `name` |
| **List** | An ordered collection of items in square brackets. | `["admin", "root", "guest"]` |
| **Counter** | A variable that starts at 0 and goes up on each match. | `failed_count = 0` |
| **`range()`** | A function that produces a sequence of numbers. | `range(1, 6)` gives 1 to 5 |
| **Nested block** | A block inside another block, indented further. | An `if` inside a `for` |
| **Accumulator pattern** | Start a counter, loop, filter with `if`, increment on a match. | The log counter |

---

## What each part does

### 1. The basic `for` loop

```python
ips = ["203.0.113.45", "198.51.100.7", "192.0.2.10"]

for ip in ips:
    print("Checking", ip)
```

- `for ip in ips:` means "for each item in `ips`, call it `ip` and run the indented lines."
- On pass 1, `ip` holds the first address. On pass 2, the second. On pass 3, the third.
- The loop ends by itself when the list runs out.
- The colon at the end of the `for` line is required.
- **Output:** three `Checking` lines, one per address.

### 2. A loop with a decision inside

```python
for count in attempts:
    if count > 20:
        print(count, "CRITICAL")
    elif count > 10:
        print(count, "HIGH")
    ...
```

- The `if/elif/else` from Lesson 3 now runs once per item.
- Two levels of indentation: 4 spaces under `for`, 8 spaces under `if`.
- Each value in the list is checked against the whole ladder, and the biggest threshold still goes first.

### 3. The counting pattern

```python
failed_count = 0

for line in log_lines:
    if "Failed password" in line:
        failed_count = failed_count + 1

print("Total failed logins:", failed_count)
```

1. Start a counter at **0**, before the loop.
2. Loop through every line.
3. Filter with `if`, using `in` to check for text.
4. Add 1 to the counter on each match.
5. Print the total **after** the loop (not indented), so it prints once.

This is the same structure as your original Lesson 1 log counter. `failed_count = failed_count + 1` can also be written `failed_count += 1`.

### 4. `elif` for a second counter

```python
elif "Accepted password" in line:
    accepted_count = accepted_count + 1
```

- Each line is either a failure, a success, or neither, so `elif` only checks lines that weren't failures.
- Each counter needs its own `= 0` before the loop.

### 5. `range()`

```python
for number in range(1, 6):
    print(number)
```

| Call | Produces |
|---|---|
| `range(3)` | 0, 1, 2 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(2, 10, 2)` | 2, 4, 6, 8 |

- **First number:** where counting starts (included). With only one number, the start defaults to 0.
- **Second number:** where it stops (**not** included).
- **Third number (optional):** the step, meaning how much to count by.

---

## Where the final `print` goes

```python
# Prints once, after the loop (correct)
for line in log_lines:
    ...
print("Total:", failed_count)

# Prints once per line (usually a mistake)
for line in log_lines:
    ...
    print("Total:", failed_count)
```

Indentation decides whether a line is inside the loop or after it.

---

## Errors and what they mean

| Problem | Cause | Fix |
|---|---|---|
| `NameError: name 'attempts' is not defined` | The list is missing, misspelled, or below the loop | Create it above the `for` line, and match the spelling |
| Count is too low, no error | Text in the check doesn't match exactly (`pasword`, `accepted` vs `Accepted`) | Compare spelling and capitalization, or use `line.lower()` |
| Wrong label for some items | A wrong value in the condition (`"bob"` instead of `"root"`) | Work back from the wrong output to the line that caused it |
| Total prints on every pass | The `print` is indented inside the loop | Move it back to the left margin |
| `IndentationError` | Wrong number of spaces under `for`, `if`, or `else` | Count the spaces and use the spacebar, not Tab |

---

## Debugging trick

Print inside the loop to see what the script sees:

```python
for line in log_lines:
    print(line)
    if "Failed password" in line:
        failed_count = failed_count + 1
```

Remove the extra `print` once you've found the problem.

---

## Interview-style explanation

> "A `for` loop lets me run the same check against every item in a collection. My basic log counter starts a counter at zero, loops through each line, uses `if` to match on a pattern like 'Failed password,' and increments on each match. Exact text matching is brittle, so I normalize with `.lower()`, because a one-character difference silently gives a wrong count."

---

## Self-check questions

1. In `for ip in ips:`, what does `ip` hold on each pass?
2. Why does the counter start at 0 **before** the loop?
3. What does `range(1, 6)` print, and why isn't 6 included?
4. Why use `elif` instead of a second `if` for the accepted-password check?
5. Why does a typo in the search text cause a wrong count and not an error?

Answers: one item at a time, the first on pass 1, the second on pass 2, and so on; because a counter created inside the loop would reset to 0 on every pass; 1, 2, 3, 4, 5, because the stop number is excluded; each line is only one kind of event, so `elif` only checks lines that weren't failures; a check that never matches is valid Python, so it just never runs the code under it.

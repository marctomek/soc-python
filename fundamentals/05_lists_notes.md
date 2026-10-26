# Lesson 5 Notes: Lists

Companion notes for `05_lists.py`. A list is one variable that holds several items, like a row of numbered boxes. In SOC scripts, lists are how you collect results: flagged IPs, matching log lines, high counts.

---

## Core terms

| Term | Plain-English meaning | Example |
|---|---|---|
| **List** | An ordered collection of items in square brackets, separated by commas. | `["203.0.113.45", "192.0.2.10"]` |
| **Item / element** | One value inside a list. | `"203.0.113.45"` |
| **Index** | An item's position number. Counting starts at 0. | `ips[0]` is the first item |
| **Negative index** | Counts from the end. `-1` is last. | `ips[-1]` |
| **Empty list** | A list with nothing in it, written `[]`. | `flagged = []` |
| **Method** | An action attached to a value, written with a dot. | `ips.append(...)` |
| **In place** | Changes the original list instead of making a copy. | `.sort()`, `.append()`, `.remove()` |
| **Slice** | A range of items: start included, stop excluded. | `attempts[0:2]` |
| **Tuple** | A fixed pair or group in parentheses. | `("203.0.113.45", 12)` |
| **Unpacking** | Splitting a tuple into separate variables. | `for ip, count in events:` |
| **Duplicate** | The same value appearing more than once. | `203.0.113.45` listed twice |

---

## Reading a list

```python
ips = ["203.0.113.45", "198.51.100.7", "192.0.2.10"]

print(ips)        # the whole list
print(ips[0])     # first item
print(ips[1])     # second item
print(ips[-1])    # last item
print(len(ips))   # number of items
```

- Items are in order, and each has a position starting at **0**. This is the same rule as `parts[0]` with strings.
- `len()` counts the items, so a list with positions 0, 1, 2 has length 3.
- Asking for a position that doesn't exist (like `ips[10]`) causes an `IndexError`.

---

## Changing a list

| Code | What it does |
|---|---|
| `ips.append("198.51.100.99")` | Adds one item to the **end** |
| `ips.remove("198.51.100.7")` | Deletes the first item matching that **value** |
| `"192.0.2.10" in ips` | Gives `True` or `False` |
| `"10.0.0.1" not in ips` | `True` when the item is missing |

- `.append()` adds one item at a time, always at the end.
- `.remove()` takes a **value**, not a position. If the value isn't in the list, you get a `ValueError`, so check with `in` first when you're not sure.
- `in` is the same word you used on strings. Here it checks list membership, which is how a script tests an IP against a watchlist.

---

## Sorting, counting, and slicing

```python
attempts = [15, 3, 25, 8, 3]

attempts.sort()           # [3, 3, 8, 15, 25]
attempts.count(3)         # 2
attempts[0:2]             # [3, 3]
max(attempts)             # 25
min(attempts)             # 3
```

- `.sort()` rearranges the list **in place**, smallest to largest. The original order is lost. `sorted(attempts)` returns a new sorted list and leaves the original alone.
- `.sort(reverse=True)` sorts largest to smallest.
- `.count(x)` says how many times `x` appears.
- A slice `[0:2]` starts at position 0 and stops **before** position 2, so it returns two items. This is the same start-included, stop-excluded rule as `range(1, 6)`.
- `max()` and `min()` return the largest and smallest values.

---

## The collecting pattern (the main SOC use)

```python
flagged = []

for ip in ips:
    if ip == "203.0.113.45":
        flagged.append(ip)

print("Flagged:", flagged)
```

1. Create an **empty list** before the loop.
2. Loop through the data.
3. Test each item with `if`.
4. `.append()` the ones that match.
5. Use the list after the loop.

The empty list has to exist before the loop. If it's created inside, it resets on every pass, and if it doesn't exist at all you get a `NameError`.

---

## Pairs and avoiding duplicates

```python
events = [
    ("203.0.113.45", 12),
    ("198.51.100.7", 2),
    ("192.0.2.10", 9),
    ("203.0.113.45", 15),
]

flagged = []

for ip, count in events:
    if count > 5:
        if ip not in flagged:
            flagged.append(ip)
```

- Each item is a **tuple**: an IP and a count in parentheses.
- `for ip, count in events:` **unpacks** each pair into two variables on every pass.
- `if count > 5:` keeps only the busy IPs.
- `if ip not in flagged:` prevents duplicates, so `203.0.113.45` is added once even though it appears twice.
- **Result:** `['203.0.113.45', '192.0.2.10']`

---

## Errors and what they mean

| Problem | Cause | Fix |
|---|---|---|
| `IndexError: list index out of range` | Asked for a position that doesn't exist | Check `len()` and remember positions start at 0 |
| `ValueError: list.remove(x): x not in list` | Removed a value that isn't there | Check with `in` first |
| `NameError: name 'flagged' is not defined` | The empty list wasn't created before the loop | Add `flagged = []` above the `for` line |
| List becomes `None` | Wrote `ips = ips.append("x")` | Call `.append()` on its own line, without assigning |
| Duplicates in results | No `not in` check before appending | Add `if ip not in flagged:` |
| Terminal shows a `>` prompt | Python code typed into Terminal | Press Ctrl+C. Code goes in the `.py` file, Terminal only runs it |

---

## Interview-style explanation

> "A list holds an ordered group of items. I read by position, add with append, remove by value, and test membership with `in`. In SOC scripts I start with an empty list, loop through events, and append anything that meets a condition, like IPs over a failure threshold. I check `not in` before appending so I don't report the same IP twice."

---

## Self-check questions

1. What does `ips[-1]` return, and what does `len(ips)` return for a 3-item list?
2. Why must `flagged = []` come before the loop?
3. What is the difference between `.sort()` and `sorted()`?
4. What does `attempts[0:2]` return, and why isn't position 2 included?
5. Why does `ip not in flagged` matter in the pairs example?

Answers: the last item, and `3`; so the list isn't reset on every pass or missing entirely; `.sort()` changes the original and `sorted()` returns a new list; the first two items, because the stop position is excluded; it stops the same IP being appended twice.

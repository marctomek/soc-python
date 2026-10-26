# 05_lists.py: Line-by-Line Breakdown

Read this alongside `05_lists_notes.md` (terms and concepts). This file walks through the script as you ran it, one block at a time, with the output each block produced.

---

## Block 1: create and read a list

```python
ips = ["203.0.113.45", "198.51.100.7", "192.0.2.10"]
print(ips)
print(ips[0])
print(ips[1])
print(ips[-1])
print(len(ips))
```

- `ips` is a **list**: three strings inside `[ ]`, separated by commas.
- `print(ips)` shows the whole list, brackets and quotes included.
- `ips[0]`, `ips[1]`, `ips[-1]` pick single items by position. Counting starts at 0, and `-1` is the last item.
- `len(ips)` counts the items.
- **Output:**

```
['203.0.113.45', '198.51.100.7', '192.0.2.10']
203.0.113.45
198.51.100.7
192.0.2.10
3
```

---

## Block 2: add an item

```python
ips.append("198.51.100.99")
print(ips)
print(len(ips))
```

- `.append()` adds one item to the **end** of the list and changes the original list.
- The length goes from 3 to 4.
- **Output:**

```
['203.0.113.45', '198.51.100.7', '192.0.2.10', '198.51.100.99']
4
```

---

## Block 3: remove an item

```python
ips.remove("198.51.100.7")
print(ips)
print(len(ips))
```

- `.remove()` deletes the first item whose **value** matches. You give it the value, not a position.
- If the value isn't in the list, Python raises a `ValueError`.
- **Output:**

```
['203.0.113.45', '192.0.2.10', '198.51.100.99']
3
```

---

## Block 4: check membership

```python
print("192.0.2.10" in ips)
print("10.0.0.1" in ips)
```

- `in` asks "is this value in the list?" and answers `True` or `False`.
- This is how a script checks an IP against a watchlist.
- **Output:**

```
True
False
```

---

## Block 5: collect matches into an empty list

```python
flagged = []

for ip in ips:
    if ip == "203.0.113.45":
        flagged.append(ip)

print("Flagged:", flagged)
```

- `flagged = []` creates an empty list **before** the loop. If it were created inside, it would reset on each pass.
- The loop visits each IP, and the `if` lets only matching ones through to `.append()`.
- The `print` has no indentation, so it runs once, after the loop.
- **Output:** `Flagged: ['203.0.113.45']`

This is the main SOC pattern for lists: start empty, loop, test, append.

---

## Block 6: sort, count, slice, max, min

```python
attempts = [15, 3, 25, 8, 3]
attempts.sort()
print(attempts)
print(attempts.count(3))
print(attempts[0:2])
print(max(attempts))
print(min(attempts))
```

- `.sort()` reorders the list **in place**, smallest to largest. The original order is gone.
- `.count(3)` counts how many times `3` appears. It appears twice.
- `attempts[0:2]` is a slice: start at position 0, stop **before** position 2, so two items.
- `max()` and `min()` return the largest and smallest values.
- **Output:**

```
[3, 3, 8, 15, 25]
2
[3, 3]
25
3
```

---

## Block 7: pairs and duplicates

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

print("Flagged IPs:", flagged)
```

- Each item is a **tuple**: an IP and a count in parentheses.
- `for ip, count in events:` splits each pair into two variables on every pass.
- `flagged = []` resets the list, so this block starts clean.
- `if count > 5:` keeps only the busy IPs.
- `if ip not in flagged:` prevents the same IP being added twice.

Trace of the loop:

| Pass | `ip` | `count` | `count > 5` | Already in `flagged` | Result |
|---|---|---|---|---|---|
| 1 | 203.0.113.45 | 12 | Yes | No | Added |
| 2 | 198.51.100.7 | 2 | No | n/a | Skipped |
| 3 | 192.0.2.10 | 9 | Yes | No | Added |
| 4 | 203.0.113.45 | 15 | Yes | Yes | Skipped (duplicate) |

- **Output:** `Flagged IPs: ['203.0.113.45', '192.0.2.10']`

---

## Full expected output

```
['203.0.113.45', '198.51.100.7', '192.0.2.10']
203.0.113.45
198.51.100.7
192.0.2.10
3
['203.0.113.45', '198.51.100.7', '192.0.2.10', '198.51.100.99']
4
['203.0.113.45', '192.0.2.10', '198.51.100.99']
3
True
False
Flagged: ['203.0.113.45']
[3, 3, 8, 15, 25]
2
[3, 3]
25
3
Flagged IPs: ['203.0.113.45', '192.0.2.10']
```

---

## What the script does overall

1. Builds a list and reads items by position.
2. Adds and removes items, and checks membership.
3. Collects matching items into an empty list inside a loop.
4. Sorts, counts, and slices numbers.
5. Flags busy IPs from pairs without reporting duplicates.

That is the core of turning raw events into a short list an analyst can act on.

---

## Bugs and slips you hit

| Problem | What happened | Lesson |
|---|---|---|
| `ips.remove(...)` typed into Terminal, `>` prompt appeared | Python code went into the shell, with an unclosed quote and bracket | Code goes in the `.py` file. Terminal only runs the file. Press Ctrl+C to escape |

---

## Limitation to remember

A list can tell you **which** IPs crossed a threshold, but only if you already have the counts. To count events per IP from raw log lines, you need a dictionary, which is Lesson 6.

---

## Still to do: the four exercises

1. **Watchlist match.** `watchlist = ["203.0.113.45", "192.0.2.99"]`. Loop through `ips` and print `MATCH` plus the IP for any address also in `watchlist`.
2. **Big counts.** Start with an empty `big_counts` list. Loop through `attempts` and append only values above 10.
3. **How many flagged.** Print `len(flagged)`.
4. **Reverse sort.** Sort `ips` with `.sort(reverse=True)`. Predict the order first.

# 06_dictionaries.py: Line-by-Line Breakdown

Read this alongside `06_dictionaries_notes.md` (terms and concepts). This file walks through the script as you ran it, one block at a time, with the output each block produced.

---

## Block 1: make a dictionary and read from it

```python
counts = {"203.0.113.45": 12, "198.51.100.7": 2}

print(counts)
print(counts["203.0.113.45"])
```

- `counts` is a **dictionary**: two key-value pairs inside `{ }`.
- Each key is an IP string, and each value is an integer count.
- `print(counts)` shows the whole dictionary.
- `counts["203.0.113.45"]` looks up that key and returns its value.
- **Output:**

```
{'203.0.113.45': 12, '198.51.100.7': 2}
12
```

---

## Block 2: add and change entries

```python
counts["192.0.2.10"] = 9
counts["198.51.100.7"] = counts["198.51.100.7"] + 1

print(counts)
```

- Line 1 uses a new key, so it **adds** an entry.
- Line 2 uses an existing key, so it **replaces** the value. It reads the current value (2), adds 1, and stores 3.
- **Output:**

```
{'203.0.113.45': 12, '198.51.100.7': 3, '192.0.2.10': 9}
```

---

## Block 3: check for keys

```python
print("203.0.113.45" in counts)
print("10.0.0.1" in counts)
```

- `in` checks the **keys** and answers `True` or `False`.
- The first IP is a key and the second is not.
- **Output:**

```
True
False
```

---

## Block 4: count from log data

```python
log_ips = ["203.0.113.45", "198.51.100.7", "203.0.113.45", "203.0.113.45"]

failed = {}

for ip in log_ips:
    if ip not in failed:
        failed[ip] = 0
    failed[ip] = failed[ip] + 1

print(failed)
```

- `log_ips` is a **list** of the IPs that appeared in failed-login lines.
- `failed = {}` creates an empty dictionary **before** the loop. Created inside, it would reset each pass.
- `if ip not in failed:` is true the first time an IP is seen, so it gets a starting count of 0.
- `failed[ip] = failed[ip] + 1` then adds 1 for this sighting.
- The `print` has no indentation, so it runs once, after the loop.

Trace of the loop:

| Pass | `ip` | New? | `failed` after |
|---|---|---|---|
| 1 | 203.0.113.45 | Yes | `{'203.0.113.45': 1}` |
| 2 | 198.51.100.7 | Yes | `{'203.0.113.45': 1, '198.51.100.7': 1}` |
| 3 | 203.0.113.45 | No | `{'203.0.113.45': 2, '198.51.100.7': 1}` |
| 4 | 203.0.113.45 | No | `{'203.0.113.45': 3, '198.51.100.7': 1}` |

- **Output:**

```
{'203.0.113.45': 3, '198.51.100.7': 1}
```

---

## Block 5: loop over the dictionary

```python
for ip in failed:
    print(ip, failed[ip])

for ip, count in failed.items():
    if count > 2:
        print("Alert", ip, count)
```

- The first loop goes through the **keys**, and `failed[ip]` looks up each one's value.
- The second loop uses `.items()` to get the key and value together, split into `ip` and `count`.
- The `if count > 2` check keeps only the IPs over the threshold, so it acts as a detection.
- **Output:**

```
203.0.113.45 3
198.51.100.7 1
Alert 203.0.113.45 3
```

- Your text said `Alert` where the lesson had `ALERT`. The words in quotes print exactly as typed, so both are valid.

---

## Full expected output

```
{'203.0.113.45': 12, '198.51.100.7': 2}
12
{'203.0.113.45': 12, '198.51.100.7': 3, '192.0.2.10': 9}
True
False
{'203.0.113.45': 3, '198.51.100.7': 1}
203.0.113.45 3
198.51.100.7 1
Alert 203.0.113.45 3
```

---

## What the script does overall

1. Stores values under names with a dictionary.
2. Adds and updates entries.
3. Checks for a key before using it.
4. Builds a per-IP tally from a list of events.
5. Loops through the tally and flags IPs over a threshold.

That is a miniature brute-force detector: **events in, counts per source out, alerts on the busy ones.**

---

## How it connects to your earlier work

Your original `lesson2.py` did exactly this: it looped through `auth.log`, picked out the IP from each failed-login line, kept counts in a dictionary, and alerted above a threshold of 5. Block 4 and Block 5 are that logic, and you can now read every line of it.

---

## Limitation to remember

The IPs are typed into a list here. A real detector reads lines from a file and pulls the IP out of each one, which is Lesson 7 (files) and Lesson 9 (regex). The counting itself stays the same.

---

## Still to do: the four exercises

1. **Count usernames.** Build `user_counts` from `["admin", "root", "admin", "guest", "admin", "root"]` using the Block 4 pattern. Expect admin 3, root 2, guest 1.
2. **Find the top offender.** Loop through `failed.items()` and track the highest count with `top_ip` and `top_count`.
3. **The `.get()` shortcut.** Build `failed2` with `failed2.get(ip, 0) + 1` and compare to Block 4. Explain what `.get(ip, 0)` returns the first time an IP is seen.
4. **Severity per IP.** Print `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW` for each IP in `failed.items()`, biggest threshold first.

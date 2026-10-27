# Lesson 6 Notes: Dictionaries

Companion notes for `06_dictionaries.py`. A dictionary stores values under names (keys) instead of positions. In SOC scripts, it is the tool for "how many events per IP, per user, per host?"

---

## Core terms

| Term | Plain-English meaning | Example |
|---|---|---|
| **Dictionary** | A collection of key-value pairs in curly braces. | `{"203.0.113.45": 12}` |
| **Key** | The name you look things up by. Must be unique. | `"203.0.113.45"` |
| **Value** | The data stored under a key. | `12` |
| **Key-value pair** | One entry: a key and its value, joined by a colon. | `"198.51.100.7": 2` |
| **Lookup** | Getting a value by its key, with square brackets. | `counts["203.0.113.45"]` |
| **Empty dictionary** | A dictionary with no entries, written `{}`. | `failed = {}` |
| **`.items()`** | Gives each key and value together, for looping. | `for ip, count in failed.items():` |
| **`.get()`** | Looks up a key and returns a default if it's missing. | `failed.get(ip, 0)` |
| **`KeyError`** | The error when you look up a key that doesn't exist. | `counts["10.0.0.1"]` |
| **Tally / frequency count** | A dictionary that counts how often each item appears. | Failed logins per IP |

---

## List vs dictionary

| | List | Dictionary |
|---|---|---|
| Brackets | `[ ]` | `{ }` |
| Look up by | Position (`ips[0]`) | Key (`counts["203.0.113.45"]`) |
| Good for | An ordered group of items | Pairing a name with a value |
| SOC use | Flagged IPs | Count per IP |

---

## What each part does

### 1. Make one and read from it

```python
counts = {"203.0.113.45": 12, "198.51.100.7": 2}

print(counts)
print(counts["203.0.113.45"])
```

- Each entry is `key: value`, and entries are separated by commas.
- Square brackets with a key return the value stored there, so the second line prints `12`.
- Keys are unique. Writing the same key twice keeps only the last value.

### 2. Add and change entries

```python
counts["192.0.2.10"] = 9
counts["198.51.100.7"] = counts["198.51.100.7"] + 1
```

- Assigning to a key that **doesn't exist** adds a new entry.
- Assigning to a key that **does exist** replaces its value.
- The second line reads the current value, adds 1, and stores it back, the same as `failed_count = failed_count + 1` with a single counter.

### 3. Check whether a key exists

```python
print("203.0.113.45" in counts)   # True
print("10.0.0.1" in counts)       # False
```

- `in` checks the **keys**, not the values.
- Looking up a missing key with `[ ]` crashes with a `KeyError`, so check with `in` first, or use `.get()`.

### 4. Counting from log data (the main use)

```python
log_ips = ["203.0.113.45", "198.51.100.7", "203.0.113.45", "203.0.113.45"]

failed = {}

for ip in log_ips:
    if ip not in failed:
        failed[ip] = 0
    failed[ip] = failed[ip] + 1
```

1. Start with an **empty dictionary** before the loop.
2. For each IP, if it hasn't been seen, create its entry with a count of 0.
3. Add 1 to that IP's count.
4. When the loop ends, `failed` holds the count for every IP.

- **Result:** `{'203.0.113.45': 3, '198.51.100.7': 1}`
- The `if ip not in failed` check is what prevents a `KeyError` on the first sighting of each IP.

### 5. Looping over a dictionary

```python
for ip in failed:
    print(ip, failed[ip])

for ip, count in failed.items():
    if count > 2:
        print("ALERT", ip, count)
```

- Looping directly gives you the **keys**.
- `.items()` gives the key and value together, and `for ip, count in ...` splits them into two variables, like the tuple unpacking in Lesson 5.
- Adding an `if` turns the loop into a detection: only IPs over the threshold print.

---

## The shortcut with `.get()`

```python
failed2 = {}
for ip in log_ips:
    failed2[ip] = failed2.get(ip, 0) + 1
```

- `failed2.get(ip, 0)` returns the current count if the IP is there, or `0` if it isn't.
- That replaces the three-line `if ip not in failed` check with one line.
- It gives the same result as the longer version.

---

## Errors and what they mean

| Problem | Cause | Fix |
|---|---|---|
| `KeyError: '10.0.0.1'` | Looked up a key that isn't in the dictionary | Check with `in` first, or use `.get(key, 0)` |
| `TypeError: unhashable type` | Used a list as a key | Keys must be strings, numbers, or tuples |
| Counts are all 1 | The dictionary was created inside the loop and resets each pass | Create `failed = {}` before the loop |
| Only the last value survives | Wrote the same key twice | Keys are unique, so use a count instead |
| Wrong match, no error | Keys are case-sensitive: `"Admin"` and `"admin"` are different | Use `.lower()` before counting |

---

## Interview-style explanation

> "A dictionary maps keys to values, so it's the natural structure for counting events per source. In a brute-force detector I loop through the failed-login lines, use the source IP as the key, and increment its count with `.get(ip, 0) + 1`. Afterward I loop through `.items()` and flag any IP over my threshold. It's the Python equivalent of `stats count by src_ip` in Splunk."

---

## Splunk connection

```
index=linux "Failed password" | stats count by src_ip | where count > 5
```

The dictionary is the `stats count by src_ip` step, and the `if count > threshold` check is the `where` step.

---

## Self-check questions

1. What is the difference between `counts["a"]` and `"a" in counts`?
2. Why does Step 4 check `if ip not in failed` before adding 1?
3. What does `failed.get(ip, 0)` return for an IP that hasn't been seen?
4. What does `.items()` give you in a `for` loop?
5. Why must `failed = {}` come before the loop?

Answers: the first returns the value (and crashes if the key is missing), the second returns `True` or `False`; to avoid a `KeyError` on an IP's first appearance; `0`; each key together with its value; otherwise it would reset on every pass and the counts would never build up.

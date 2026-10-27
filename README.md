# soc-python

Learning Python by building small tools for SOC analyst work.

I'm preparing for a SOC analyst role, and this repo is my daily practice. Each lesson is a short script built around a real security task, such as counting failed logins, flagging brute-force attempts, and collecting suspicious IPs. Every lesson also has written notes that explain the concepts in plain English, because being able to explain code matters as much as writing it.

## Lessons

| # | File | Topic | SOC example |
|---|---|---|---|
| 1 | `fundamentals/01_variables.py` | Variables and printing | Store an IP, host, and event ID, then print an alert line |
| 2 | `fundamentals/02_strings.py` | Strings | Split an SSH log line and pull out the user, IP, and port |
| 3 | `fundamentals/03_conditions.py` | Conditions | Classify event IDs and assign severity from a failure count |
| 4 | `fundamentals/04_loops.py` | Loops | Count failed and accepted logins across log lines |
| 5 | `fundamentals/05_lists.py` | Lists | Collect flagged IPs without duplicates |

## Notes

Each lesson has two write-ups in `fundamentals/`:

- `NN_topic_notes.md`: terms, concepts, common errors, and self-check questions
- `NN_topic_breakdown.md`: the script explained block by block, with its output

There is also `git_notes.md`, a write-up of fixing a rejected push and a rebase conflict.

## Running a lesson

Python 3 is required (tested on 3.9). From the `fundamentals/` folder:

```bash
python3 01_variables.py
```

## Roadmap

- [x] Variables, strings, conditions, loops, lists
- [ ] Dictionaries: count failed logins per IP
- [ ] Reading log files line by line
- [ ] Functions
- [ ] Regex: extract IPs and usernames from messy text
- [ ] Mini project: a brute-force detector with a time window
- [ ] IOC enrichment with a threat-intelligence API

## Sample data

All IP addresses are from ranges reserved for documentation (`203.0.113.0/24`, `198.51.100.0/24`, `192.0.2.0/24`), so none belong to real hosts. The log lines are made up for practice.

## Related

Splunk detection labs live in [splunk-home-soc-lab](https://github.com/marctomek/splunk-home-soc-lab).

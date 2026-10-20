ips = ["203.0.113.45", "198.51.100.7", "192.0.2.10"]

for ip in ips:
       print("Checking", ip)
#ips is a list: three strings in square brackets, separated by commas.
#for ip in ips: runs the indented line once per item. On each pass, ip holds the current address.
#The list has to be created above the loop, because Python reads top to bottom. A missing or misspelled list gives NameError: name 'attempts' is not defined, the error you hit.
#Output:
#Checking 203.0.113.45
#Checking 198.51.100.7
#Checking 192.0.2.10

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
#The list holds integers (no quotes), so comparisons like count > 20 work.
#The if/elif/else ladder from Lesson 3 now runs once per number.
#Indentation has two levels: 4 spaces under for, and 8 spaces under each if, elif, and else.
#Output:
#3 LOW
#8 MEDIUM
#15 HIGH
#25 CRITICAL
    
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
        accepted_count = accepted_count+ 1

print("Total failed logins:", failed_count)
print("Total accepted logins:", accepted_count)
#Each item in log_lines is a string, with a comma after it. A missing comma would join two lines into one string.
#Both counters start at 0 before the loop. If they were created inside it, they would reset on every pass.
#if "Failed password" in line: is true when that exact text appears in the line.
#elif only checks lines that weren't failures, which is correct because each line is one kind of event.
#failed_count = failed_count + 1 reads the current value, adds 1, and stores it back.
#The two print lines have no indentation, so they run once, after the loop finishes.

for number in range(1, 6):
    print(number)
       python
#range(1, 6) starts at 1 and stops before 6.
#number holds each value in turn.
#Output:
#1
#2
#3
#4
#5

usernames = ["admin", "root", "guest", "bob"]

for name in usernames:
    if name == "admin" or name == "root":
        print(name, "Privileged account")
    else:
        print(name, "Standard account")
#A list of four strings, looped one at a time.
#or joins two full comparisons. Either match makes the if true.
#Anything that isn't admin or root falls through to the else.
#Output:
#admin Privileged account
#root Privileged account
#guest Standard account
#bob Standard account

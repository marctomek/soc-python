ips = ["203.0.113.45", "198.51.100.7", "192.0.2.10"]

for ip in ips:
       print("Checking", ip)

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

for number in range(1, 6):
    print(number)

usernames = ["admin", "root", "guest", "bob"]

for name in usernames:
    if name == "admin" or name == "root":
        print(name, "Privileged account")
    else:
        print(name, "Standard account")

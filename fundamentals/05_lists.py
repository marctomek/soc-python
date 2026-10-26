ips = ["203.0.113.45", "198.51.100.7", "192.0.2.10"]
print(ips)
print(ips[0])
print(ips[1])
print(ips[-1])
print(len(ips))
ips.append("198.51.100.99")
print(ips)
print(len(ips))
ips.remove("198.51.100.7")
print(ips)
print(len(ips))
print("192.0.2.10" in ips)
print("10.0.0.1" in ips)
flagged = []
for ip in ips:
    if ip == "203.0.113.45":
        flagged.append(ip)

print("Flagged:", flagged)
attempts = [15, 3, 25, 8, 3]
attempts.sort()
print(attempts)
print(attempts.count(3))
print(attempts[0:2])
print(max(attempts))
print(min(attempts))
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

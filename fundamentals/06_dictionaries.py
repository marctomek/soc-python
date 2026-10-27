counts = {"203.0.113.45": 12, "198.51.100.7": 2}

print(counts)
print(counts["203.0.113.45"])

counts["192.0.2.10"] = 9
counts["198.51.100.7"] = counts["198.51.100.7"] + 1

print(counts)

print("203.0.113.45" in counts)
print("10.0.0.1" in counts)

log_ips =["203.0.113.45", "198.51.100.7", "203.0.113.45", "203.0.113.45"]

failed = {}

for ip in log_ips:
    if ip not in failed:
        failed[ip] = 0
    failed[ip] = failed[ip] + 1

print(failed)

for ip in failed:
    print(ip, failed[ip])

for ip, count in failed.items():
    if count > 2:
        print("Alert", ip, count)
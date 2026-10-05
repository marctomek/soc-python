log_file = "auth.log"
threshold = 5
counts = {}

with open(log_file) as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]
            if ip not in counts:
                counts[ip] = 0
            counts[ip] = counts[ip] + 1

for ip in sorted(counts, key=counts.get, reverse=True):
    if counts[ip] > threshold:
        print("ALERT", ip, counts[ip])
    else:
        print("ok", ip, counts[ip])
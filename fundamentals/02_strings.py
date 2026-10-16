line = "Oct 16 09:14:02 server sshd[1234]: Failed password for admin from 203.0.113.45 port 51234 ssh2"

print("Failed password" in line)

parts = line.split()
print(parts)

print(parts[0])
print(parts[5])

print(parts[-1])
print(parts[-4])

print(line.upper())
print(line.lower())
print(line.replace("Failed", "FAILED"))

print(len(line))

username = parts[8]
print(username)

ip = parts[10]
port = parts[12]
print(ip)
print(port)

print(f"User {username} tried to log in from {ip} on port {port}")

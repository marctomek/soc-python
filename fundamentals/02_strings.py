line = "Oct 16 09:14:02 server sshd[1234]: Failed password for admin from 203.0.113.45 port 51234 ssh2"
#Creates a variable called line and puts the whole log entry inside it as a string.
#Nothing prints yet. This line only stores data.

print("Failed password" in line)
#in asks whether "Failed password" appears anywhere in line.
#Output: True

parts = line.split()
print(parts)
#.split() cuts the line at every space and returns a list of words, saved in parts.
# (ex. output) ['Oct', '16', '09:14:02', 'server', 'sshd[1234]:', 'Failed', 'password', 'for', 'admin', 'from', '203.0.113.45', 'port', '51234', 'ssh2']

print(parts[0])
print(parts[5])
#Square brackets pick one item by its position. Counting starts at 0.
# Output: [Oct] [Failed]
#parts[0] is the first item, and parts[5] is the sixth.

print(parts[-1])
print(parts[-4])
#Negative numbers count backward from the end. -1 is last.
#parts[-4] lands on the IP because it is four items from the end: ssh2 (-1), 51234 (-2), port (-3), IP (-4).

print(line.upper())
print(line.lower())
print(line.replace("Failed", "FAILED"))
#.upper() makes everything capitals, .lower() makes everything lowercase, and .replace(old, new) swaps one piece of text for another.
#OCT 16 09:14:02 SERVER SSHD[1234]: FAILED PASSWORD FOR ADMIN FROM 203.0.113.45 PORT 51234 SSH2
#oct 16 09:14:02 server sshd[1234]: failed password for admin from 203.0.113.45 port 51234 ssh2
#Oct 16 09:14:02 server sshd[1234]: FAILED password for admin from 203.0.113.45 port 51234 ssh2

print(len(line))
#len() counts the characters in the string.
#Output: 94

username = parts[8]
print(username)

ip = parts[10]
port = parts[12]
print(ip)
print(port)

print(f"User {username} tried to log in from {ip} on port {port}")

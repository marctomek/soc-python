# (=) here means "store this," not "is equal to."
ip = "203.0.113.45" # The name goes on the left, the value on the right, and = connects them
hostname = "WORKSTATION-07" # # string (in quotes)
event_id = 4625
failed_attempts = 7 # integer (no quotes)

print("Source IP:", ip)
print("Host:", hostname)
print("Event ID:", event_id)
print("Failed attempts:", failed_attempts)
# print() displays something on screen.
#Anything in quotes prints exactly as typed. A variable name without quotes prints the value stored inside it.
#Commas between items add a space between them automatically.
#Compare print("ip") (shows the word ip) with print(ip) (shows 203.0.113.45).

print(f"ALERT: {failed_attempts} failed logins from {ip} on {hostname}")
#The f before the opening quote turns on variable insertion.
#Inside {} goes the name of a variable, not the value itself. Python looks up the name and swaps in the value.
#Wrong: {203.0.113.45} causes a SyntaxError. Right: {ip}.
#This is the cleanest way to build alert messages, because the text and the data live in one line.

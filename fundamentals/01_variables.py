ip = "203.0.113.45"
hostname = "WORKSTATION-07"
event_id = 4625
failed_attempts = 7

print("Source IP:", ip)
print("Host:", hostname)
print("Event ID:", event_id)
print("Failed attempts:", failed_attempts)

print(f"ALERT: {failed_attempts} failed logins from {ip} on {hostname}")
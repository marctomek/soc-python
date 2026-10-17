failed_attempts = 2
threshold = 5

if failed_attempts > threshold: 
    print("ALERT: possible brute force")
else:
    print("OK: below threshold")

event_id = 4625

if event_id == 4624:
    print("Successful Logon")
elif event_id == 4625:
    print("Failed logon")
elif event_id == 4720:
    print("User account created")
else: 
    print("Unknown event")

username = "admin"

if failed_attempts > threshold and username =="admin":
    print("HIGH: brute force against admin account")

if username == "root" or username == "admin":
    print("Privileged account targeted")

country = "RU"

if country == "RU" or "CN":
    print("Review: login from watchlist country")
else:
    print("Normal")

if failed_attempts > 20:
    print("CRITICAL")
elif failed_attempts > 10:
    print("HIGH")
elif failed_attempts > 5:
    print("MEDIUM")
else:
    print("LOW")







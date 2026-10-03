# Lesson 1: count the failed logins in an SSH log

log_file = "auth.log"
failed_count = 0 
success_count =0

with open(log_file) as f:
    for line in f:
        if "Failed password" in line:
            failed_count = failed_count + 1
        if "Accepted password" in line:
            success_count = success_count + 1

print("Total failed logins:", failed_count)
print("Total successful logins:", success_count)
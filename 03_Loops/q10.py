import time 

wait_time = 1
max_retried = 5
attempts = 0

while attempts < max_retried:
    print("Attempting to connect...attems:",attempts,"wait-time:",wait_time)
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2
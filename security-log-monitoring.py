import time

LOG_FILE = "security.log"

def monitor_logs():
    print("Monitoring logs...")

    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Move to end of file

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            if "FAILED LOGIN" in line:
                print(f"[ALERT] Suspicious Activity Detected: {line.strip()}")

monitor_logs()

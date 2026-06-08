import subprocess
import platform
import time
from datetime import datetime

# List of devices/websites to monitor
targets = [
    "8.8.8.8",          # Google DNS
    "google.com",
    "github.com"
]

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", param, "1", host]

    try:
        output = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return output.returncode == 0

    except Exception:
        return False

print("Network Monitoring Tool Started...\n")

while True:
    print("=" * 50)
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    for target in targets:
        status = "UP" if ping(target) else "DOWN"
        print(f"{target:<20} : {status}")

    time.sleep(10)

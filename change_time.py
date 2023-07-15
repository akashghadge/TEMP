import subprocess
import sys

def change_system_date(new_date):
    # Windows
    if sys.platform.startswith("win"):
        subprocess.run(["date", new_date], shell=True)
    # macOS
    elif sys.platform.startswith("darwin"):
        subprocess.run(["sudo", "date", new_date], shell=True)
    # Linux
    elif sys.platform.startswith("linux"):
        subprocess.run(["sudo", "date", "-s", new_date], shell=True)
    else:
        print("Unsupported platform.")
        return

    print("System date changed successfully.")

# Usage example
new_date = "2023-06-15"
change_system_date(new_date)

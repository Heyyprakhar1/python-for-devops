#!/usr/bin/env python3
import os
import sys
# Read environment variable
LOG_LEVEL = os.getenv("logenv", "INFO")
# Check CLI argument
if len(sys.argv) < 2:
    print("Usage: python log_analyzer.py <log_file>")
    sys.exit(1)
LOG_FILE = sys.argv[1]
OUTPUT_FILE = "log_summary.txt"
def write_summary(log_counts):
    with open(OUTPUT_FILE, "w") as file:
        file.write("Log Analysis Summary\n")
        file.write("====================\n")
        for level, count in log_counts.items():
            file.write(f"{level}: {count}\n")
def main():
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()

            if not lines:
                print("Log file is empty.")
                return

            for line in lines:
                if LOG_LEVEL in line:
                    if "INFO" in line:
                        log_counts["INFO"] += 1
                    elif "WARNING" in line:
                        log_counts["WARNING"] += 1
                    elif "ERROR" in line:
                        log_counts["ERROR"] += 1
    except FileNotFoundError:
        print("Log file not found.")
        return
    print("\nLog Analysis Summary")
    print("====================")
    for level, count in log_counts.items():
        print(f"{level}: {count}")

    write_summary(log_counts)
if __name__ == "__main__":
    main()

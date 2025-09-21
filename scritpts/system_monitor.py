#!/usr/bin/env python3

import psutil
import time
import os
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 90

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"HIGH CPU: {cpu_usage}%")
    return cpu_usage

def check_memory():
    mem = psutil.virtual_memory()
    if mem.percent > MEMORY_THRESHOLD:
        log_alert(f"HIGH MEMORY: {mem.percent}%")
    return mem.percent

def check_disk():
    issues = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            percent = (usage.used / usage.total) * 100
            if percent > DISK_THRESHOLD:
                log_alert(f"HIGH DISK {partition.mountpoint}: {percent:.1f}%")
                issues.append((partition.mountpoint, percent))
        except PermissionError:
            pass
    return issues

def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"[{timestamp}] {message}"
    print(alert)
    with open("alerts.log", "a") as f:
        f.write(alert + "\n")

def main():
    print("System monitor started...")
    while True:
        try:
            cpu = check_cpu()
            mem = check_memory()
            disk_issues = check_disk()
            
            print(f"{datetime.now().strftime('%H:%M:%S')} - CPU:{cpu}% MEM:{mem}%")
            time.sleep(60)
        except KeyboardInterrupt:
            print("Monitor stopped")
            break

if __name__ == "__main__":
    main()
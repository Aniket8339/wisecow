#!/usr/bin/env python3

import requests
import time
from datetime import datetime

APPS = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "GitHub", "url": "https://github.com"},
]

def check_app(app):
    try:
        response = requests.get(app["url"], timeout=10)
        if response.status_code == 200:
            return {"name": app["name"], "status": "UP", "code": response.status_code}
        else:
            return {"name": app["name"], "status": "DOWN", "code": response.status_code}
    except Exception as e:
        return {"name": app["name"], "status": "DOWN", "error": str(e)}

def main():
    print("Health checker started...")
    while True:
        try:
            for app in APPS:
                result = check_app(app)
                status_icon = "✓" if result["status"] == "UP" else "✗"
                print(f"{datetime.now().strftime('%H:%M:%S')} {status_icon} {result['name']}: {result['status']}")
            
            time.sleep(60)
        except KeyboardInterrupt:
            print("Health checker stopped")
            break

if __name__ == "__main__":
    main()

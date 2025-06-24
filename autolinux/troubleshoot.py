# filepath: autolinux/troubleshoot.py
import subprocess

def troubleshoot():
    print("Collecting logs...")
    print("Gathering system logs (last 100 lines):")
    try:
        logs = subprocess.check_output(['tail', '-n', '100', '/var/log/syslog'], text=True)
        print(logs)
    except Exception as e:
        print(f"Could not read syslog: {e}")

    print("Searching for installed apps:")
    try:
        apps = subprocess.check_output(['dpkg-query', '-W', '-f=${binary:Package}\n'], text=True)
        print(apps.split('\n')[:10], "...")  # Show first 10 for brevity
    except Exception as e:
        print(f"Could not list packages: {e}")

    print("Checking system performance:")
    try:
        uptime = subprocess.check_output(['uptime'], text=True)
        print("Uptime:", uptime.strip())
    except Exception as e:
        print(f"Could not get uptime: {e}")

    print("Troubleshooting complete.")
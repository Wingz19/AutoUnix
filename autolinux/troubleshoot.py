import subprocess

def troubleshoot():
    log_file = "log_collector.txt"
    with open(log_file, "w") as f:
        f.write("=== Autolinux Troubleshooting Report ===\n\n")

        f.write(">>> Collecting system logs (last 100 lines):\n")
        print("Collecting logs...")
        try:
            logs = subprocess.check_output(['tail', '-n', '100', '/var/log/syslog'], text=True)
            f.write(logs + "\n")
            print("System logs collected.")
        except Exception as e:
            error_msg = f"Could not read syslog: {e}\n"
            f.write(error_msg)
            print(error_msg.strip())

        f.write("\n>>> Collecting ERROR/FAILURE logs (last 100 lines):\n")
        print("Collecting error/failure logs...")
        try:
            error_logs = subprocess.check_output(
                "grep -Ei 'error|fail|critical' /var/log/syslog | tail -n 100",
                shell=True, text=True
            )
            if error_logs.strip():
                f.write(error_logs + "\n")
                print("Error/failure logs collected.")
            else:
                f.write("No error or failure logs found in /var/log/syslog.\n")
                print("No error or failure logs found.")
        except Exception as e:
            error_msg = f"Could not filter error/failure logs: {e}\n"
            f.write(error_msg)
            print(error_msg.strip())

        f.write("\n>>> Searching for installed apps:\n")
        print("Searching for installed apps...")
        try:
            apps = subprocess.check_output(['dpkg-query', '-W', '-f=${binary:Package}\n'], text=True)
            app_list = apps.split('\n')[:10]
            f.write('\n'.join(app_list) + "\n...\n")
            print("Installed apps listed.")
        except Exception as e:
            error_msg = f"Could not list packages: {e}\n"
            f.write(error_msg)
            print(error_msg.strip())

        f.write("\n>>> Checking system performance:\n")
        print("Checking system performance...")
        try:
            uptime = subprocess.check_output(['uptime'], text=True)
            f.write("Uptime: " + uptime.strip() + "\n")
            print("System performance checked.")
        except Exception as e:
            error_msg = f"Could not get uptime: {e}\n"
            f.write(error_msg)
            print(error_msg.strip())

        f.write("\n=== End of Troubleshooting Report ===\n")
        print("Troubleshooting report complete. Report saved to log_collector.txt.")
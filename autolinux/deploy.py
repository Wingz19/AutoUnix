# filepath: autolinux/deploy.py
from autolinux.backup import config_backup
import os
import json

DEPLOY_STATUS_FILE = "/tmp/autolinux_deploy_status.json"

def _load_status():
    if os.path.exists(DEPLOY_STATUS_FILE):
        with open(DEPLOY_STATUS_FILE, "r") as f:
            return json.load(f)
    return {"deployed": False}

def _save_status(status):
    with open(DEPLOY_STATUS_FILE, "w") as f:
        json.dump(status, f)

def deploy():
    status = _load_status()
    if status.get("deployed"):
        print("Already deployed. Skipping deployment.")
        return
    config_backup()
    print("Deploying application...")
    # Simulate deployment logic
    print("Copying files, setting permissions, starting services...")
    status["deployed"] = True
    _save_status(status)
    print("Deployment complete.")

def test_deploy():
    print("Simulating deployment (--dry-run)...")
    print("Would backup config, copy files, set permissions, start services.")
    print("Test deploy complete.")

def check_deploy():
    status = _load_status()
    print(f"Deployment status: {'DEPLOYED' if status.get('deployed') else 'NOT DEPLOYED'}")

def revert_deploy():
    print("Reverting to previous deployment config...")
    # Simulate pulling backup and restoring
    print("Pulling backup from backup server...")
    print("Restoring files and configuration...")
    _save_status({"deployed": False})
    print("Revert complete.")
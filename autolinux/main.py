import argparse
from autolinux.maintenance import maintenance_tasks
from autolinux.deploy import deploy, test_deploy, check_deploy, revert_deploy
from autolinux.patch import patch, test_patch, check_patch, revert_patch
from autolinux.fix import fix, test_fix, check_fix, revert_fix
from autolinux.troubleshoot import troubleshoot
from autolinux.backup import config_backup
from autolinux.bashcompletion import print_bash_completion

def main():
    parser = argparse.ArgumentParser(description="Autolinux Automation Tool")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("help", help="List all commands and explanations")
    subparsers.add_parser("deploy", help="Deploy server")
    subparsers.add_parser("test-deploy", help="Dry run deploy")
    subparsers.add_parser("check-deploy", help="Check last deploy")
    subparsers.add_parser("revert-deploy", help="Revert to previous deploy config")
    subparsers.add_parser("patch", help="Apply patches")
    subparsers.add_parser("test-patch", help="Dry run patch")
    subparsers.add_parser("check-patch", help="Check last patch")
    subparsers.add_parser("revert-patch", help="Revert to previous patch config")
    subparsers.add_parser("fix", help="Apply fix")
    subparsers.add_parser("test-fix", help="Dry run fix")
    subparsers.add_parser("check-fix", help="Check last fix")
    subparsers.add_parser("revert-fix", help="Revert to previous fix config")
    subparsers.add_parser("troubleshoot", help="Troubleshoot system")
    subparsers.add_parser("config-backup", help="Create and ship backup")
    subparsers.add_parser("bash-completion", help="Output bash completion script")

    args = parser.parse_args()

    if args.command == "help":
        print("autolinux do deploy | test-deploy | check-deploy | revert-deploy")
        print("autolinux do patch | test-patch | check-patch | revert-patch")
        print("autolinux do fix | test-fix | check-fix | revert-fix")
        print("autolinux do troubleshoot")
        print("autolinux do config-backup")
        print("autolinux bash-completion  # Output bash completion script")
    
    elif args.command == "deploy":
        deploy()
    elif args.command == "test-deploy":
        test_deploy()
    elif args.command == "check-deploy":
        check_deploy()
    elif args.command == "revert-deploy":
        revert_deploy()
    elif args.command == "patch":
        patch()
    elif args.command == "test-patch":
        test_patch()
    elif args.command == "check-patch":
        check_patch()
    elif args.command == "revert-patch":
        revert_patch()
    elif args.command == "fix":
        fix()
    elif args.command == "test-fix":
        test_fix()
    elif args.command == "check-fix":
        check_fix()
    elif args.command == "revert-fix":
        revert_fix()
    elif args.command == "troubleshoot":
        troubleshoot()
    elif args.command == "config-backup":
        config_backup()
    elif args.command == "bash-completion":
        print_bash_completion()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
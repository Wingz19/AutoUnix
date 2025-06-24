import os

def print_bash_completion():
    commands = [
        "deploy", "test-deploy", "check-deploy", "revert-deploy",
        "patch", "test-patch", "check-patch", "revert-patch",
        "fix", "test-fix", "check-fix", "revert-fix",
        "troubleshoot", "config-backup", "help", "bash-completion", "enable-bash-completion"
    ]
    completion_script = f"""
_autolinux_completions()
{{
    COMPREPLY=($(compgen -W "{' '.join(commands)}" -- "${{COMP_WORDS[1]}}"))
}}
complete -F _autolinux_completions autolinux
"""
    print(completion_script)

def enable_bash_completion():
    home = os.path.expanduser("~")
    script_path = os.path.join(home, "autolinux-completion.sh")
    bashrc_path = os.path.join(home, ".bashrc")

    # Write the completion script
    with open(script_path, "w") as f:
        commands = [
            "deploy", "test-deploy", "check-deploy", "revert-deploy",
            "patch", "test-patch", "check-patch", "revert-patch",
            "fix", "test-fix", "check-fix", "revert-fix",
            "troubleshoot", "config-backup", "help", "bash-completion", "enable-bash-completion"
        ]
        completion_script = f"""
_autolinux_completions()
{{
    COMPREPLY=($(compgen -W "{' '.join(commands)}" -- "${{COMP_WORDS[1]}}"))
}}
complete -F _autolinux_completions autolinux
"""
        f.write(completion_script)

    # Add source line to .bashrc if not already present
    source_line = f"source {script_path}"
    already_set = False
    if os.path.exists(bashrc_path):
        with open(bashrc_path, "r") as f:
            for line in f:
                if source_line in line:
                    already_set = True
                    break
    if not already_set:
        with open(bashrc_path, "a") as f:
            f.write(f"\n# Enable autolinux bash completion\n{source_line}\n")
        print(f"Bash completion enabled! Added to {bashrc_path}.")
    else:
        print("Bash completion already enabled in your .bashrc.")

    print("You may need to restart your terminal or run: source ~/.bashrc")
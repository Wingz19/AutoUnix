# Autolinux
Automation Tool For Linux

Maintenance:
Server access
search for apps used - logs related to
system performance details
any issues to look at
patches available

Server deployment
check if it was deployed before and if it was do not deploy
test deploy and produce result --dry-run
create minimal tool that create compressed data/config backups 

Check vulnerabilities and suggest fixes

develop and cli for this tool:

every backup created is shipped offsite to autonix backup server

autolinux deploy requirements
autolinux server
autolinux backup server

command syntax: 
autolinux help me - lists all commands and explanations
<command> - deploy|test|patch|check|
autolinux do deploy-<command> Deploy server
autolinux do revert-<command> revert to previous config, working config - pulls backup from backup server
autolinux do test-<command> is a dry run with details on what would have happened
autolinux do check-<command> check last deploy and what was changed
autolinux do troubleshoot - collect logs, search for used apps and logs related, system performances
autolinux do config-backup - create backup and ship offsite to autonix backup server

autolinux do deploy | test-deploy | check-deploy | revert-deploy
autolinux do patch | test-patch | check-patch | revert-patch
autolinux do fix | test-fix | check-fix | revert-fix
autolinux do troubleshoot
autolinux do config-backup


# Autolinux
Automation Tool For Linux

Maintenance
Server deployment

Start Here:

Clone Repo:
git clone https://github.com/Wingz19/AutoUnix.git
cd AutoUnix/autolinux

Install pip and switch to virtual env:
apt install python3-pip
apt install python3
apt install python3-venv
python3 -m venv testenv
source testenv/bin/activate

Enable bash completion
python -m autolinux.main bash-completion
python -m autolinux.main bash-completion > autolinux-completion.sh
source autolinux-completion.sh

syntax 
autolinux <do>
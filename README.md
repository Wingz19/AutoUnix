# Autolinux
Automation Tool For Linux

## Features
- Maintenance
- Server deployment

## Start Here

### Clone the Repository
```sh
git clone https://github.com/Wingz19/AutoUnix.git
cd AutoUnix/autolinux
```
### Install pip and Switch to Virtual Environment
```sh
apt install python3-pip
apt install python3
apt install python3-venv
python3 -m venv testenv
source testenv/bin/activate
```
### Enable Bash Completion
```sh
python -m autolinux.main bash-completion
python -m autolinux.main bash-completion > autolinux-completion.sh
source autolinux-completion.sh
```
### Command Syntax
```sh
python -m autolinux.main <option>
```
### Example, to list all available options
```sh
python -m autolinux.main help
```
# Developer Prep

## Install Prereqs

### Mac

1. [Install brew](https://brew.sh/)
1. Install openssh: `brew install openssh`
1. Turn on remote login: System Preference > General > Sharing > Advanced > Remote Login

### All systems
1. Generate ssh key: `ssh-keygen`
1. Install key on local system: `ssh-copy-id localhost`
1. [Install Python](https://www.python.org/downloads/macos/)
1. Install pip and venv
  1. If you used the python installer: `python3 -m ensurepip`
  1. If you used brew to install python: `brew install pipx`
  1. If you used apt to install python: `apt install pipx`
1. Install Ansible `pipx install --include-deps ansible`
  1. You may need to add `$HOME/.local/bin` to `$PATH`
    1. On most shells: `export PATH=$PATH:$HOME/.local/bin`
    1. You can also update your rc file typically: `~/.bashrc` or `~/.zshrc`

### Installing the rest of the dependencies
1. Run the ansible playbook for your os, e.g. for a mac: `ansible-playbook -i ansible/inventory.ini ansible/mac-deps.yaml`

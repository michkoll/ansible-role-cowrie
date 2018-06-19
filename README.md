Ansible Role: Cowrie
=========

Ansible role for setting up the medium interaction honeypot [Cowrie](https://github.com/micheloosterhof/cowrie)

Requirements
------------

Written and tested on Ubuntu 16.06

Python need to be installed.

Role Variables
--------------
Short overview of the role variables and default values defined in `defaults/main.yml`.

```yaml
cowrie_hostname: userdb
```
Hostname for the honeypot, displayed by the shell prompt of the virtual environment. If you are using multiple instances you have to define the hostname in inventory variables per host.

```yaml
cowrie_auth_method: "random"
```
Defining the ssh auth method. Possible values are `userdb`, `random` or `none`.

```yaml
cowrie_ssh_enabled: "true"
cowrie_sftp_enabled: "true"
cowrie_telnet_enabled: "true"
```
Activate or deactivate honeypot services.

```yaml
cowrie_output_json: "true"
cowrie_output_json_path: "log/cowrie.json"
```
Configure json logging output.

```yaml
cowrie_output_mysql: "true"
cowrie_output_mysql_host: "localhost"
cowrie_output_mysql_database: "cowrie"
cowrie_output_mysql_username: "cowrie"
cowrie_output_mysql_password: "secret"
cowrie_output_mysql_port: "3306"
```
Configure mysql logging output. If mysql output is activated, mysql server and necessary packages will be installed automatically.


Extra Variables
---------------

```bash
ansible-playbook site.yml --extra-vars "cowrie_clear_database=true"
```
Reset cowrie database. All data will be deleted.


Dependencies
------------

Dependency to hardening role for changing ssh port and basic iptables rules.

See https://github.com/michkoll/ansible-role-hardening for more details.

Example Playbook
----------------

After installing the role (```requirements.xml``` or as dependency) you can use the role as described here:

    - hosts: cowrie
      roles:
         - { role: cowrie}

License
-------

MIT

Author Information
------------------

&copy; 2018
Written by [Michael Koll](https://github.com/michkoll)

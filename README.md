Ansible Role: Cowrie
=========

Ansible role for setting up the medium interaction honeypot [Cowrie](https://github.com/micheloosterhof/cowrie)

Requirements
------------

TODO

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
Configure logging output. At the moment only jsonlog is possible.


Extra Variables
---------------

```bash
ansible-playbook site.yml --extra-vars "cowrie_clear_database=true"
```
Reset cowrie database. All data will be deleted.

TODO

Dependencies
------------

TODO

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

MIT

Author Information
------------------

Written by [Michael Koll](https://github.com/michkoll)

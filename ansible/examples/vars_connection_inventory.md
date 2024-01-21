==============================================================================================
ansible_connection

    Connection type to the host. This can be the name of any Ansible connection plugin. SSH protocol types are smart, ssh or paramiko. The default is smart. Non-SSH based types are described in the next section.
==============================================================================================
General for all connections:

ansible_host

    The name of the host to connect to, if different from the alias you wish to give to it.
ansible_port

    The connection port number, if not the default (22 for ssh)
ansible_user

    The username to use when connecting to the host
ansible_password

    The password to use to authenticate to the host (never store this variable in plain text; always use a vault. See Keep vaulted variables safely visible)
==============================================================================================
Specific to the SSH connection:

ansible_ssh_private_key_file

    Private key file used by SSH. Useful if using multiple keys and you do not want to use SSH agent.
ansible_ssh_common_args

    This setting is always appended to the default command line for sftp, scp, and ssh. Useful to configure a ProxyCommand for a certain host (or group).
ansible_sftp_extra_args

    This setting is always appended to the default sftp command line.
ansible_scp_extra_args

    This setting is always appended to the default scp command line.
ansible_ssh_extra_args

    This setting is always appended to the default ssh command line.
ansible_ssh_pipelining

    Determines whether or not to use SSH pipelining. This can override the pipelining setting in ansible.cfg.
ansible_ssh_executable (added in version 2.2)

    This setting overrides the default behavior to use the system ssh. This can override the ssh_executable setting in ansible.cfg under ssh_connection.
==============================================================================================
Privilege escalation (see Ansible Privilege Escalation for further details):

ansible_become

    Equivalent to ansible_sudo or ansible_su, allows to force privilege escalation
ansible_become_method

    Allows to set privilege escalation method
ansible_become_user

    Equivalent to ansible_sudo_user or ansible_su_user, allows you to set the user you become through privilege escalation
ansible_become_password

    Equivalent to ansible_sudo_password or ansible_su_password, allows you to set the privilege escalation password (never store this variable in plain text; always use a vault. See Keep vaulted variables safely visible)
ansible_become_exe

    Equivalent to ansible_sudo_exe or ansible_su_exe, allows you to set the executable for the escalation method selected
ansible_become_flags

    Equivalent to ansible_sudo_flags or ansible_su_flags, allows you to set the flags passed to the selected escalation method. This can be also set globally in ansible.cfg in the become_flags option under privilege_escalation.
==============================================================================================
Remote host environment parameters:

ansible_shell_type

    The shell type of the target system. You should not use this setting unless you have set the ansible_shell_executable to a non-Bourne (sh) compatible shell. By default, commands are formatted using sh-style syntax. Setting this to csh or fish will cause commands executed on target systems to follow those shell’s syntax instead.

ansible_python_interpreter

    The target host Python path. This is useful for systems with more than one Python or not located at /usr/bin/python such as *BSD, or where /usr/bin/python is not a 2.X series Python. We do not use the /usr/bin/env mechanism as that requires the remote user’s path to be set right and also assumes the python executable is named python, where the executable might be named something like python2.6.
ansible_*_interpreter

    Works for anything such as ruby or perl and works just like ansible_python_interpreter. This replaces shebang of modules that will run on that host.
==============================================================================================
New in version 2.1.

ansible_shell_executable

    This sets the shell the ansible control node will use on the target machine, overrides executable in ansible.cfg which defaults to /bin/sh. You should only change this value if it is not possible to use /bin/sh (in other words, if /bin/sh is not installed on the target machine or cannot be run from sudo.).
==============================================================================================
==============================================================================================
Examples from an Ansible-INI host file:

some_host         ansible_port=2222     ansible_user=manager
aws_host          ansible_ssh_private_key_file=/home/example/.ssh/aws.pem
freebsd_host      ansible_python_interpreter=/usr/local/bin/python
ruby_module_host  ansible_ruby_interpreter=/usr/bin/ruby.1.9.3

==============================================================================================


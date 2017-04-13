#!/usr/bin/python
###############################################################
# Author: Cristian Segura <cristian.segura.lepe@gmail.com>
# Creation Date: 2017/02/18 20:38
###############################################################


import paramiko

DEFAULT_SSH_PORT=22


def remote_exec(r_host, r_user, r_pass, r_command, r_port=DEFAULT_SSH_PORT):
    # remote_exec:
    # Usage: execute remote shell command via SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(r_host, r_port, username=r_user, password=r_pass)
    stdin, stdout, stderr = ssh.exec_command(r_command)
    print stdout.read()




# Just test remote_exec function
#remote_exec('localhost', 'csl', 'kaned2345', 'echo $HOSTNAME')

"""
warning
/usr/bin/python2.7 /home/csl/PycharmProjects/testing/python/ssh/cslSSHTools.py
/usr/lib/python2.7/dist-packages/Crypto/Cipher/blockalgo.py:141: FutureWarning: CTR mode needs counter parameter, not IV
  self._cipher = factory.new(key, *args, **kwargs)
4.4.0-62-generic
"""

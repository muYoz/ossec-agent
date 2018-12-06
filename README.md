# ossec-agent
OSSEC剂自动安装脚本-linux系统

执行过程（***为脱敏）：
rm -rf /etc/yum.repos.d/wazuh.repo

cat > /etc/yum.repos.d/wazuh.repo <<\EOF
[wazuh_repo]
gpgcheck=1
gpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH
enabled=1
name=Wazuh repository
baseurl=https://packages.wazuh.com/3.x/yum/
protect=1
EOF

yum remove -y wazuh-agent
Loaded plugins: fastestmirror
Resolving Dependencies
--> Running transaction check
---> Package wazuh-agent.x86_64 0:3.7.1-1 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package             Arch           Version           Repository           Size
================================================================================
Removing:
 wazuh-agent         x86_64         3.7.1-1           @wazuh_repo          74 M

Transaction Summary
================================================================================
Remove  1 Package

Installed size: 74 M
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : wazuh-agent-3.7.1-1.x86_64                                   1/1 
warning: /var/ossec/etc/ossec.conf saved as /var/ossec/etc/ossec.conf.rpmsave
warning: /var/ossec/etc/client.keys saved as /var/ossec/etc/client.keys.rpmsave
  Verifying  : wazuh-agent-3.7.1-1.x86_64                                   1/1 

Removed:
  wazuh-agent.x86_64 0:3.7.1-1                                                  

Complete!
yum install -y wazuh-agent
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.cn99.com
 * epel: mirrors.aliyun.com
 * extras: mirrors.163.com
 * updates: mirrors.cn99.com
Resolving Dependencies
--> Running transaction check
---> Package wazuh-agent.x86_64 0:3.7.1-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package             Arch           Version            Repository          Size
================================================================================
Installing:
 wazuh-agent         x86_64         3.7.1-1            wazuh_repo         6.9 M

Transaction Summary
================================================================================
Install  1 Package

Total download size: 6.9 M
Installed size: 74 M
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : wazuh-agent-3.7.1-1.x86_64                                   1/1 
  Verifying  : wazuh-agent-3.7.1-1.x86_64                                   1/1 

Installed:
  wazuh-agent.x86_64 0:3.7.1-1                                                  

Complete!
sed -i "s/MANAGER_IP/192.168.1.***/g" /var/ossec/etc/ossec.conf
/var/ossec/bin/agent-auth -m 192.168.1.***  -A 192.168.1.*** -P Top**Secret
INFO: Connected to 192.168.1.***:1515
INFO: Using agent name as: 192.168.1.***
INFO: Send request to manager. Waiting for reply.
INFO: Received response with agent key
INFO: Valid key created. Finished.
INFO: Connection closed.
systemctl restart wazuh-agent
service wazuh-agent restart
Restarting wazuh-agent (via systemctl):  [  OK  ]
主机：192.168.1.*** 账号：root，密码：1QAZ2wsx 已完成install作业

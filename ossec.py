#-*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
import threading
import time

#多线程批量安装

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print o,
        ssh.close()
        print u"主机：%s 账号：%s，密码：%s 已完成install作业" % (ip, username, passwd)
        time.sleep(2)#发现执行了一半后程序停止，加个睡眠时间给足够反应
    except Exception, e:
        if "Errno 61" in e or "timed out" in e: return


if __name__=='__main__':
    usernames = ['root', 'oracle']  # 用户名
    passwds = ['123456', '1qaz2wsx', '1QAZ2wsx', '1234qwer', '1qaz@WSX', 'oracle']
    print "Begin......"
    threads = []   #多线程
    #result = []
    # 将IP一行一个添加到txt
    with open('sship.txt', 'r') as f:
        result = f.readlines()
    for ips in result:
        ip = ips.strip()#不加这个会导致下面注册agent的时候ip会出现隔行的巨坑，需要去掉\n
        print ip
        for username in usernames:
            for passwd in passwds:
                passwd = str(passwd.replace('{username}', username))
                cmd = ['rm -rf /etc/yum.repos.d/wazuh.repo\n',
                       'cat > /etc/yum.repos.d/wazuh.repo <<\EOF\n'
                       '[wazuh_repo]\n'
                       'gpgcheck=1\n'
                       'gpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH\n'
                       'enabled=1\n'
                       'name=Wazuh repository\n'
                       'baseurl=https://packages.wazuh.com/3.x/yum/\n'
                       'protect=1\n'
                       'EOF\n',
                       'yum remove -y wazuh-agent',
                       'yum install -y wazuh-agent',
                       'sed -i "s/MANAGER_IP/192.168.1.***/g" /var/ossec/etc/ossec.conf',
                       '/var/ossec/bin/agent-auth -m 192.168.1.***  -A %s -P Top**Secret' % (ip),
                       'systemctl restart wazuh-agent',
                       'service wazuh-agent restart']  # 你要执行的命令列表
                a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
                a.start()

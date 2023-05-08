import paramiko


# def sshExcCMD(ip, username, password, port=22):
def sshExcCMD():
    # 实例化SSHClient
    """
        创建shhs端工具
    """
    client = paramiko.SSHClient()
    # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接SSH服务端，以用户名和密码进行认证
    client.connect(hostname='192.168.81.136', port=22, username='root', password='111111')
    '''
    stdin  # 1.标准输入 用于实现交互式命令
    stdout # 2.标准输出 保存命令的正常执行结果
    stderr # 3.标准错误输出 保存命令的错误信息
    '''
    # 打开一个Channel并执行命令
    # client.exec_command('cd /;cd home; rmdir text; ls ')
    stdin, stdout, stderr = client.exec_command('cd /;cd home; rmdir text; ls ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
    # 打印执行结果
    print(stdout.read().decode('utf-8'))
    # 关闭SSHClient
    client.close()


if __name__ == '__main__':
    sshExcCMD()

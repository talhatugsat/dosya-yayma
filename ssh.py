import paramiko

class ssh:
    def __init__(self, username, password):
        self.usnm = username
        self.pasw = password
    
    def connect(self, hostname, port = 22, timeout = 10):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname, port, self.usnm, self.pasw, timeout = timeout)
            self.ssh_client = ssh_client
            return True
        except Exception as e:
            return e

    def upload_file(self, local_file_path, remote_file_path):
        try:
            ssh_client = self.ssh_client
            sftp_client = ssh_client.open_sftp()
            sftp_client.put(local_file_path, remote_file_path)
            return True
        except Exception as e:
            return e
    def emtpy_the_folder(self, remote_folder_path):
        try:
            ssh_client = self.ssh_client
            ssh_client.exec_command("rm -rf {}".format(remote_folder_path))
            return True
        except Exception as e:
            return e
    def restartService(self, service_name):
        try:
            ssh_client = self.ssh_client
            ssh_client.exec_command("service {} restart".format(service_name))
            return True
        except Exception as e:
            return e
    
    def close(self):
        self.ssh_client.close()
        return True
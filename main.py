from ssh import ssh
from telegram import Telegram
import os
import time

local_dir = "/path/to/local/folder"
remote_dir = "/path/to/remote/folder"
telegram_chat = "telegram_chat_id"
telegram_bot_token = "telegram_bot_token"
sleepsecond = 10

hosts = {
    "Test Server": {
        "hostname": "192.168.1.25",
        "port": 22,
        "username": "root",
        "password": "123456",
    },
    "Real Server": {
        "hostname": "192.168.1.26",
        "port": 22,
        "username": "root",
        "password": "123456",
    },
    
}


def main():
    tlgrm = Telegram(telegram_bot_token,telegram_chat)
    tlgrm.sendMessage("Started")
    for host in hosts:
        ssh_obj = ssh(hosts[host]["username"], hosts[host]["password"])
        connect = ssh_obj.connect(hosts[host]["hostname"], hosts[host]["port"])
        if connect == True:
            ssh_obj.emtpy_the_folder(remote_dir + "/*")
            for file in os.listdir(local_dir):
                ssh_obj.upload_file(local_dir + "/" + file, remote_dir + "/" + file)
            
            ssh_obj.close()
            tlgrm.sendMessage("Connection ok: {}".format(host))
        else:
            print("Error to connecting the server: {}".format(connect))
            tlgrm.sendMessage("Error to connecting the server: {}".format(host))
    tlgrm.sendMessage("Stopped")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(sleepsecond)
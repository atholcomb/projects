#!/usr/bin/python3
# written by: atholcomb
# make_logs.py
# generates log file entries

import json
from random import choice
from random import randint

def make_logs():
  logfile = {}
  
  # create 30 log entries
  for i in range(1, 31):
    acct_names = ["apache", "sys", "ath", "user1", "root", "docker", "mysql"]
    http_status = ["200", "301", "400", "403", "404", "500", "303", "501"]
    cmds = ["grep", "top", "systemctl", "netstat", "nmap", "su -", "restart", "ssh"]
    perms = ["0600", "0700", "0777", "0755", "0500", "0655", "0644", "0555"]
    date = f"{randint(1, 12)}/{randint(1,31)}/{randint(2021, 2023)}"
    
    # create dictionary from values above
    logfile[f"log#{i}"] = [date, choice(http_status), choice(perms), choice(cmds), choice(acct_names)]

  # store json data into a file name 'logs.json' inside working directory
  data = json.dumps(logfile, indent=4)
  f = open('logs.json', 'w')
  f.write(data)
  f.close()

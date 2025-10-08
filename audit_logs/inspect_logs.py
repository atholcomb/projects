#!/usr/bin/python3
# written by: atholcomb
# main.py
# generate log files and parse for root entries

import json
from logs import logs

def main():

  # create logfile entries to parse
  logs.make_logs()

  # open the logs.json file that was created
  with open("logs.json", "r") as read_file:
    # convert file into Python dictionary
    logfile = json.load(read_file)
    # parse log file for root entries
    for lognum, entry in logfile.items():
      for audit in entry:
        if "su -" in audit or "root" in audit:
          print(lognum, "\t", audit, "\t", entry[0])


if __name__ == "__main__":
    main()

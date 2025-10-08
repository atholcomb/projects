# audit logs
Audits the logs.json file for entries that contain `root` or `su -`

# To Run:
`./inspect_logs.py`

# Output should read as follows:
```
log#1 	 root 	 6/25/2023
log#6 	 su - 	 1/16/2023
log#8 	 root 	 4/5/2022
log#9 	 root 	 1/2/2023
log#15 	 su - 	 4/10/2022
log#15 	 root 	 4/10/2022
log#21 	 su - 	 12/21/2023
log#24 	 root 	 12/26/2021
log#29 	 su - 	 1/10/2021
```

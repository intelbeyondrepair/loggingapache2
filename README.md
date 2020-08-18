
# By: Shawn Adams                                                                  

This script automates displaying log files in linux.
	* It Shows All Recent SSH Logins,
	
	* Every IP that visited the Apache2 Web Server and what they requested,

	* And All Kernel Messages Using the command dmesg

Just a side project to help me learn Python. Feel Free to request any additions to the script.

	USAGE: python3 LogReader.py
	OR: sudo chmod +x ./LogReader.py && ./LogReader.py

REQUIREMENTS:
gnome-terminal (To open a new terminal window for each log)
Apache2 (To be able to read the Apache Logs)
Python 3

I personally use this because i tend to be lazy.
I set an alias to open the script so i wont have to dig around in /var/log
	Like So:
nano .bash_aliases
alias logs='sudo python /home/$USER/LogReader/LogReader.py'


Remember, Check Your Logs Often. :3

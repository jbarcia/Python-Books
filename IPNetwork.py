from netaddr import IPNetwork
for ip in IPNetwork('199.254.202.0/24'):
	print '%s' % ip
import ldap
def auth_user(user, passwd):
	conn = ldap.initialize("ldap://IP:PORT”)
	try:
		conn.simple_bind_s(user, passwd)
		return 1
	except:
		return 0


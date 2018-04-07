from parties.user import User

class Client(User):

	def __init__(self, name):
		super(Client, self).__init__()
		self.name = name
		self.consultant_pub_key = None
		self.type = "patient"
		
	def set_consultant_pub_key(self, pubKey):
		self.consultant_pub_key = pubKey

	def get_consultant_pub_key(self):
		return self.consultant_pub_key

	def generate_own_key(self, mpeck, g):
		self.set_own_keys(mpeck.single_keygen(g))

	# def __dict__():
	# 	return ""
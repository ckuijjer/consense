
class User(object):

	def __init__(self):
		super(User, self).__init__()
		self.public_key = None
		self.private_key = None
		self.g = None
		self.type = ''
		
	def get_pub_key(self):
		return self.public_key

	def get_pr_key(self):
		return self.private_key

	def get_g(self):
		return self.g

	def set_own_keys(self, key_pair):
		(pk, sk) = key_pair
		self.private_key = sk['x']
		self.g = pk['g']
		self.public_key = pk['h']
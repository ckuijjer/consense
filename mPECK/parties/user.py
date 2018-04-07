from enum import Enum


class User_Type(Enum):
	RESEARCHER = 'RESEARCHER'
	PATIENT = 'PATIENT'


class User(object):

	def __init__(self, name, user_type):
		super(User, self).__init__()
		self.name = name

		self.public_key = None
		self.private_key = None
		self.g = None
		
		self.type = user_type
		self.otherKeys = []
	
	def generate_own_keys(self, mpeck):
		self.set_own_keys(mpeck.single_keygen(self.g))

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

	def set_other_keys_by_name(self, name, key_pair):
		if name not in self.otherKeys:
			#(pk, sk) = key_pair
			self.otherKeys[name] = key_pair.pk['h']

	def get_other_keys_by_name(self, name):
		return self.otherKeys[name]
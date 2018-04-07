from enum import Enum
import json
from random import randint

class User_Type(Enum):
	RESEARCHER = 'RESEARCHER'
	PATIENT = 'PATIENT'

	def __str__(self):
		return str(self.value)


class User(object):

	def __init__(self, name, user_type):
		super(User, self).__init__()
		self.name = name
		self.ID = randint(1, 666)

		self.public_key = None
		self.private_key = None
		self.g = None
		
		self.type = user_type
		self.otherKeys = dict()
	
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


	def add_other_key_by_name(self, name, key):
		if name not in self.otherKeys:
			self.otherKeys[name] = key

	def get_other_keys_by_name(self, name):
		return self.otherKeys[name]

	def __dict__(self):
		return "{name : %s, type : %s, public_key : %s, other_keys : %s}" % (self.name, self.type, self.public_key, self.otherKeys)

	def serialize(self):
		return json.dumps(self, default=lambda x: x.__dict__(), indent=4)
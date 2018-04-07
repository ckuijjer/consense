
class Record(object):
	
	def __init__(self,  user, keywords = [], i=None):
		super(Record, self).__init__()
		self.keywords = keywords
		self.type = user.type
		self.user = user
		self.i = i

	def add_keyword(self, kw):
		if not any(kw in s for s in self.keywords):
			self.keywords.append(kw)
		return self

	def remove_keyword(self, kw):
		self.keywords = [x for x in self.keywords if x != kw]

	def get_keyword(self, i):
		return self.keywords[i]

	def __dict__(self):
		return "{user: %s, user_type : %s, keywords : %s}" % (self.user.ID, self.type, self.keywords)

	def __eq__(self, other):
		return (self.keywords == other.keywords and self.user == other.user and self.type == other.type)
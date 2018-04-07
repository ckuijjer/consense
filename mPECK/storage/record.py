
class Record(object):
	
	def __init__(self,  user, userType, keywords, i=None):
		super(Record, self).__init__()
		self.keywords = keywords
		self.type = userType
		self.user = user
		self.i = i

	def add_keyword(self, kw):
		if not any(kw in s for s in self.keywords):
			self.keywords.append(kw)
		return self

	def remove_keyword(self, kw):
		self.keywords = [x for x in self.keywords if x != kw]

	def get_name(self):
		return self.keywords[0]

	def generate(self):
		return self.keywords

	def to_dict(self):
		return {'User': self.user,
				'User Type' : self.type,
                'Keywords': self.keywords}

	def __eq__(self, other):
		return (self.keywords == other.keywords and self.user == other.user and self.type == other.type)
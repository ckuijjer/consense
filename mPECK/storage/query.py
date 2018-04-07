# Class to simplify query generation. Insert keywords with
# the set_...([keyword]) functions and generate query Q with 
# the generate() function. Can be utilised with consecutive 
# calls as follows:
#
#	Query()
#		.set_name("name_to_be_searched")
#		.set_field_type(1)
#		.generate()
#
# This will return a query Q in the format (I, W), where
# I is the list of indices of queried keywords, and W is
# the list of queried keywords.


class Query(object):
	"""docstring for Query"""
	def __init__(self):
		super(Query, self).__init__()
		self.indices = [0, 0, 0, 0, 0]
		self.keywords = [None, None, None, None, None]

	def set_name(self, value):
		self.indices[0] = 1
		self.keywords[0] = value
		return self

	def set_field_type(self, value):
		self.indices[1] = 1
		self.keywords[1] = value
		return self

	def set_date(self, value):
		self.indices[2] = 1
		self.keywords[2] = value
		return self

	def set_time(self, value):
		self.indices[3] = 1
		self.keywords[3] = value
		return self

	def set_amount(self, value):
		self.indices[4] = 1
		self.keywords[4] = value
		return self

	def remove_keyword(self, i):
		self.indices[i] = 1

	def generate(self):
		I = list()
		W = list()

		for x in range(0,5):
			if self.indices[x]==1:
				I.append(x)
				W.append(self.keywords[x])

		return (I,W)
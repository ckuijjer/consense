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

	def __init__(self):
		super(Query, self).__init__()
		self.indices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.keywords = [None, None, None, None, None, None, None, None, None, None, None]


	def set_keyword(self, index, value):
		self.indices[index] = 1
		self.keywords[index] = value
		return self


	def set_keywords_from_list(self, list_of_values):
		i = 0
		for elem in list_of_values:
			if elem is not None:
				self.indices[i] = 1
				self.keywords[i] = elem
			i = i + 1
		return self


	def remove_keyword(self, i):
		self.indices[i] = 0
		self.keywords[i] = None


	def generate(self):
		I = list()
		W = list()

		for x in range(0,5):
			if self.indices[x] == 1:
				I.append(x)
				W.append(self.keywords[x])
		return (I,W)
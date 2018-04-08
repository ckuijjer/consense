

from DataEnum import Data_Enum

class Query(object):

	def __init__(self):
		super(Query, self).__init__()
		self.indices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.keywords = [None, None, None, None, None, None, None, None, None, None, None]


	def set_keyword(self, value):
		self.indices[Data_Enum(value).value] = 1
		self.keywords[Data_Enum(value).value] = value
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

		for x in range(0, len(self.indices)):
			if self.indices[x] == 1:
				I.append(x)
				W.append(self.keywords[x])
		return (I,W)

class Server(object):

	def __init__(self):
		super(Server, self).__init__()
		self.data = list()
		self.users = list()
		self.ids = list()
		self.i = 0

	def next_id(self):
		i = self.i
		self.i += 1
		return i

	def store_data(self, u, ciphertext, i):
		if i is None:
			i = self.next_id()
			self.ids.append(i)
			self.data.append(ciphertext)
			self.users.append(u)
		else:
			index = self.ids.index(i)
			self.data[index] = ciphertext
		return i

	def delete(self, i):
		index = self.ids.index(i)
		del self.data[index]
		del self.users[index]
		del self.ids[index]

	def search(self, mpeck, pk, TQ):
		matches = list()
		for i, S in enumerate(self.data):
			res = mpeck.test((S, TQ, pk))
			if res != None:
				matches.append((self.users[i], self.ids[i], res))
		return matches
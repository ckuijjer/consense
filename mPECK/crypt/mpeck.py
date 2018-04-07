# Implementation of mPECK designed by Hwang and Lee. 
# 
# The scheme consists of 4 algorithms
# 
# 1. KeyGen
# 		takes as input a security parameter and returns 
# 		params (system parameters) and the public/private 
# 		key pairs (pk1, sk1), . . . , (pkn, skn).
# 2. mPECK
# 		is executed by the sender to encrypt a keyword set
# 		W = {w1, . . ., wL}. It produces a searchable 
# 		keyword encryption S of W with the public keys
# 		(pk1, . . . , pkn).
# 3. Trapdoor
# 		takes as input the secret key skj and the keyword 
# 		query Q = {I1, . . . , Im, wI1, . . . , wIm} for 
# 		m <= L where Ii is an index to denote a location of 
# 		wI1, and returns a trapdoor Tj,Q for the 
# 		conjunctive search of a given keyword query.
# 4. Test
# 		is executed by the server to search the documents 
# 		with the keywords of a trapdoor Tj,Q. It takes as 
# 		input the public key pkj, the searchable keyword 
# 		encryption S, and the trapdoor Tj,Q. It outputs 
# 		'1' if S includes Q and '0' otherwise.


from charm.toolbox.pairinggroup import PairingGroup,G1,pair
from charm.core.engine.util import objectToBytes,bytesToObject


class mPECK:
	def __init__(self):
		self.group = PairingGroup('SS512')


	def keygen(self, n, g=None):
		if(g==None):
			g = self.g_gen()
		keyPair_list = list()
		for a in range(n):
			keyPair_list.append(self.single_keygen(g))

		return keyPair_list


	def single_keygen(self, g):
		x = self.group.random()
		h = g ** x
		pk = {'g':g, 'h':h }
		sk = {'x':x}
		return (pk, sk)


	def g_gen(self):
		return self.group.random(G1)


	def m_peck(self, g, m, W, pks):
		s = self.group.random()
		r = self.group.random()
		E = self.m_enc(g, m, pks, r, s)
		A = g ** r
		B = list()
		for b in pks:
			B.append(b ** s)
		C = list()
		for w in W:
			h = self.group.hash(w, G1) ** r
			f = self.hash2(w, G1) ** s
			C.append(h * f)

		return (E,(A,B,C))


	def trapdoor(self,g, Q, sk):
		t = self.group.random()
		Q1 = g ** t
		Q2 = 1
		Q3 = 1
		for w in range(len(Q[0])):
			Q2 *= self.group.hash(Q[1][w], G1)
			Q3 *= self.hash2(Q[1][w], G1) 
		Q2 = Q2 ** t
		Q3 = Q3 ** (t/sk)
		return (Q1,Q2,Q3,Q[0])


	def test(self, ES, TQ, pk):
		P = 1
		for I in TQ[3]:
			P *= ES[1][2][I]

		lhs = pair(TQ[0], P)
		rhs = pair(ES[1][0], TQ[1])
		for B in ES[1][1]: 
			if lhs == rhs * pair(B, TQ[2]):
				return (ES[1][0],B,ES[0]) #this output format is described on page 16
		return None


	def m_enc(self, g, m, pks, r, s):
		return self.bytes_xor(objectToBytes(self.group.hash(pair(g,g) ** (r*s), G1), self.group), m) # TODO find suitable hashing function mapping to M


	def m_dec(self, sk, A, B, E):
		X = objectToBytes(self.group.hash(pair(A, B) ** (1/sk), G1), self.group)
		xor = self.bytes_xor(E, X)
		print(xor)
		return xor #if user is legitimate, this will be equal to m


	def hash2(self, m, type):
		return self.group.hash(self.group.hash(m, type), type) # TODO does this count as a second (different) hash function that maps to G1 ?


	def bytes_xor(self, a, b):
		return bytes(x ^ y for x, y in zip(a, b))


	def toBytes(self, m):
		return objectToBytes(m, self.group)


	def fromBytes(self, m):
		return bytesToObject(m, self.group)

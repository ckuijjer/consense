


from crypt.mpeck import mPECK
from storage.record import Record
from storage.server import Server
from storage.query import Query
from parties.user import User
from parties.user import User_Type
import json

def create_users(mpeck, n, names=None, verbose=False):
	if verbose:
		print('Creating %d users and generating keys...' % n)
	if names is not None:
		assert len(names) == n
	
	users = list()
	if(n < 1):
		return users
	ks = mpeck.keygen(n)

	# Define a researcher user
	users.append(User('researcher_1', User_Type.RESEARCHER))
	users[0].set_own_keys(ks[0])

	# Define patient users
	for i in range(1, n):
		name = str(i) if names is None else names[i - 1]
		users.append(User(name, User_Type.PATIENT))
		users[i].set_own_keys(ks[i])
		users[i].add_other_key_by_name(users[0].name, users[0].get_pub_key())
	return users


def decrypt_results(mpeck, C, sk, include_meta_data):
	P = list()
	for u, i, c in C:
		dec = mpeck.m_dec(sk, c[0], c[1], c[2])
		if include_meta_data:
			P.append((u, i, mpeck.fromBytes(dec)))
		else:
			P.append(mpeck.fromBytes(dec))
	return P


def run_query(mpeck, s, Q, u, include_meta_data=False, verbose=False):
	TQ = mpeck.trapdoor(u.get_g(), Q, u.get_pr_key())
	R = s.search(mpeck, u.get_pub_key(), TQ)
	decrypted = decrypt_results(mpeck, R, u.get_pr_key(), include_meta_data)
	if verbose:
		print('\n\n\n====================================\nQuery %s ->\n\n%s ->\n\n%s' % (Q, R, decrypted))
	return decrypted


def store_data(mpeck, s, D, U, i=None, verbose=False):
	m = mpeck.toBytes(D)
	PKS = list()
	for u in U:
		PKS.append(u.get_pub_key())
	C = mpeck.m_peck(U[0].get_g(), m, D, PKS)
	i = s.store_data(U[-1], C, i)
	if verbose:
		print('\n\n\n====================================\nStore (%d) %s ->\n\n%s' % (i, D, C))
	return Record(keywords=D, user=U[-1], i=i)


# Receive input from other processes
def load_data(path):
	return


#--------------------------------- MAIN ---------------------------


if __name__ == '__main__':

	mpeck = mPECK()
	server = Server()
	names = ['user_1','user_2','user_3','user_4','user_5','user_6']
	users = create_users(mpeck, 6, names)

	#print(users[0].serialize())

	R1 = Record(users[1], ['20', 'dna', 'Groningen'])
	R2 = Record(users[2], ['25', 'dna', 'Amsterdam'])
	R3 = Record(users[3], ['25', 'blood', 'Maastricht'])
	R4 = Record(users[4], ['30', 'blood', 'Maastricht'])
	R5 = Record(users[5], ['30', 'dna', 'Maastricht'])

	records = [R1, R2, R3, R4, R5]
	#print(R.__dict__())
	for elem in records:
		store_data(mpeck, server, elem.keywords, users)

	query = Query().set_keyword("dna").generate()






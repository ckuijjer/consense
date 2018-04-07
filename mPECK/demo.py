


from crypt.mpeck import mPECK
from storage.record import Record
from storage.server import Server
from storage.query import Query
from parties.user import User
from parties.consultant import Consultant
from parties.client import Client
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
	users.append(Consultant('researcher_1'))
	users[0].set_own_keys(ks[0])
	consultant_pub_key = users[0].get_pub_key()
	for i in range(1, n):
		name = str(i) if names is None else names[i - 1]
		users.append(Client(name))
		users[i].set_own_keys(ks[i])
		users[i].set_consultant_pub_key(consultant_pub_key)
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
	return Record(keywords=D, user=U[-1], userType = U[-1].type, i=i)



#--------------------------------- MAIN ---------------------------

if __name__ == '__main__':

	mpeck = mPECK()
	s = Server()
	names = ['user_1','user_2','user_3','user_4','user_5','user_6']
	users = create_users(mpeck, 6, names)

	usr_json = json.dumps(users[0], default=lambda x: x.__dict__, indent=4)
	print(usr_json)


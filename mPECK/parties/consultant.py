from parties.user import User

class Consultant(User):

    def __init__(self, name):
        super(Consultant, self).__init__()
        self.client_pub_keys = list()
        self.name = name
        self.type = "researcher"

    def add_client_pub_key(self, pub_key):
        if not any(pub_key in s for s in self.client_pub_keys):
            self.client_pub_keys.append(pub_key)

    def set_client_pub_keys(self, c):
        self.client_pub_keys = c

    # def __dict__(self):
    #     return "{Name : %s, Type : %s, Client_pks : {}}" % (self.name, self.type, self.client_pub_keys)

user_id = ""
password = ""
class RegisterCrud(object):
    def __init__(self):
        self.user_id = user_id
        self.password = password
    def create(self, user_id ,password):
        if user_id != "" and password != "" and isinstance ( user_id , str ):
            self.user_id = user_id
            self.password = password
        else:
            raise ValueError
        

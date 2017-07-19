users = { "User1" : "password1" , "User2" : "password2" }
class LoginAssert(object):
    def set(self, user_name , password ):
        if (user_name != "" and password != "" ):
            if isinstance ( user_name , str ):
                self.user_name = user_name
                self.password = password
                if self.user_name in users == True:
                    if users.get(self.user_name)== self.password:
                        print ( "Found account")
                    else:
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError


        


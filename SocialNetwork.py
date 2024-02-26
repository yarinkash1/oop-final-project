from User import User
class SocialNetwork:
    _instance = None

    def __new__(cls,name):
        # If an instance does not exist, create one
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name=name
            cls._instance.users=[]
            print("The social network " + name + " was created!")
        return cls._instance

    def get_users_array(self):
        return self.users

    def sign_up(self,username,password):
        user_exist=True
        valid_password=False
        if not username in self.users:
            user_exist=False
        password_length=len(password)
        if(password_length>=4 and password_length<=8):
            valid_password=True
        if(user_exist==False and valid_password==True):
            new_user = User(username,password)
            self.users.append(new_user)
            new_user.set_status(True)
            return new_user


    def log_in(self,username,password):

        i = 0
        for i in range(len(self.users)):
            if(self.users[i].get_username()==username and self.users[i].get_password()==password):
                self.users[i].set_status(True)
                print(self.users[i].get_username() + " connected")

    def log_out(self,username):

        i = 0
        for i in range(len(self.users)):
            if(self.users[i].get_username()==username):
                self.users[i].set_status(False)
                print(self.users[i].get_username() + " disconnected")

    def __str__(self):
        string=f"{self.name} social network:\n"
        for user in self.users:
            string+=str(user)+"\n"
        return string






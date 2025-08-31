class userManager:
    def __init__(self):
        self.users={}

    def add_users(self,username,email):
        if username in self.users:
            raise ValueError("User Already exist")
        
        self.users[username]=email
        return True
    
    def get_user(self,username):
        return self.users[username]
    
    
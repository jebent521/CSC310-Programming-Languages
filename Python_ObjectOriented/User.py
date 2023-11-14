# Jonah Ebent, 11/17/23, CSC 310 Programming Languages, HW14
class User:
    userList = []       # stores usernames so there can't be duplicates
    blacklist = []      # stores usernames that can't be chosen

    def __init__(self, username, password) -> None:
        # error handling
        if username in User.userList:                       # username can't be taken
            raise ValueError("Username already taken")
        if username in User.blacklist:                      # username can't be in blacklist
            raise ValueError("Username is invalid")
        if not isinstance(username, str):                   # username must be a string
            raise ValueError("Username must be a string")
        if not (isinstance(password, str)):                 # password must be a string
            raise ValueError("Password must be a string")
        if not User.checkPassword(password):                # password must be strong enough
            raise ValueError("Password is not strong enough")
        
        User.userList.append(username)
        self.username = username
        self._password = password

    def __del__(self):
        User.userList.remove(self.username)

    def __repr__(self) -> str:
        return f'User("{self.username}", "{self._password}")'

    def __str__(self) -> str:
        return self.username
    
    def changePassword(self, oldPassword, newPassword):
        if oldPassword != self._password:                   # oldPassword must match current password
            raise ValueError("Old password doesn't match current password")
        if not isinstance(newPassword, str):                # newPasssword must be a string
            raise ValueError("New password must be a string")
        if not User.checkPassword(newPassword):             # newPassword must be strong enough
            raise ValueError("New password not strong enough")
        self._password = newPassword

    @classmethod
    def blacklistNames(cls, *usernames):
        '''adds usernames to blacklist so that users can't have them'''
        cls.blacklist += usernames
    
    @classmethod
    def whitelistNames(cls, *usernames):
        '''removes usernames from blacklist so that users can have them'''
        for username in usernames:
            cls.blacklist.remove(username)

    @staticmethod
    def checkPassword(password):
        '''returns True if password is strong enough, False if otherwise'''
        if len(password) < 10: return False                                         # length >= 10
        if not any(chr.isdigit() for chr in password): return False                 # must contain digit
        if not any(chr in "[@_!#$%^&*()<>?}{~:]" for chr in password): return False # must contain special character
        return True
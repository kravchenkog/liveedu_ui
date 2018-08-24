class UserData:
    def __init__(self, skype=None, role=None, passwords=None, email=None,  username=None, password1=None, password2=None, userrole=None, slug=None):
        self.email = email
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.userrole = userrole
        self.slug = slug
        self.role = role
        self.passwords = passwords
        self.skype = skype
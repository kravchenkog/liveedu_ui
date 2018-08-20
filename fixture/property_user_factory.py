class UserData:
    def __init__(self, email=None, password=None, username=None, password1=None, password2=None, userrole=None, slug=None):
        self.email = email
        self.password = password
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.userrole = userrole
        self.slug = slug




class UserParseFactory:


    def parse_user_properties(self, resp_dict=None):
        user = UserData()
        all_fields = ['email', 'publick_key', 'username', 'password1', 'password2']
        for field in all_fields:
            if field in resp_dict.keys():
                setattr(user, field, resp_dict[field])

        return user
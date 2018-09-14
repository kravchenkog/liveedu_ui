
class Route:
    def __init__(self):
        self.check_email = '/api/v3/auth/registration/check-email/'
        self.get_public_key = '/api/v3/auth/public-key/'
        self.check_password = '/api/v3/auth/registration/check-password/'
        self.check_username = '/api/v3/auth/registration/check-username/'
        self.register = '/api/v3/auth/registration/register/'
        self.topics = '/api/v3/topics/'
        self.email_confirmation = '/api/v3/auth/registration/verify-email/'
        self.login = '/api/v3/auth/login/'
        self.categories = '/api/v3/categories/'
        self.projects_suggestions = '/api/v3/projects-suggestions/'


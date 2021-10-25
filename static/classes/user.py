class User:
    def __init__(self, name="Nome", email="generic@generic.com"):
        self.user_id = 0
        self.name = name.title()
        self.email = email
        self.password_hash = ""
        self.social_media_id = ""
        self.picture_url = ""
        self.birthday_date = "01/01/2001"
        self.admin = False
        self.validate = False

    def logoff(self):
        self.user_id = 0
        self.name = ""
        self.email = ""
        self.password_hash = ""
        self.social_media_id = ""
        self.picture_url = ""
        self.birthday_date = "01/01/2001"
        self.admin = False
        self.validate = False




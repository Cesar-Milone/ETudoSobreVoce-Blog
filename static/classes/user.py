
class User:
    def __init__(self, user_id, fname, lname, email, password_hash, password_salt, cpf, social_media_id,
                 picrue_url, birthday_date):
        self.user_id = user_id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password_salt = password_salt
        self.password_hash = password_hash
        self.cpf = cpf
        self.social_media_id = social_media_id
        self.picture_url = picrue_url
        self.birthday_date = birthday_date

    def insert_user_db(self):
        sql = f"INSERT INTO public.user_table(" \
              f"user_id, fname, lname, password_hash, password_salt, cpf, social_media_url, " \
              f"picture_url, birthday_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
        return True




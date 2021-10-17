import psycopg2


class Database:
    def __init__(self):
        self.conn = psycopg2.connect("dbname='blog_data' user='postgres' host='localhost' password='123'")
        self.cur = self.conn.cursor()
        self.post_title = ""
        self.post_subtitle = ""
        self.user_id = 0
        self.post_body = ""
        self.comment_id = 0

    def exec_select(self):
        sql_query = "SELECT * FROM public.post_table " \
                    "ORDER BY post_id ASC "

        self.cur.execute(sql_query)
        return self.cur.fetchall()

    def exec_insert(self):
        sql_query = f"INSERT INTO public.post_table(" \
                    f"post_title, post_subtitle, user_id, post_body, comment_id) " \
                    f"VALUES ('{self.post_title}', '{self.post_subtitle}', {self.user_id}, " \
                    f"'{self.post_body}', {self.comment_id});"
        print(sql_query)
        self.cur.execute(sql_query)
        self.conn.commit()

    def exec_delete(self, post_id):
        if post_id != 0:
            sql_query = f"DELETE FROM public.post_table " \
                        f"WHERE post_id = {post_id}"
            return self.cur.execute(sql_query)
        else:
            return False

    def exec_update(self, post_id):
        if post_id != 0:
            sql_query = f"UPDATE public.post_table " \
                        f"SET post_title = {self.post_title}, post_subtitle = {self.post_subtitle}, " \
                        f"post_body = {self.post_body}" \
                        f"WHERE post_id = {post_id};"
            return self.cur.execute(sql_query)
        else:
            return False

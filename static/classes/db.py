import psycopg2
import pandas as pd

db_server = {
    "host": "ec2-54-164-22-242.compute-1.amazonaws.com",
    "database": "d955444mit53rq",
    "user": "uaqgakbkzsgimy",
    "port": 5432,
    "password": "9203b4c0a73e865cc5b0a6f1a5ea0e13033bdb5faea8e9c4c55c14116906d3de",
    "uri": "postgres://uaqgakbkzsgimy:9203b4c0a73e865cc5b0a6f1a5ea0e13033bdb5faea8e9"
           "c4c55c14116906d3de@ec2-54-164-22-242.compute-1.amazonaws.com:5432/d955444mit53rq",
    "heroku cli": "heroku pg:psql postgresql-adjacent-44014 --app etudosobrevoce-blog",
}
db_local = {
    "host": "localhost",
    "database": "blog_data",
    "user": "postgres",
    "port": 5432,
    "password": "123",
}
DB_TABLE = "post_table"
LOCAL_SERVER = 1  # 0 to local and 1 to server


class Database:
    def __init__(self):
        if LOCAL_SERVER == 0:
            self.conn = psycopg2.connect(host=db_local['host'], database=db_local['database'],
                                         port=db_local['port'], user=db_local['user'], password=db_local['password'])
        elif LOCAL_SERVER == 1:
            self.conn = psycopg2.connect(host=db_server['host'], database=db_server['database'],
                                         port=db_server['port'], user=db_server['user'], password=db_server['password'])

        sql_create_table = f"CREATE TABLE IF NOT EXISTS {DB_TABLE} (" \
                           "post_id serial PRIMARY KEY, post_title CHARACTER VARYING(255) unique NOT NULL, " \
                           "post_subtitle CHARACTER VARYING(255), post_body CHARACTER VARYING(10000) NOT NULL, " \
                           "user_id INTEGER);"
        self.cur = self.conn.cursor()
        self.cur.execute(sql_create_table)
        self.conn.commit()
        self.post_title = ""
        self.post_subtitle = ""
        self.user_id = 0
        self.post_body = ""
        self.comment_id = 0

    def exec_select(self):
        sql_query = "SELECT * FROM public.post_table " \
                    "ORDER BY post_id ASC "

        self.cur.execute(sql_query)
        rows = self.cur.fetchall()
        self.cur.close()
        return rows

    def exec_insert(self):
        sql_query = f"INSERT INTO public.post_table(" \
                    f"post_title, post_subtitle, user_id, post_body) " \
                    f"VALUES ('{self.post_title}', '{self.post_subtitle}', {self.user_id}, " \
                    f"'{self.post_body}');"
        sql_select = f"SELECT * FROM public.post_table " \
                     f"WHERE post_title = '{self.post_title}'"
        self.cur.execute(sql_select)
        rows = self.cur.fetchall()
        if not rows:
            try:
                self.cur.execute(sql_query)
                self.conn.commit()
                return True
            except psycopg2.errors.UniqueViolation or psycopg2.errors.InFailedSqlTransaction:
                return False
        else:
            return False

    def exec_delete(self, post_id):
        cur = self.conn.cursor()
        if post_id != 0:
            sql_query = f"DELETE FROM public.post_table " \
                        f"WHERE post_id = {post_id}"
            cur.execute(sql_query)
            self.conn.commit()
            return True
        else:
            return False

    def exec_update(self, post_id):
        cur = self.conn.cursor()
        if post_id != 0:
            sql_query = f"UPDATE public.post_table " \
                        f"SET post_title = {self.post_title}, post_subtitle = {self.post_subtitle}, " \
                        f"post_body = {self.post_body}" \
                        f"WHERE post_id = {post_id};"
            cur.execute(sql_query)
            self.conn.commit()
            return True
        else:
            return False

    def exec_select_pandas(self):
        sql_query = "SELECT * FROM public.post_table " \
                    "ORDER BY post_id ASC "
        return pd.read_sql(sql_query, self.conn)


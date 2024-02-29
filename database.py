
import  psycopg2
class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='kun_uz',
            user='postgres',
            password='2004',
            host='localhost'
        )

    def manager(self, sql, *args,
                fetchone:bool=False,
                fetchall:bool=False,
                fetchmany:bool=False,
                commit:bool=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result

    def create_table_categories(self):
            sql='''CREATE TABLE IF NOT EXISTS categories(
                categories_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                categories_name VARCHAR(50) UNIQUE NOT NULL
            )  '''
            self.manager(sql,commit=True)
    def insert_category(self,category):
        sql='''INSERT INTO categories(categories_name) VALUES (%s) ON CONLICE DO NOTHING'''
        self.manager(sql,(category,),commit=True)
    def create_table_articels(self):
        sql='''CREATE TABLE IF NOT EXISTS articels(
            articels_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            title VARCHAR(20),
            content TEXT,
            created TIMESTAMP DEFAULT NOW(),
            views INTEGER
            
            )'''
        self.manager(sql,commit=True)

db=DataBase()
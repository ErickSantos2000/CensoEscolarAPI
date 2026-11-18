import os

import psycopg
from psycopg.rows import dict_row
from flask import g

def get_conn():
    if "db" not in g:
        # credenciais vêm do .env (carregado no app.py); nada fica escrito no código
        g.db = psycopg.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            # equivalente ao sqlite3.Row: acessa as colunas pelo nome (row["id"])
            row_factory=dict_row,
        )
    return g.db


def close_conn(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()
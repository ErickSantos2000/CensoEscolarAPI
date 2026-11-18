import os
import sqlite3
from flask import g


DATABASE = os.getenv("DATABASE_PATH", "censoescolar.db")


def get_conn():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_conn(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

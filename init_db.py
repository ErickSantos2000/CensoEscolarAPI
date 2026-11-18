import sqlite3

from pathlib import Path

from helpers.database import DATABASE


connection = None
try:
    connection = sqlite3.connect(DATABASE)
    with open(Path(__file__).with_name("schema.sql"), encoding="utf-8") as schema_file:
        connection.executescript(schema_file.read())
    connection.commit()
except sqlite3.Error as error:
    print(f"O banco lançou uma exceção: {error}")
finally:
    if connection is not None:
        connection.close()

import os

import psycopg
from pathlib import Path
from dotenv import load_dotenv

# fora do Flask não existe get_conn() (depende do g), então conecta direto
load_dotenv()

connection = None
try:
    connection = psycopg.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    with open(Path(__file__).with_name("schema.sql"), encoding="utf-8") as schema_file:
        # sem parâmetros, o psycopg executa vários comandos de uma vez (como o executescript)
        connection.execute(schema_file.read())
    connection.commit()
except psycopg.Error as error:
    print(f"O banco lançou uma exceção: {error}")
finally:
    if connection is not None:
        connection.close()

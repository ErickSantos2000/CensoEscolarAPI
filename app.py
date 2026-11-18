import os

from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from controllers.InstituicoesEnsinoController import instituicao_bp
from helpers.database import close_conn


app = Flask(__name__)
app.teardown_appcontext(close_conn)
app.register_blueprint(instituicao_bp)


@app.route("/")
def index():
    return {"versao": "0.0.1"}, 200


@app.route("/health")
def health():
    return {"health": "ok"}, 200


if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("FLASK_PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
    )

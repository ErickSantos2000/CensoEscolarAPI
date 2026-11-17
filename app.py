
from flask import Flask
from helpers.database import close_conn
from controller.InstituicaoEnsinoController import instituicao_bp
 
# instancia o app flask
app = Flask(__name__)
 
# registra o teardown
app.teardown_appcontext(close_conn)
 
# registra os controllers (rotas)
app.register_blueprint(instituicao_bp)
 
 
@app.route("/")
def index():
    return {"versao": "0.0.1"}, 200
 
 
@app.route("/health")
def health():
    return {"health": "ok"}, 200
 
 
def main(arg=[]):
    app.run(debug=True)
 
 
if __name__ == '__main__':
    main()
 
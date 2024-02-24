from flask import Flask
from .api import login, access_data, make_transaction

app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(access_data)
app.register_blueprint(make_transaction)

if __name__ == "__main__":
    app.run(debug=True)

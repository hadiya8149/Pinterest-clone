from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,static_url_path='', static_folder='static', template_folder='templates')


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
#from memory_profiler import profile
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
db = SQLAlchemy(app)


#@profile
class PinClone(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    image = Column(Text, unique=False)


db.create_all()


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)

"""
A simple Campus study spaces flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from sign import Sign
from details import details


app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/sign/',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

app.add_url_rule('/details/',
                 view_func=details.as_view('details'),
                 methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))

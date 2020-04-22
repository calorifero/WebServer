from flask import Flask, request
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
import config as c

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''  # Insert connection data
db = SQLAlchemy(app)


from src.database import init_database
init_database()
from .schema import schema


@app.route('/', methods=['POST'])
def main():
    req = request.values.get('value')
    print(req)


@app.teardown_appcontext
def close_session(exception=None):
    db.close_all_sessions()


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

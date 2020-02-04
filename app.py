#!/usr/bin/env python

from database import db_session, init_db, test_db
from flask import Flask
from schema import schema
from flask_cors import CORS
from flask_graphql import GraphQLView

app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql",
                                  schema=schema,
                                  graphiql=True,
                                  context={'session': db_session}))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')
    init_db()
    test_db()

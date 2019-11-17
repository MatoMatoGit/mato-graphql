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
    "/graphql", view_func=GraphQLView.as_view("graphql",
                                              schema=schema,
                                              graphiql=True)
)

example_query = """
{
  allMeasurements {
    edges {
      node {
        id
        uuid
        data
        createdOn
        hash
      }
    }
  }
  
  allSensors {
    edges {
      node {
        id
        uuid
        hash
      }
    }
  }
}
"""


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    init_db()
    test_db()
    app.run()

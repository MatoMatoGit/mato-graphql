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
                                              graphiql=True,
                                              context={'session': db_session}))

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

example_mutation = """
mutation {
  createMeasurement(data:888, hash:"TESTHASH"){
    measurement{
      id
      data
      createdOn
      uuid
    }
    sensor {
      id
      hash
    }
  }
}
"""

if __name__ == "__main__":
    # init_db()
    test_db()
    app.run()

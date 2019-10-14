import os
import graphene

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView

basedir = os.path.abspath(os.path.dirname(__file__))

# INIT
app = Flask(__name__)
app.debug = True
CORS(app)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# MODULES
db = SQLAlchemy(app)

# Models
class Measurement(db.Model):
    __tablename__ = 'measurement'
    uuid = db.Column(db.Integer, primary_key=True)
    sensorKey = db.Column(db.String(256), index=True)

    def __repr__(self):
        return '<Measurement %r>' % self.uuid


# Schema Objects
class MeasurementObject(SQLAlchemyObjectType):
    class Meta:
        model = Measurement
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_measurements = SQLAlchemyConnectionField(MeasurementObject)


schema = graphene.Schema(query=Query)

# Routes
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run()

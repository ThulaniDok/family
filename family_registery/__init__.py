# import the framework
import shelve
import markdown
import os
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)


# Create the API
api = Api(app)


# db connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("family.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


# Create the API
class FamilyList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        family = []

        for key in keys:
            family.append(shelf[key])

        return {'message': 'Success', 'data': family}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True)
        parser.add_argument('gender', required=True)
        parser.add_argument('age', required=True)
        parser.add_argument('occupation', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['name']] = args

        return {'message': 'Member registered', 'data': args}, 201


class Member(Resource):
    def get(self, name):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (name in shelf):
            return {'message': 'Member not found', 'data': {}}, 404

        return {'message': 'Member found', 'data': shelf[name]}, 200

    def delete(self, name):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (name in shelf):
            return {'message': 'Member not found', 'data': {}}, 404

        del shelf[name]
        return '', 204


api.add_resource(FamilyList, '/')
api.add_resource(Member, '/family/<string:name>')
